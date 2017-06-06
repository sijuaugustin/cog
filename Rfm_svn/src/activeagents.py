'''
Created on Aug 17, 2016

@author: cloudera
'''
from pymongo import MongoClient 
db_client = MongoClient(host='169.45.215.122', port=27017)
agents= list(db_client.iestimate.rets_standardized_data_new.find({"ListAgentFullName":{"$ne":None},"CloseDate": {"$gte": "2015-01-01"}},{"ListAgentFullName":1,"rets_id":1}))
#agents="Garfield Lalah"
#print agents
print len(agents)
print 'pass'
# for i in range(len(agents)):
#         try:
#             print agents[i]
#             agen=list(db_client.iestimate.rets_standardized_data_new.find({"ListAgentFullName":agents[i], "ListAgentFullName":{"$ne":None},"CloseDate": {"$gte": "2015-01-01"}}))
#             print len(agen)
#             if len(agen)>1:
#                 ActiveAgents=list(agents[i])
#         except Exception as ex:
#             print ex
# print len(ActiveAgents)
for i in range(len(agents)):
        try:
            agentdata=[
                                               {"$match":
                                                    {   "ListAgentFullName":agents[i]
                                                        
                                                                 
                                                }},
                                               {"$group":
                                                {
                                                 "_id" : {"PostalCode":"$PostalCode","ListAgentFullName":"$ListAgentFullName","CountyOrParish":"$CountyOrParish","StateOrProvince":"$StateOrProvince"},
                                                 "Transactions":{"$push":{"SI_Address":"$SI_Address","ClosePrice":"$ClosePrice",
                                                                "ListPrice":"$ListPrice",
                                                                "DaysOnMarket":"$DaysOnMarket",
                                                                "StateOrProvince":"$StateOrProvince",
                                                                "rets_id":"$rets_id",
                                                                "server_id":"$server_id",
                                                                "StandardStatus":"$StandardStatus",
                                                                "CloseDate":"$CloseDate",
                                                                "PreviousListPrice":"$PreviousListPrice",
                                                                "PostalCode" :"$PostalCode",
                                                                "CountyOrParish":"$CountyOrParish"}
                                                                  },
                                                 "count": { "$sum": 1 }
                                                   
                                                  
                                                  
                                                 }
                                                }
                                               ]
            agentsunique=list(db_client.iestimate.rets_standardized_data_new.aggregate(agentdata))
           # n_trans = len(agentsunique)
             
              
            db_client.RFM.agent_list.insert_many(agentsunique)
            #print data
        except Exception as ex:
         print ex
 
             
