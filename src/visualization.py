import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from glob import glob
import matplotlib.cm as cm
from MulticoreTSNE import MulticoreTSNE as TSNE


def visualize_unsup_scatter(data_2d, figsize=(20,20)):
    plt.figure(figsize=figsize)
    plt.grid()
    
    plt.scatter(data_2d[:,0],data_2d[:,1],marker='o',linewidth='1',alpha=0.8)    

    return plt

def visualize_sup_scatter(data_2d, label_ids, figsize=(20,20), color=None):
    #label_to_id_dict = {v:i for i,v in enumerate(np.unique(label_ids))}
    #id_to_label_dict = {v: k for k, v in label_to_id_dict.items()}
    plt.figure(figsize=figsize)
    plt.grid()
    
    nb_classes = len(np.unique(label_ids))
    
    for label_id in np.unique(label_ids):
        if not(color):
            c = plt.cm.tab20(label_id / float(nb_classes))
        else:
            c = color[int(label_id)]

        plt.scatter(data_2d[np.where(label_ids == label_id), 0],
                    data_2d[np.where(label_ids == label_id), 1],
                    marker='o',
                    color= c,
                    linewidth='1',
                    alpha=0.8)
                    #label=id_to_label_dict[label_id])
    return plt

def plot_cluster_errors(Ks, Js, figsize=(20,20)):
	print("J ",Js)
	print("Ks ",Ks)
	plt.figure(figsize=figsize)
	plt.plot(Ks,Js)
	plt.ylabel('Error')
	plt.xlabel('Clusters')
	return plt

def visualize_sup_scatter_hover(data_2d, label_ids, info, figsize=(20,20), color=None):

    #plt.figure(figsize=figsize)
    #plt.grid()

    fig,ax = plt.subplots()    
    
    nb_classes = len(np.unique(label_ids))
    
    
    '''
    for label_id in np.unique(label_ids):
        if not(color):
            c = plt.cm.tab20(label_id / float(nb_classes))
        else:
            c = color[int(label_id)]
    
        sc = plt.scatter(data_2d[np.where(label_ids == label_id), 0],
                    data_2d[np.where(label_ids == label_id), 1],
                    marker='o',
                    color= c,
                    linewidth='1',
                    alpha=1.0)
                    #label=id_to_label_dict[label_id])
    '''

    sc = plt.scatter(data_2d[:, 0],
                    data_2d[:, 1],
                    marker='o',
                    linewidth='1',
                    alpha=1.0)
   
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))

    annot.set_visible(False)

    def update_annot(ind):

        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        #text = "{}, {}".format(" ".join(list(map(str,data_2d[ind["ind"]])))," ".join([info[n] for n in ind["ind"]]))
        text = "{}".format(" ".join([info[n] for n in ind["ind"]]))
        annot.set_text(text)
        #annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    return plt


def create_tsne_labels(X, smp_sz = 7000):    
    tsne_bow = TSNE(n_jobs=-1, n_components=2, perplexity=500, verbose=True)
    tsne_bow_result = tsne_bow.fit_transform(X[:smp_sz])
    return tsne_bow_result
