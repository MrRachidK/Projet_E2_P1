import sys
sys.path.insert(0,"/home/apprenant/Documents/Projets/Projet_E2_P1/")
import streamlit as st
import pandas as pd
from src.optimized_model.functions import load_model, predict_price, user_input_features

def app():

    model = load_model('/home/apprenant/Documents/Projets/Projet_E2_P1/src/optimized_model/finalized_model_Rachid.sav')
    X = pd.read_csv("/home/apprenant/Documents/Projets/Projet_E2_P1/data/clean_X_Rachid.csv")

    # Sidebar
    # Header of Specify Input Parameters
    st.sidebar.header("Quels sont vos critères ?")

    Age_2 = st.sidebar.slider('Ancienneté du bien', int(X.Age.min()), int(X.Age.max()), int(X.Age.mean()))
    LotArea_2 = st.sidebar.slider('Surface totale', int(X.LotArea.min()), int(X.LotArea.max()), int(X.LotArea.mean()))
    GrLivArea_2 = st.sidebar.slider('Surface au sol', int(X.GrLivArea.min()), int(X.GrLivArea.max()), int(X.GrLivArea.mean()))
    GarageArea_2 = st.sidebar.slider('Taille du garage', int(X.GarageArea.min()), int(X.GarageArea.max()), int(X.GarageArea.mean()))
    Fence_2 = st.sidebar.select_slider('Présence de barrières', options=[False, True])
    TotalBsmtSF_2 = st.sidebar.slider('Surface totale du sous-sol', int(X.TotalBsmtSF.min()), int(X.TotalBsmtSF.max()), int(X.TotalBsmtSF.mean()))
    FirstFlrSF_2 = st.sidebar.slider('Surface du 1er étage', int(X.FirstFlrSF.min()), int(X.FirstFlrSF.max()), int(X.FirstFlrSF.mean()))

    validation_button_1 = st.sidebar.button("Validez vos choix")

    if validation_button_1:
        data_2 = {'Age': Age_2,
            'GrLivArea': GrLivArea_2,
            'LotArea': LotArea_2,
            'GarageArea': GarageArea_2,
            'Fence': Fence_2,
            'TotalBsmtSF': TotalBsmtSF_2,
            'FirstFlrSF': FirstFlrSF_2
            }
        features_2 = user_input_features(data_2)
        st.header('Récapitulatif de vos choix')
        st.write(features_2)
        st.write('---')

        prediction_2 = predict_price(model, features_2)
        formated_prediction_2 = '${:,}'.format(int(prediction_2))

        st.header('Prédiction du prix de vente')
        st.write(formated_prediction_2)
        st.write('---')
        st.header('Comparaisons avec la première estimation')
        if formated_prediction_2 > st.session_state.first_estimation:
            st.write('Le prix de vente est supérieur à la première estimation')
        elif formated_prediction_2 == st.session_state.first_estimation:
            st.write('Le prix de vente est égal à la première estimation')
        else:
            st.write('Le prix de vente est inférieur à la première estimation')
        st.write("La précédente prédiction était de {}".format(st.session_state.first_estimation))
        st.write('Vous avez modifié les valeurs suivantes :')
        for key, value in data_2.items():
            if value != st.session_state[key]:
                st.write("- {}".format(key))