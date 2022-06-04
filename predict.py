import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import pickle
import sys 
import os
sys.path.append(os.path.abspath("/home/veo/veo/coffee/train"))
from training import training

model = pickle.load(open('model.pkl', 'rb'))

input_ = input('1: Train model\n2: Show cluster centers\n3: Show diagram\n')

if(input_=='1'):
    trained = training()
    if(trained):
        model = trained
elif(input_==2):
    a = 0

