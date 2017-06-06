from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
STATE=db_client.MLSLite.mlslite_unique.distinct("StateOrProvince")
print len(STATE)
for st in STATE:
    print st
    if st==None:
        continue
    
        
    agentdata=[
                                                   {"$match":{"StateOrProvince":st}},
                                                   {"$group":
                                                    {
                                                     "_id" : {"ListAgentFullName":"$ListAgentFullName"},
                                                     "Transactions":{"$push":{"ClosePrice":"$ClosePrice"
                                                                    
                                                                    
                                                                     }}
                                                    },
                                                     
                                                     
                                                    "count": { "$sum": 1 }
                                                       
                                                      
                                                      
                                                     }
                                                    
                                                   ]
    agentsunique=list(db_client.MLSLite.mlslite_unique.aggregate(agentdata))
       # n_trans = len(agentsunique)
    #print 'pass'       
    db_client.RFM_mlslite.stat_agen.save(agentsunique)
    print 'pass'

         
                    #db_client.RFM.Agents.insert()
         
         
     

        