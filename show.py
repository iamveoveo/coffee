import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from config import CONST

#
# Show the trained model function
# @param: k-means model
# @return: return boolean type
#
def showModel(model):
    try:
        print('\n', model)
        stop = False
        while (not stop):
            option_ = input('\n1: Cluster centers.\n2: Label of each data point.\n3: Sum of squared distances.\n4: Number of iterations run.\n0: Abort\n>>> ')
            if (option_ == '1'):
                print(model.cluster_centers_)
            elif (option_ == '2'):
                print(*model.labels_)
            elif (option_ == '3'):
                print(model.inertia_)
            elif (option_ == '4'):
                print(model.n_iter_)
            else:
                print('\n\tabort\n')
                stop = True
                break
            input()
        return True
    except:
        print('\nSomething went wrong, please return later')
        return False

#
# Draw diagram option function
# @param: label of each data point
# @return: return boolean type
#
def showDiagram(lbls):
    try:
        feature_name = []
        print("\nAroma\t\tFlavor\t\tAftertaste\nAcidity\t\tBody\t\tBalance\nUniformity\tClean.Cup\tSweetness\nCupper.Points\tTotal.Cup.Points")
        feature_name = list(input('\nEnter 2 desired features, separated by space\n').split())
        draw_diagram = drawScatter(feature_name, lbls)
        return True
    except:
        print('\nSomething went wrong, please return later')
        return False

#
# Draw scatter of 2 feature function
# @param_1: array of desired features to draw
# @param_2: label of each data point
# @return: return boolean type
#
def drawScatter(feature_name, labels):
    try:
        data = pd.read_csv(CONST.PATH_DATA_SET+'/coffee-quality-data/data/arabica_data_extracted.csv', index_col = 0)
        
        if (len(feature_name) != 2):
            print('Feature number does not match')
            return False
        else:
            for name in feature_name:
                if (name not in data.keys()):
                    print('Please enter valid feature')
                    return False
            
        x = data[feature_name[0]]
        y = data[feature_name[1]]
        colors = labels

        fig, ax = plt.subplots()

        scatter = ax.scatter(x, y, c=colors)

        legend1 = ax.legend(*scatter.legend_elements(),
                            loc="lower left", title="Classes")
        ax.add_artist(legend1)
        plt.title(feature_name[0] + ' - ' + feature_name[1])
        plt.xlabel(feature_name[0])
        plt.ylabel(feature_name[1])
        plt.show()
        return True
    except:
        print("\nAn error occurred during drawing")
        return False

#
# Show data by option
# @param: none
# @return: return boolean type
#
def showData():
    try:
        pd.set_option('display.max_rows', 1400)
        pd.set_option('display.max_columns', CONST.NUM_OF_FEATURE)
        data = pd.read_csv(CONST.PATH_DATA_SET+'/coffee-quality-data/data/arabica_data_extracted.csv', index_col = 0)

        print(data)
        return True
    except:
        print('\nSomething went wrong, please return later')
        return False
    