import sys
sys.path.insert(0,"/home/apprenant/Documents/Projets/Projet_E2_P1/")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

st.write("""
# Prédiction du prix de vente des biens immobiliers à Ames (Iowa USA)
""")
st.write('---')


X = pd.read_csv("data/clean_X_Rachid.csv")
print(X)


# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Quels sont vos critères?')


def user_input_features():
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
            "FirstFlrSF": FirstFlrSF,
            "SecondFlrSF": SecondFlrSF,
            "FullBath": FullBath,
            "TotRmsAbvGrd": TotRmsAbvGrd,
            "GarageCars": GarageCars
            }
    features = pd.DataFrame(data, index=[0])
    
    return features

def dump_data(data, pickle_name):
    with open(pickle_name, "wb") as f:
        pickle.dump(data, f)
    f.close()

def load_data(name):
    with open(name, "rb") as f:
        result = pickle.load(f)
    return result

datas = []
df = user_input_features()
for column in df.columns:
    if df[column].dtype == 'bool':
        df[column] = df[column].astype('object')

df = df.keys().tolist()
print(df)
#datas = datas.append(df)

saved_df = dump_data(df, "data/data")
loaded_df = load_data("data/data")

# Main Panel

# Print specified input parameters
st.header('Précisez vos critères')
st.write(df)
st.write('---')


# Apply Model to Make Prediction
def predict_price(data, filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    prediction = loaded_model.predict(data)
    return prediction

predictions = []
prediction = predict_price(df, 'src/optimized_model/finalized_model_Rachid.sav')
formated_prediction = '${:,}'.format(int(prediction))
saved_prediction = dump_data(formated_prediction, "data/prediction")
loaded_prediction = load_data("data/prediction")

st.header('Prediction du prix de vente')
st.write(loaded_prediction)
st.write('---')
