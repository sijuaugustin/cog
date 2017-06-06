'''
Created on Nov 8, 2016

@author: sysadmin
'''
from pymongo import MongoClient
db_client = MongoClient(host='52.91.122.15', port=27017)
for row in  list(db_client.MLSLite.listing_unique.find({},{"ListAgentFullName":1,"_id":0})):
    db_client.RFM.MLSLITE_AGENTS.insert(row)
    print 'pass' 