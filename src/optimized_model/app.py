import sys
sys.path.insert(0,"/home/apprenant/Documents/Projets/Projet_E2_P1/")
import streamlit as st
from multiapp import MultiApp 
from apps import home, first_estimation, second_estimation

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("First estimation", first_estimation.app)
app.add_app("Second estimation", second_estimation.app)

if "page" in st.session_state:
        st.session_state.update(st.session_state)
else:
    st.session_state.update({
        # Default page
        "page": "Home",

        # Default widget values
        "first_estimation" : "", 
        "Age":0,
        'LotArea':0,
        'GrLivArea':0,
        'LotFrontage':0,
        'GarageArea':0,
        'Fence':False,
        'Pool':False,
        'YrSold':0,
        'YearBuilt':0,
        'TotalBsmtSF':0,
        'FirstFlrSF':0,
        'SecondFlrSF':0,
        'FullBath':0,
        'TotRmsAbvGrd':0,
        'GarageCars':0
    })

app.run()