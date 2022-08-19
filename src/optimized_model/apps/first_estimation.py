import sys
sys.path.insert(0,"/home/marmouset/Documents/Projet_E2_P1/")
import streamlit as st
import pandas as pd
from src.optimized_model.functions import load_model, predict_price, user_input_features

def app():
    # Load Model
    model = load_model('/home/marmouset/Documents/Projet_E2_P1/src/optimized_model/finalized_model_Rachid.sav')
    X = pd.read_csv("/home/marmouset/Documents/Projet_E2_P1/data/clean_X_Rachid.csv")

    # Sidebar
    # Header of Specify Input Parameters
    st.sidebar.header("Quels sont vos critères ?")

    Age = st.sidebar.slider('Ancienneté du bien', int(X.Age.min()), int(X.Age.max()), int(X.Age.mean()))
    LotArea = st.sidebar.slider('Surface totale', int(X.LotArea.min()), int(X.LotArea.max()), int(X.LotArea.mean()))
    GrLivArea = st.sidebar.slider('Surface au sol', int(X.GrLivArea.min()), int(X.GrLivArea.max()), int(X.GrLivArea.mean()))
    GarageArea = st.sidebar.slider('Taille du garage', int(X.GarageArea.min()), int(X.GarageArea.max()), int(X.GarageArea.mean()))
    Fence = st.sidebar.select_slider('Présence de barrières', options=[False, True])
    TotalBsmtSF = st.sidebar.slider('Surface totale du sous-sol', int(X.TotalBsmtSF.min()), int(X.TotalBsmtSF.max()), int(X.TotalBsmtSF.mean()))
    FirstFlrSF = st.sidebar.slider('Surface du 1er étage', int(X.FirstFlrSF.min()), int(X.FirstFlrSF.max()), int(X.FirstFlrSF.mean()))

    validation_button_1 = st.sidebar.button("Validez vos choix")

    if validation_button_1:
        data = {'Age': Age,
                'GrLivArea': GrLivArea,
                'LotArea': LotArea,
                'GarageArea': GarageArea,
                'Fence': Fence,
                'TotalBsmtSF': TotalBsmtSF,
                'FirstFlrSF': FirstFlrSF
                }
        for key, value in data.items():
            st.session_state[key] = value

        features = user_input_features(data)

        st.header('Récapitulatif de vos choix')
        st.write(features)
        st.write('---')
        
        prediction_1 = predict_price(model, features)
        formated_prediction_1 = '${:,}'.format(int(prediction_1))
        st.session_state.first_estimation = formated_prediction_1

        st.header('Prédiction du prix de vente')
        st.write(st.session_state.first_estimation)
        st.write('---')
    



