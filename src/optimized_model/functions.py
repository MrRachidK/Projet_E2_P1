import pickle
import pandas as pd

# Load model
def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb')) 
    return loaded_model

# Apply Model to Make Prediction
def predict_price(model, data):
    prediction = model.predict(data)
    return prediction

# Get features for price estimation
def user_input_features(data): 

    features = pd.DataFrame(data, index=[0])
    for column in features.columns:
        if features[column].dtype == 'bool':
            features[column] = features[column].astype('object')

    return features