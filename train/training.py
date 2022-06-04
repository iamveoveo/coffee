import pandas as pd
from sklearn.cluster import KMeans
import pickle

PATH_DATA_SET = '/home/veo/veo/coffee'
NUM_OF_FEATURE = 11
PARAM = {
            "n_clusters" : 3,
            "init" : 'k-means++',
            "n_init" : 10,
            "max_iter" : 300
        }

#
# Training model function
# @param: none
# @return: model have been trained
#
def training():
    try:
        param = PARAM
        customize_check = input('\nY: Customize parameters\nN: Default parameters')

        if(customize_check == 'Y'):
            param = inputCustomizeParameter()
            print(param)

        data = pd.read_csv(PATH_DATA_SET+'/coffee-quality-data/data/arabica_data_extracted.csv', index_col = 0)

        print('Training the model, please wait a moment')
        
        model = KMeans(n_clusters = param['n_clusters'], init = param['init'], n_init = param['n_init'], nmax_iter = param['max_iter'])
        model.fit(data)

        pickle.dump(model, open("model.pkl", "wb"))
        print('The model has been trained')
        return model
    except:
        print("An error occurred during training")
        return False
    

#
# inputting customize parameter function
# @param: none
# @return: dict of parameter
#
def inputCustomizeParameter():
    try:
        cus_param = {}
        input_init_ = []

        input_ = int(input('\nn_clusters(The number of clusters to form as well as the number of centroids to generate.)\nn_cluster = '))
        cus_param['n_clusters'] = input_ if input_ != '' else PARAM['n_clusters']

        clus_cus = input('\ninitial cluster centroid yourself? (Y/n)')
        input_ = ''
        if(clus_cus=='Y'):
            i = 0
            while (i < cus_param['n_clusters']):
                input_ = []
                input_ = list(map(int,input().split())) 
                if (len(input_) != 11):
                    print('Invalid cluster center, please re-enter')
                    continue
                input_init_.append(input_)
                i += 1
        cus_param['init'] = input_init_ if input_init_ != '' else PARAM['init']

        input_ = int(input('\nn_init(Number of time the k-means algorithm will be run with different centroid seeds.\n The final results will be the best output of n_init consecutive runs in terms of inertia.)\nn_init = '))
        cus_param['n_init'] = input_ if input_ != '' else PARAM['n_init']

        input_ = int(input('\nmax_iter(Maximum number of iterations of the k-means algorithm for a single run.)\nmax_iter = '))
        cus_param['max_iter'] = input_ if input_ != '' else PARAM['max_iter']

        return( cus_param)
    except:
        print("An error occurred during inputting")
        return False
