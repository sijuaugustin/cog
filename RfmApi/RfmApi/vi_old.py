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
                if  request.query_params['level'].isdigit():
                    return Response({'status':'ERROR','error':'INVALID_LEVEL'})
            except:
                return Response({'status':'ERROR','error':'NO_LEVEL_SPECIFIED'})
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
                    
#             data = list(db_client.iestimate.HeatMapMediansZipWise.find({}))
#             heat_data=[]
            #level_map = {"State":{"collection":"HeatMapMediansStateWise"}}
           # level_map = {"County":{"collection":"HeatMapMediansCountyWise_copy"}}
            #feture_data_List=[]
            #cords=[]
                    data=[]
                    data_=list(db_client['RFM'][level].find({level:value},{'Agent_data.AgentName':1,'Agent_data.rfm':1,'Agent_data.R_Score':1,'Agent_data.F_Score':1,'Agent_data.M_    Score':1,'Agent_data.last_transaction_dates':1}).limit(10))
                    print data_
                    print len( data_)
                    name=[]
                    for i in range(len(data_))[:10]:
                        name.append(data_[i]['Agent_data'])
#                     for row in data_:
#                         print row['Agent_data.AgentName']
                    #name=[]
                    #for i in data_:
                        #print i['AgentName']
                    #print name    
                    calc={'Top Agents':name}
                    #print calc
#                     print calc
#                     
#                     for i in range(len(data_)):
#                             
#                         calc={'agents data':i}
#                         data.append(calc)
                    return calc
#                     print data_
#                     if len(data_)==0:
#                         return Response({'status':'No data to display'})
#                     else:
# #                         for row in data_:
# #                             data.append(row['Agent_data'])
# #                       
# #                         calc = {'Top 10 agents':data}
# #                         print calc
#                         #return data_
#                         return Response(data_)
            req_level=request.query_params['level']
            print req_level
            req_value= request.query_params['value']
            if req_level=='states':
                dat=RfmFilter.rfm('states',req_value)
                print type(dat)
                return Response(dat)
               
            elif req_level=='County':
                dat=RfmFilter.rfm('County',req_value)
                return Response(dat)
            elif req_level=='post':
                dat=RfmFilter.rfm('post',req_value)
                return Response(dat) 
                #return Response(da)
#             elif req_level=='postal_code':
#                 RfmFilter.rfm('postal_code',req_value)                       

 