import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

raw_data = pd.read_csv('coffee-quality-database\\data\\arabica_data_cleaned.csv', index_col = 0)

features = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity', 'Clean.Cup', 'Sweetness', 'Cupper.Points', 'Total.Cup.Points', 'Moisture', 'Quakers', ]
data = pd.DataFrame(raw_data, columns=features)

file_name = 'coffee-quality-database\\data\\arabica_data_extracted.csv'
data.to_csv(file_name, encoding='utf-8')