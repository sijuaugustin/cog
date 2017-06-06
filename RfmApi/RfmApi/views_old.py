'''
Created on Jul 29, 2016

@author: cloudera
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from pymongo import MongoClient
from pyzipcode import Pyzipcode as pz
#ZIPType = ['33131']
@permission_classes((permissions.AllowAny,))

class rfm(viewsets.ViewSet):

    def list(self, request):

#             try:
#                 if request.query_params['zip'] not in ZIPType:
#                     return Response({'status':'ERROR','error':'INVALID_POSTALCODE'})
            try:
                if not request.query_params['zip'].isdigit():
                    return Response({'status':'ERROR','error':'INVALID_ZIP'})
            except:
                return Response({'status':'ERROR','error':'NO_ZIP_SPECIFIED'})
#             try:
#                 zipcode = pz.get(str(request.query_params['zip']),"US")
#             except:
#                 return Response({'status':'ERROR','error':'Invalid ZipCode'})
#                
 
                     
#             except:
#                 return Response({'status':'ERROR','error':'NO_SPAN_SPECIFIED'}) 
            
            req_zip=request.query_params['zip']
            data=[]  
            db_client = MongoClient(host='169.45.215.122', port=27017)
#             data = list(db_client.iestimate.HeatMapMediansZipWise.find({}))
#             heat_data=[]
            #level_map = {"State":{"collection":"HeatMapMediansStateWise"}}
           # level_map = {"County":{"collection":"HeatMapMediansCountyWise_copy"}}
            #feture_data_List=[]
            #cords=[]
            data_= list(db_client.RFM.RFMSCORE_zip.find({'postalcode':req_zip},{'Agent_data':1}).limit (10))
            if len(data_)==0:
                return Response({'status':'No data to display'})
            else:
                for row in data_:
                    data.append(row['Agent_data'])
            
                calc = {'Top 10 agents':data}
                return Response(calc)

 