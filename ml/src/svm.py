'''
Created on Mar 31, 2017

@author: sysadmin
'''
import numpy as np
from sklearn import tree

from sklearn import svm,datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
#import matplotlib.pyplot.cm.Paired

X = iris.data[:, :2] # we only take the first two features. We could
 # avoid this ugly slicing by using a two-dim dataset
print iris,X
y = iris.target
svc = svm.SVC(kernel='linear', C=1,gamma=0).fit(X, y) 
print svc
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z,alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show() 