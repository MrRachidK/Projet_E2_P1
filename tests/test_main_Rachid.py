import sys
sys.path.insert(0, "/home/apprenant/Documents/Projets/Projet_E2_P1/")
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from src.optimized_model.functions import load_model, predict_price, user_input_features
import pickle

def test_user_input_features():
    type_data = {'Age': int(),
            'GrLivArea': int(),
            'LotFrontage': int(),
            'LotArea': int(),
            'GarageArea': float(),
            'Fence': bool(),
            'Pool' : bool(),
            'YrSold': int(),
            'YearBuilt': int(),
            'TotalBsmtSF': int(),
            'FirstFlrSF': int(),
            'SecondFlrSF': int(),
            'FullBath': int(),
            'TotRmsAbvGrd': int(),
            'GarageCars': int()
            }

    fake_data = {'Age': 10,
            'GrLivArea': 100,
            'LotFrontage': 10,
            'LotArea': 50,
            'GarageArea': 5,
            'Fence': True,
            'Pool' : False,
            'YrSold': 2000,
            'YearBuilt': 2000,
            'TotalBsmtSF': 100,
            'FirstFlrSF': 100,
            'SecondFlrSF': 100,
            'FullBath': 1,
            'TotRmsAbvGrd': 1,
            'GarageCars': 1
            }

    type_dataframe_simulation = pd.DataFrame(type_data, index=[0])
    function_test = user_input_features(fake_data)
    assert type(function_test) == type(type_dataframe_simulation)
    assert type(function_test.columns) == type(type_dataframe_simulation.columns)
    assert len(function_test.columns) == len(type_dataframe_simulation.columns)

def test_load_model():
    filename = '/home/apprenant/Documents/Projets/Projet_E2_P1/src/optimized_model/finalized_model_Rachid.sav'
    function_test = load_model(filename)
    assert type(filename) == str
    assert type(function_test) == type(pickle.load(open(filename, 'rb')))
    
def test_predict_price():
    data = {'Age': 10,
            'GrLivArea': 100,
            'LotFrontage': 10,
            'LotArea': 50,
            'GarageArea': 5,
            'Fence': True,
            'Pool' : False,
            'YrSold': 2000,
            'YearBuilt': 2000,
            'TotalBsmtSF': 100,
            'FirstFlrSF': 100,
            'SecondFlrSF': 100,
            'FullBath': 1,
            'TotRmsAbvGrd': 1,
            'GarageCars': 1
            }

    dataframe_simulation = pd.DataFrame(data, index=[0])

    for column in dataframe_simulation.columns:
        if dataframe_simulation[column].dtype == 'bool':
            dataframe_simulation[column] = dataframe_simulation[column].astype('object')

    filename = '/home/apprenant/Documents/Projets/Projet_E2_P1/src/optimized_model/finalized_model_Rachid.sav'
    model = pickle.load(open(filename, 'rb'))

    function_test = predict_price(model, dataframe_simulation)

    assert isinstance(function_test, np.ndarray)
    assert isinstance(function_test[0], float)
    assert function_test[0] > 0
    assert function_test[0] < 700000