from sklearn.cluster import KMeans
import pickle
from config import CONST
from training import training
from show import showModel
from show import showDiagram
from show import showData

try:
    model = pickle.load(open('model.pkl', 'rb'))
    end = False

    while (not end):
        option_ = input('\n1: Train model\n2: Show model\n3: Show diagram\n4: Show dataset\n0: Exit\n>>> ')

        if (option_=='1'):
            trained = training()
            if(trained):
                model = trained
        elif (option_=='2'):
            show_model = showModel(model)
        elif (option_=='3'):
            draw_diagram = showDiagram(model.labels_)
        elif (option_=='4'):
            show_data = showData()
        else:
            exit_ = input('\n\tExit? (Y/n)')
            if (exit_ == 'Y'):
                end = True
            continue
        input('\n<<<Press ENTER to continue.>>>')
except:
    print('The application cannot be launched at this time, thanks for visiting')
