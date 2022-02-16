import sys
sys.path.insert(0, "/home/apprenant/Documents/Projets/Projet_E2_P1/")
import pytest
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from src.optimized_model.apps.main_Rachid import user_input_features, predict_price

def test_user_input_features():
    data = {'Age': int(),
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
    dataframe_simulation = pd.DataFrame(data, index=[0])
    function_test = user_input_features()
    assert type(function_test) == type(dataframe_simulation)
    assert type(function_test.columns) == type(dataframe_simulation.columns)
    assert len(function_test.columns) == len(dataframe_simulation.columns)


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

    filename = 'src/optimized_model/finalized_model_Rachid.sav'

    function_test = predict_price(dataframe_simulation, filename)

    assert isinstance(function_test, np.ndarray)
    assert isinstance(function_test[0], float)
    assert function_test[0] > 0
    assert function_test[0] < 700000