'''
Created on Apr 25, 2017

@author: sysadmin
'''
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as sklearnpca
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import *
from matplotlib.cm import register_cmap
from scipy import stats
import seaborn
movies=pd.read_csv('D:\WorkSpace\moviedata\orientlens-master\movielens\movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings.drop(['timestamp'], axis=1, inplace=True)
def replace_name(x):
    return movies[movies['movieId']==x].title.values[0]

ratings.movieId = ratings.movieId.map(replace_name)

M = ratings.pivot_table(index=['userId'], columns=['movieId'], values='rating')
m = M.shape

df1 = M.replace(np.nan, 0, regex=True)
X_std = StandardScaler().fit_transform(df1)
# mean_vec = np.mean(X_std, axis=0)
# cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
# print('Covariance matrix \n%s' %cov_mat)
#print('NumPy covariance matrix: \n%s' %np.cov(X_std.T))
#Perform eigendecomposition on covariance matrix
#cov_mat = np.cov(X_std.T)
#eig_vals, eig_vecs = np.linalg.eig(cov_mat)
#print('Eigenvectors \n%s' %eig_vecs)
#print('\nEigenvalues \n%s' %eig_vals)
# Visually confirm that the list is correctly sorted by decreasing eigenvalues
#eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
# print('Eigenvalues in descending order:')
# for i in eig_pairs:
#     print(i[0])
pca = sklearnpca(n_components=2)
pca.fit_transform(df1)
#print pca.explained_variance_ratio_ 
pca = sklearnpca().fit(X_std)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.show()