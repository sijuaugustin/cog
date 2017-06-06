'''
Created on Nov 22, 2016

@author: sysadmin
'''

'''
Created on Nov 18, 2016

@author: sysadmin
'''
from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
STATE=db_client.MLSLite.mlslite_unique.distinct("StateOrProvince")
print len(STATE)
for st in STATE:
    if st==None:
        continue
   
        
#         dist_agnt=[{"$match":
#                                                             {   "StateOrProvince":st
#                                                                  
#                                                                           
#                                                         }},{ '$group': {'_id': "$ListAgentFullName"},
#                                                                         "Transactions":{"$push":{"ClosePrice":"$ClosePrice",
#                                                                     "ListPrice":"$ListPrice",
#                                                                  "CloseDate":"$CloseDate",
#                                                                     "SI_DaysOnMarket":"$SI_DaysOnMarket","ListingId":"$ListingId"
#                                                                      }}  }
#             ]
    distagents= list(db_client.MLSLite.mlslite_unique.distinct("ListAgentFullName",{"StateOrProvince" :st}))
    print len(distagents)
    agent_info_statewise=[]
    for row in distagents:
                if row==None:
                    continue
                #print row                   
                AGENTINFO=list(db_client.MLSLite.mlslite_unique.find({"ListAgentFullName":row,"StateOrProvince":st},{"ListAgentKey":1,
                                                                        "ListAgentAOR" : 1,
                                                                    "ListAgentCellPhone" : 1,
                                                                    "ListAgentDesignation" : 1,
                                                                    "ListAgentDirectPhone" : 1,
                                                                    "ListAgentEmail" :1,
                                                                    "ListAgentFax" : 1,
                                                                    "ListAgentFirstName" : 1,
                                                                    "ListAgentFullName" :1,
                                                                    "ListAgentHomePhone" : 1,
                                                                    "ListAgentKey" : 1,
                                                                    "ListAgentLastName" : 1,
                                                                    "ListAgentMiddleName" : 1,
                                                                    "ListAgentMlsId" : 1,
                                                                    "ListAgentNamePrefix" : 1,
                                                                    "ListAgentNameSuffix" : 1,
                                                                    "ListAgentOfficePhone" : 1,
                                                                    "ListAgentOfficePhoneExt" : 1,
                                                                    "ListAgentPager" : 1,
                                                                    "ListAgentPreferredPhone" : 1,
                                                                    "ListAgentPreferredPhoneExt" : 1,
                                                                    "ListAgentStateLicense" : 1,
                                                                    "ListAgentTollFreePhone" : 1,
                                                                    "ListAgentURL" : 1,
                                                                    "ListAgentVoiceMail" : 1,
                                                                    "ListAgentVoiceMailExt" :1,
     
     
                                                                    "CoListAgentFullName" :1,
     
                                                                    "CoListAgentEmail" : 1,
     
     
                                                                    "BuyerAgentFullName" : 1,
     
                                                                    "BuyerAgentCellPhone" :1,
                                                                    "CoBuyerAgentFullName" : 1,
     
                                                                    "CoBuyerAgentOfficePhone" : 1
                                                                  }))
                info=AGENTINFO[0]
                Data_notrans = list(db_client.MLSLite.mlslite_unique.find(
                                                                    {
                                                                    "ListAgentFullName":row,
                                                                    "CloseDate": {"$gte": "2014-01-01"},
                                                                    "StateOrProvince":st
                                                                    },
                                                                    {
                                                                    "ClosePrice":1,"CloseDate":1,
                                                                    "ListPrice":1,"SI_DaysOnMarket":1,"ListingId":1,"Longitude":1,"Latitude":1,"location":1,"SI_FIPS":1,"PublicRemarks":1,
                                                                    "DaysOnMarket":1,
                                                                    "City":1,"SI_Address":1,
                                                                     
                                                                    "server_id":1,
                                                                    "StateOrProvince":1,"SI_PropertyRefID":1,"PropertyType":1, "PropertySubType" :1,
     
                                                                    "PostalCode" :1,"ListOfficeEmail":1,"ListOfficeName" :1,"ClassName":1,'ListAgentFullName':1
                                                                     
      }
                                                                    ))
                n_trans = len(Data_notrans)
                #print n_trans
                if n_trans>5:
                    #print 'pass'
                    agent={"AgentName":row,"Transactions":Data_notrans,"number of Transactions":n_trans,"AgentInfo":AGENTINFO[0] }
                    agent_info_statewise.append(agent)
                #print Data[i]['NOT']
     
                    #print agent          
    if len(agent_info_statewise)>2:
        AGNTDATA={'STATE':st,'Agentdata':agent_info_statewise}
        db_client.RFM_mlslite.Agents_statewise_.insert(AGNTDATA)
        print 'pass'


     
                #db_client.RFM.Agents.insert()
     
     
 

    