import pandas as pd

raw_data = pd.read_csv('/home/veo/veo/coffee/coffee-quality-data/data/arabica_data_cleaned.csv', index_col = 0)

features = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity', 'Clean.Cup', 'Sweetness', 'Cupper.Points', ]
data = pd.DataFrame(raw_data, columns=features)

file_name = '/home/veo/veo/coffee/coffee-quality-data/data/arabica_data_extracted.csv'
data.to_csv(file_name, encoding='utf-8')