# Importing the libraries
import streamlit as st
import pandas as pd
import pickle


# Heading
st.header("Car Price Prediction App")

# Using the pandas to import the dataset
df = pd.read_csv("car_price.csv")

# st.dataframe can be used to print the dataset
# st.dataframe(df)


# inputs from the user

year = st.number_input("Insert a number")
fuel_type = st.selectbox("Enter the fuel type",("Diesel","Petrol","CNG","LPG","Electric"))
transmission = st.selectbox("Enter the transmission type",("Manual","Automatic"))
engine = st.slider("Engine CC",500,5000,100)


encode_dict = {
    "fuel_type" :{"Diesel":1,"Petrol" : 2,"CNG" : 3, "LPG" : 4, "Electric" : 5},
    "seller_type" : {"Dealer":1, "Individual" : 2, "Trustmark Dealer":3},
    "transmission_type" : {"Manual" : 1, "Automatic" : 2}
}

# Loading the final trained ML model which was saved in the format of car_pred.pkl --> Pickle file
def model_pred():
    with open("car_pred","rb") as file:
        model = pickle.load(file)

        input_features = [2014,"seller_type",130000,"Petrol","Manual",19.7,796,46.3,5]
        return model.predict()

