'''
Created on Jan 23, 2017

@author: sysadmin
'''
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from pymongo import MongoClient
from dbauth import DATABASE_ACCESS

import matplotlib.pyplot as pyl
db_client=MongoClient("mongo-master.propmix.io", 33017)
db_client.MLSLite.authenticate(**DATABASE_ACCESS)
data=list(db_client.MLSLite.miami1L.find({'ClosePrice':{'$ne':'NULL'}},{"ClosePrice":1,"LivingArea":1,'_id':0}).limit(10))
filtered_data=pd.DataFrame(data)
lrmatrix= np.matrix(filtered_data)
X,Y = lrmatrix[:,0],lrmatrix[:,1]
model=LinearRegression().fit(X,Y)
m=model.coef_[0]
b=model.intercept_
print m,b

