from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
agents= list(db_client.MLSLite.listing_unique.distinct("ListAgentFullName"))
#agents="Garfield Lalah"
print len(agents)

for i in range(len(agents)):
        try:
            print agents[i]
            listkey=db_client.MLSLite.MiamiMlsLite.find_one({"ListAgentFullName":agents[i]},{"ListAgentKey":1})
            Data_notrans = list(db_client.MLSLite.listing_unique.find(
                                                                {
                                                                "ListAgentFullName":agents[i],
                                                                "CloseDate": {"$gte": "2014-01-01"},
                                                                "StandardStatus":"Sold"
                                                                },
                                                                {
                                                                "ClosePrice":1,
                                                                "ListPrice":1,"SI_DaysOnMarket":1,"ListingId":1,"Longitude":1,"Latitude":1,"location":1,"SI_FIPS":1,"PublicRemarks":1,
                                                                "DaysOnMarket":1,
                                                                "City":1,"ListAgentPreferredPhone":1,"SI_Address":1,
                                                                "ListAgentFullName":1,
                                                                "ListAgentKey":1,
                                                                "server_id":1,
                                                                "StateOrProvince":1,

                                                                "PostalCode" :1,
                                                                "CountyOrParish":1,

                                                                "ListAgentOfficePhone" : 1,

                                                                "ListAgentEmail" : 1,

                                                                "CoListAgentFullName" :1,

                                                                "CoListAgentEmail" : 1,


                                                                "BuyerAgentFullName" : 1,

                                                                "BuyerAgentCellPhone" :1,
                                                                "CoBuyerAgentFullName" : 1,

                                                                "CoBuyerAgentOfficePhone" : 1
                                                                }
                                                                ))
            n_trans = len(Data_notrans)
            if n_trans>5:
                agent={"AgentName":agents[i],"Transactions":Data_notrans,"number of Transactions":n_trans,"key":listkey}
            #print Data[i]['NOT']

                print len(agent)          
                db_client.MLSLite.list_agent_all_mlslite.insert(agent)
                print 'pass'
            else:
                continue

            #db_client.RFM.Agents.insert()

        except:
                print 'error data'
#print 'pass'
