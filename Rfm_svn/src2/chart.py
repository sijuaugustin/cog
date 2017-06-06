'''
Created on Nov 24, 2016

@author: sysadmin
'''
from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
agentdata=[
                                               {"$match":
                                                    {   'Agentdata.Transactions.City':'Safford'
                                                        
                                                                 
                                                }},
                                               {"$group":
                                                {
                                                 "_id" : {'ListAgentFullName':'$ListAgentFullName'},
                                                 
                                                 "sum": { "$ListPrice": 1 }
                                                   
                                                  
                                                  
                                                 }
                                                }
                                               ]
agentsunique=list(db_client.RFM_mlslite.Agents_fips_wise_.aggregate(agentdata))
print agentsunique
