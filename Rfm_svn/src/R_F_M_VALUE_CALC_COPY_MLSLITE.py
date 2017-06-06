'''
Created on Nov 4, 2016

@author: sysadmin
'''
from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
dist_agnt=[{ '$group': {'_id': "$ListAgentFullName"}  },
    { '$group': { '_id': 1, 'count': { '$sum': 1 } } }]
for row in list(db_client.MLSLite.listing_unique.aggregate(dist_agnt)):
#for row in list(db_client.MLSLite.listing_unique.find({},{"ListAgentFullName":1,"_id":0})):
#agents="Garfield Lalah"


        try:
            print row['ListAgentFullName']
            AGENTINFO=db_client.MLSLite.listing_unique.find({"ListAgentFullName":row['ListAgentFullName']},{"ListAgentKey":1,
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
                                                              })
            Data_notrans = list(db_client.MLSLite.listing_unique.find(
                                                                {
                                                                "ListAgentFullName":row['ListAgentFullName'],
                                                                "CloseDate": {"$gte": "2014-01-01"},
                                                                "StandardStatus":"Sold"
                                                                },
                                                                {
                                                                "ClosePrice":1,"CloseDate":1,
                                                                "ListPrice":1,"SI_DaysOnMarket":1,"ListingId":1,"Longitude":1,"Latitude":1,"location":1,"SI_FIPS":1,"PublicRemarks":1,
                                                                "DaysOnMarket":1,
                                                                "City":1,"SI_Address":1,
                                                                
                                                                "server_id":1,
                                                                "StateOrProvince":1,"SI_PropertyRefID":1,"PropertyType":1, "PropertySubType" :1,

                                                                "PostalCode" :1,"ListOfficeEmail":1,"ListOfficeName" :1,"ClassName":1
                                                                
  }
                                                                ))
            n_trans = len(Data_notrans)
            if n_trans>5:
                agent={"AgentName":row['ListAgentFullName'],"Transactions":Data_notrans,"number of Transactions":n_trans,"AgentInfo":AGENTINFO}
            #print Data[i]['NOT']

                print len(agent)          
                db_client.RFM.MLSLITE_LIST_AGENT.insert(agent)
                print 'pass'
            else:
                continue

            #db_client.RFM.Agents.insert()

        except:
                print 'error data'
#print 'pass'
