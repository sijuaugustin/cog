from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes 
from rest_framework import permissions
from pymongo import MongoClient
#from pyzipcode import Pyzipcode as pz

@permission_classes((permissions.AllowAny,))

class rfm(viewsets.ViewSet):

    def list(self, request):

#             try:
#                 if request.query_params['zip'] not in ZIPType:
#                     return Response({'status':'ERROR','error':'INVALID_POSTALCODE'})
            try:
                if  request.query_params['level'].isdigit():
                    return Response({'status':'ERROR','error':'INVALID_LEVEL'})
            except:
                return Response({'status':'ERROR','error':'NO_LEVEL_SPECIFIED'})
            try:
                if  request.query_params['value'].isalpha():
                    return Response({'status':'ERROR','error':'INVALID_VALUE'})
            except:
                return Response({'status':'ERROR','error':'NO_VALUE_SPECIFIED'})
#             try:
#                 zipcode = pz.get(str(request.query_params['zip']),"US")
#             except:
#                 return Response({'status':'ERROR','error':'Invalid ZipCode'})
#                
 
                     
#             except:
#                 return Response({'status':'ERROR','error':'NO_SPAN_SPECIFIED'}) 
            
            
             
            db_client = MongoClient(host='52.91.122.15', port=27017)
            class RfmFilter:
                @staticmethod
                def rfm(level,value):

                    data=[]
                    data_=list(db_client['RFM_mlslite'][level].find({level:value},{'Agent_data.AgentName':1,'Agent_data.rfm':1,'Agent_data.R_Score':1,'Agent_data.F_Score':1,'Agent_data.M_Score':1,'Agent_data.last_transaction_date':1}).limit(10))
                    #print data_
                    print len( data_)
                    name=[]
                    tenagents=[]
                    for x in xrange(10):
                        tenagents.append(data_[0]['Agent_data'][x])
#                         
#                     for i in range(len(data_))[:10]:
#                         name.append(data_[i]['Agent_data'])

                    calc={'Top Agents':tenagents}

                    return calc

            req_level=request.query_params['level']
            print req_level
            req_value= request.query_params['value']
            if req_level=='State':
                dat=RfmFilter.rfm('State',req_value)
                print type(dat)
                return Response(dat)
               
            elif req_level=='County':
                dat=RfmFilter.rfm('COUNTY',req_value)
                return Response(dat)
            elif req_level=='post':
                dat=RfmFilter.rfm('post',req_value)
                return Response(dat) 
                #return Response(da)
#             elif req_level=='postal_code':
#                 RfmFilter.rfm('postal_code',req_value)                       

 