# K Means Clustering

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing data set
dataset = pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,3:5].values  # this can be done instead of [:,[3,4]]

# using the elbow method to find the optimal no. of clusters by plotting graph
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans= KMeans(n_clusters=i , init ='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)        # n_init=no of times kmeans algo. will run with diff inital centroids it's default value is 10
    wcss.append(kmeans.inertia_ )

plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')  
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.show()  # from this graph we get no of clusters=5

#Applying K-Means to the dataset
kmeans=KMeans(n_clusters=5 , init ='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans=kmeans.fit_predict(X)  # it tells that which customers belong to which clusters by indicating no of it
                                # clusters no start from 0 to 4

#Visualising the clusters
plt.scatter(X[y_kmeans ==0 , 0],X[y_kmeans==0 ,1] ,s=100, c='red', label='Cluster 1') # label by seeing graph -->standard
  # it means x coordinate of clusters no-0 oh X dataset of column 1,simalrily foy y coordinate
  # s means size of data points
plt.scatter(X[y_kmeans ==1 , 0],X[y_kmeans==1 ,1] ,s=100, c='blue', label='Cluster 2') # label by seeing graph -->careless
plt.scatter(X[y_kmeans ==2 , 0],X[y_kmeans==2 ,1] ,s=100, c='green', label='Cluster 3')  # label by seeing graph -->target
plt.scatter(X[y_kmeans ==3 , 0],X[y_kmeans==3 ,1] ,s=100, c='cyan', label='Cluster 4')    # label by seeing graph --> sensible
plt.scatter(X[y_kmeans ==4 , 0],X[y_kmeans==4 ,1] ,s=100, c='magenta', label='Cluster 5')   # label by seeing graph -->careful

plt.scatter(kmeans.cluster_centers_[:,0] , kmeans.cluster_centers_[:,1] ,s=300, c='yellow', label='Centroid')
plt.title('Clusters of clients')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend()
plt.show()
 

# to clear console ctrl+L
#to clear variable variable explorer select %reset -f 
