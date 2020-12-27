import numpy as np
import pandas as pd
import math
import sklearn
import sklearn.metrics as metrics
import matplotlib.pyplot as plt


def applyClusterMetrics(X, y_pred):

    applyDaviesBouldinScore(X, y_pred)
    applyCalinskiScore(X, y_pred)
    applySilhouetteScore(X, y_pred)


def applyDaviesBouldinScore(X, y_pred):
    """
            The minimum score is zero, with lower values indicating better clustering.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html
    """
    score_db = metrics.davies_bouldin_score(X, y_pred)
    print("Davies Bouldin")
    print(score_db)
    print()


def applyCalinskiScore(X, y_pred):
    """
            The score is defined as ratio between the within-cluster dispersion and the between-cluster dispersion.
            The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html

    """
    score_ch = metrics.calinski_harabasz_score(X, y_pred)
    print("Calinski and Harabaz")
    print(score_ch)
    print()


def applySilhouetteScore(X, y_pred):
    """
            The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
    """
    score_s = metrics.silhouette_score(X, y_pred)
    print("Silhouette Score")
    print(score_s)
    print()


def applyRegressionMetrics(y, y_pred):
    error = math.sqrt(((y_pred-y)**2).mean())
    mape = (np.abs(y_pred-y) / y).mean()
    mdape = (np.abs(y_pred-y) / y).median()
    res_metrics = {
        'y': y,
        'y_pred': y_pred,
        'RMSE':  error,
        'MAPE': mape,
        'MDAPE': mdape,
        'MSE':  metrics.mean_squared_error(y, y_pred),
        'MAE':  metrics.mean_absolute_error(y, y_pred),
        'R2':  metrics.r2_score(y, y_pred),
    }

    return res_metrics


def evaluateRegression(y, y_pred):
    error = math.sqrt(((y_pred-y)**2).mean())
    mape = (np.abs(y_pred-y) / y).mean()
    mdape = (np.abs(y_pred-y) / y).median()
    print("RMSE : %.4f" % error)
    print("MAPE': %.4f" % mape)
    print("MDAPE': %.4f" % mdape)
    print("MSE: %.4f" % metrics.mean_squared_error(y, y_pred))
    print("MAE: %.4f" % metrics.mean_absolute_error(y, y_pred))
    print('R2: %.4f' % metrics.r2_score(y, y_pred))

    plt.plot([y.min(), y.max()], [y_pred.min(), y_pred.max()], 'k--', lw=3)
    plt.scatter(y, y_pred)
    plt.ylabel('Predicted')
    plt.xlabel('Real')
    plt.show()

    plt.hist(y, bins=100, color='blue', linewidth=3)
    plt.xlabel('Real')
    plt.show()
    plt.hist(y_pred, bins=100, color='red', linewidth=3)
    plt.xlabel('Predicted')
    plt.show()
