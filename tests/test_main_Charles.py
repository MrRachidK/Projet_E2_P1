import sys
sys.path.insert(0,"/home/apprenant/Documents/Projets/Projet_E2_P1/")
import pytest
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from src.initial_model.main_Charles import user_input_features, predict_price

def test_user_input_features():
    data = {'Age': int(),
            'GrLivArea': int(),
            'LotFrontage': int(),
            'LotArea': int(),
            'GarageArea': float(),
            'Fence': bool(),
            'Pool' : bool(),
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
            }

    dataframe_simulation = pd.DataFrame(data, index=[0])

    for column in dataframe_simulation.columns:
        if dataframe_simulation[column].dtype == 'bool':
            dataframe_simulation[column] = dataframe_simulation[column].astype('object')

    filename = 'src/initial_model/finalized_model_Charles.sav'

    function_test = predict_price(dataframe_simulation, filename)

    assert isinstance(function_test, np.ndarray)
    assert isinstance(function_test[0], float)
    assert function_test[0] > 0
    assert function_test[0] < 700000