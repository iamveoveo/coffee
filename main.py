import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import pickle

pickled_model = pickle.load(open('train\\model.pkl', 'rb'))

a = []
input_ = 0
while (len(a)<11):
    input_ = input('nhap vao cac he so mong muon')
    a.append(input_)
    print(a)

pickled_model.predict([a])