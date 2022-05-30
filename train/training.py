import pandas as pd
from sklearn.cluster import KMeans
import pickle

def training(n_clusters = 3, n_init = 30, init='k-means++'):
    w, h = 11, n_clusters;

    #init = [[input() for y in range(h)] for x in range(w)]
    #input init
    data = pd.read_csv('..\\coffee-quality-data\\data\\arabica_data_extracted.csv', index_col = 0)

    model = KMeans(n_clusters = n_clusters, init= init, n_init = n_init, random_state=0)
    print(data)
    model.fit(data)

    pickle.dump(model, open("model.pkl", "wb"))