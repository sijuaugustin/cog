
'''
Created on Apr 26, 2017

@author: sysadmin
'''
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from pymongo import MongoClient
from dbauth import DATABASE_ACCESS
from sklearn.ensemble import RandomForestClassifier
db_client=MongoClient("mongo-master.propmix.io", 33017)
db_client.MLSLite.authenticate(**DATABASE_ACCESS)
data=list(db_client.MLSLite.miami1L.find({'ClosePrice':{'$ne':'NULL'},'LivingArea':{'$ne':'NULL'},'ListPrice':{'$ne':'NULL'},'SI_DaysOnMarket':{'$ne':'NULL'}},{"ClosePrice":1,"LivingArea":1,"ListPrice":1,"SI_DaysOnMarket":1,'_id':0}).limit(10))
filtered_data=pd.DataFrame(data)
#data = pd.read_csv('Big_Mart_PCA.csv')
#print filtered_data
#data = filtered_data.replace(np.nan, 0, regex=True)
# print data
# X=data.values
# X = scale(X)
pca = PCA(n_components=3)
train_features = pca.fit_transform(filtered_data)
#pca.fit(filtered_data)
var= pca.explained_variance_ratio_
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
#print var1
#plt.plot(var)

rfr = RandomForestClassifier(n_estimators = 100, n_jobs = 1,oob_score=True)

rfr.fit(train_features)
test_features=list(db_client.MLSLite.miami1L.find({'ClosePrice':{'$ne':'NULL'},'LivingArea':{'$ne':'NULL'},'ListPrice':{'$ne':'NULL'},'SI_DaysOnMarket':{'$ne':'NULL'}},{"ClosePrice":1,"LivingArea":1,"ListPrice":1,"SI_DaysOnMarket":1,'_id':0}).limit(10))

test_features = pca.transform(test_features)
rfr.predict(test_features)
print 'pass'
# pca = PCA(n_components=30)
# pca.fit(X)
# X1=pca.fit_transform(X)
# print X1