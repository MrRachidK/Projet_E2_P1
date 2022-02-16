import sys
sys.path.insert(0,"/home/apprenant/Documents/Projets/Projet_E2_P1/")
import streamlit as st
import pickle
import pandas as pd

# Functions
def app():
    # Load Model
    def load_model(filename):
        loaded_model = pickle.load(open(filename, 'rb')) 
        return loaded_model

    # Apply Model to Make Prediction
    def predict_price(model, data):
        prediction = model.predict(data)
        return prediction

    model = load_model('/home/apprenant/Documents/Projets/Projet_E2_P1/src/optimized_model/finalized_model_Rachid.sav')
    X = pd.read_csv("/home/apprenant/Documents/Projets/Projet_E2_P1/data/clean_X_Rachid.csv")

    # States

    st.write(st.session_state)

    # Sidebar
    # Header of Specify Input Parameters
    st.sidebar.header("Quels sont vos critères ?")

    Age = st.sidebar.slider('Ancienneté du bien', int(X.Age.min()), int(X.Age.max()), int(X.Age.mean()))
    LotArea = st.sidebar.slider('Surface totale', int(X.LotArea.min()), int(X.LotArea.max()), int(X.LotArea.mean()))
    GrLivArea = st.sidebar.slider('Surface au sol', int(X.GrLivArea.min()), int(X.GrLivArea.max()), int(X.GrLivArea.mean()))
    LotFrontage = st.sidebar.slider('Taille de la façade', int(X.LotFrontage.min()), int(X.LotFrontage.max()), int(X.LotFrontage.mean()))
    GarageArea = st.sidebar.slider('Taille du garage', int(X.GarageArea.min()), int(X.GarageArea.max()), int(X.GarageArea.mean()))
    Fence = st.sidebar.select_slider('Présence de barrières', options=[False, True])
    Pool = st.sidebar.select_slider('Piscine souhaitée ?', options=[False, True])
    YrSold = st.sidebar.slider('Année de vente', int(X.YrSold.min()), int(X.YrSold.max()), int(X.YrSold.mean()))
    YearBuilt = st.sidebar.slider('Année de construction', int(X.YearBuilt.min()), int(X.YearBuilt.max()), int(X.YearBuilt.mean()))
    TotalBsmtSF = st.sidebar.slider('Surface totale du sous-sol', int(X.TotalBsmtSF.min()), int(X.TotalBsmtSF.max()), int(X.TotalBsmtSF.mean()))
    FirstFlrSF = st.sidebar.slider('Surface du 1er étage', int(X.FirstFlrSF.min()), int(X.FirstFlrSF.max()), int(X.FirstFlrSF.mean()))
    SecondFlrSF = st.sidebar.slider('Surface du 2ème étage', int(X.SecondFlrSF.min()), int(X.SecondFlrSF.max()), int(X.SecondFlrSF.mean()))
    FullBath = st.sidebar.slider('Nombre de salles de bain', int(X.FullBath.min()), int(X.FullBath.max()), int(X.FullBath.mean()))
    TotRmsAbvGrd = st.sidebar.slider('Nombre de pièces au dessus du sol', int(X.TotRmsAbvGrd.min()), int(X.TotRmsAbvGrd.max()), int(X.TotRmsAbvGrd.mean()))
    GarageCars = st.sidebar.slider('Nombre de voitures dans le garage', int(X.GarageCars.min()), int(X.GarageCars.max()), int(X.GarageCars.mean()))

    validation_button_1 = st.sidebar.button("Validez vos choix")

    if validation_button_1:
        data = {'Age': Age,
                'GrLivArea': GrLivArea,
                'LotFrontage': LotFrontage,
                'LotArea': LotArea,
                'GarageArea': GarageArea,
                'Fence': Fence,
                'Pool' : Pool,
                'YrSold': YrSold,
                'YearBuilt': YearBuilt,
                'TotalBsmtSF': TotalBsmtSF,
                'FirstFlrSF': FirstFlrSF,
                'SecondFlrSF': SecondFlrSF,
                'FullBath': FullBath,
                'TotRmsAbvGrd': TotRmsAbvGrd,
                'GarageCars': GarageCars
                }
                
        for key, value in data.items():
            st.session_state[key] = value        
        features = pd.DataFrame(data, index=[0])
        for column in features.columns:
            if features[column].dtype == 'bool':
                features[column] = features[column].astype('object')
        st.header('Récapitulatif de vos choix')
        st.write(features)
        st.write('---')
        
        prediction_1 = predict_price(model, features)
        formated_prediction_1 = '${:,}'.format(int(prediction_1))
        st.session_state.first_estimation = formated_prediction_1

        st.header('Prédiction du prix de vente')
        st.write(st.session_state.first_estimation)
        st.write('---')
    



