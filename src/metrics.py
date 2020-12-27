import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score, silhouette_score

def applyAllMetrics(X,y_pred):

	applyDaviesBouldinScore(X,y_pred)
	applyCalinskiScore(X,y_pred)
	applySilhouetteScore(X,y_pred)

def applyDaviesBouldinScore(X,y_pred):
	"""
		The minimum score is zero, with lower values indicating better clustering.
		https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html
	"""
	score_db = davies_bouldin_score(X,y_pred)
	print("Davies Bouldin")
	print(score_db)
	print()

def applyCalinskiScore(X,y_pred):
	"""
		The score is defined as ratio between the within-cluster dispersion and the between-cluster dispersion.
		The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
		https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html

	"""
	score_ch = calinski_harabasz_score(X,y_pred)
	print("Calinski and Harabaz")
	print(score_ch)
	print()

def applySilhouetteScore(X,y_pred):
	"""
		The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
		https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
	"""
	score_s = silhouette_score(X,y_pred)
	print("Silhouette Score")
	print(score_s)
	print()