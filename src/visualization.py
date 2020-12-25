import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from glob import glob
import matplotlib.cm as cm
from MulticoreTSNE import MulticoreTSNE as TSNE


def create_tsne_labels(X, smp_sz = 7000):    
    tsne_bow = TSNE(n_jobs=-1, n_components=2, perplexity=500, verbose=True)
    tsne_bow_result = tsne_bow.fit_transform(X[:smp_sz])
    return tsne_bow_result
