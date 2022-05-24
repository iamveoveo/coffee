import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import pickle

data = pd.read_csv('..\\coffee-quality-database\\data\\arabica_data_extracted.csv', index_col = 0)

model = KMeans(n_clusters=3, n_init=15, random_state=0)
print(data)
model.fit(data)

''' pickle.dump(model, open("model.pkl", "wb")) '''

print(model.labels_)
print(model.cluster_centers_)