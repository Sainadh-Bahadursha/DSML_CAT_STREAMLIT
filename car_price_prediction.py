# Importing the libraries
import streamlit as st
import pandas as pd
import pickle
import datetime


# Heading
st.header("Car Price Prediction App")


# Using the pandas to import the dataset
df = pd.read_csv("car_price.csv")


# st.dataframe can be used to print the dataset
# st.dataframe(df)

# inputs from the user
col1, col2 = st.columns(2) # to create two columns
with col1:
    year_inp = st.number_input("Enter the Year", min_value=1900,max_value=2024)
with col2:
    seats_inp = st.selectbox("Enter number of seats",[4,5,7,9,11])


col1, col2 = st.columns(2)
with col1:
    fuel_type_inp = st.selectbox("Enter the fuel type",("Diesel","Petrol","CNG","LPG","Electric"))
with col2:
    transmission_inp = st.selectbox("Enter the transmission type",("Manual","Automatic"))


col1, col2 = st.columns(2)
with col1:
    engine = st.slider("Engine CC",min_value=500,max_value=5000,step=100)
with col2:
    seller_inp = st.selectbox("Enter the seller type",["Dealer","Individual","Trustmark Dealer"])

# Create encode dictionary to convert input strings to respective encodings as present in model
encode_dict = {
    "fuel_type" :{"Diesel":1,"Petrol" : 2,"CNG" : 3, "LPG" : 4, "Electric" : 5},
    "seller_type" : {"Dealer":1, "Individual" : 2, "Trustmark Dealer":3},
    "transmission_type" : {"Manual" : 1, "Automatic" : 2}
}

# Loading the final trained ML model which was saved in the format of car_pred.pkl --> Pickle file
def model_pred(year_inp,seller_encoded,fuel_type_encoded,transmission_encoded,engine,seats_inp):
    with open("car_pred","rb") as file:
        model = pickle.load(file) # Pickle is used to save and load the already created model

        input_features = [[year_inp,seller_encoded,130000,fuel_type_encoded,transmission_encoded,19.7,engine,46.3,seats_inp]]
        return model.predict(input_features) # Return the prediction for given input features
    


if st.button("Predict"): # Button is created for the sake predicting only when pressed on button
    fuel_type_encoded = encode_dict["fuel_type"][fuel_type_inp]
    transmission_encoded = encode_dict["transmission_type"][transmission_inp]
    seller_encoded = encode_dict["seller_type"][seller_inp]
    second_hand_price = model_pred(year_inp,seller_encoded,fuel_type_encoded,transmission_encoded,engine,seats_inp)
    st.write("Predicted Price is ", str(second_hand_price))
