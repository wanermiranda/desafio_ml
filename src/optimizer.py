import sys
sys.path.append('../')
from src import visualization as v
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from matplotlib import pyplot as plt

def elbow_kmeans(X, min_k=2, max_k=100, eps = 1e-2, step=3):
    error = 0
    Ks = []
    Js = []    
    it = 1
    J = 0.
    k = min_k
    last_j = 999999999.
    print("###############################")
    while ((error > eps) or (it == 1)):        
        print("Number of Clusters:",k)
        print("Starting K-means++")
        cluster = KMeans(n_clusters=k,random_state=42)
        cluster_result = cluster.fit(X)
        print("Finished")
        error = J
        J = cluster_result.inertia_ / X.shape[0]        
        print("J =",J)        
        error = abs(error-J)  
        Ks.append(k)
        print("error =",error)
        Js.append(J)        
        print("###############################")
        k += step
        it += 1                    
        if J > last_j: 
            print('Found optimal')
            break        
        last_j = J        
        if (k > max_k): break
        

    best_K = k-step
    print("\nBest k:",best_K)
    print("Number of iterations:",it)
    print("Error threshold ", (error > eps))
    return best_K, Ks, Js

def linkage_cluster_dendogram(X, opt_method='ward'): 
    X_linked = linkage(X, opt_method, )
    plt.figure(figsize=(10,5))
    dendrogram(X_linked,                
                truncate_mode='lastp',
                distance_sort='descending')
    plt.show()


    return X_linked

def fcluster_cut(X, max_d, opt_method='ward'): 
    X_linked = linkage(X, opt_method)
    clusters = fcluster(X_linked, max_d, criterion='distance')
    return clusters    