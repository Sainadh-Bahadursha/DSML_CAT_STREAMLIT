# Importing the libraries
import streamlit as st
import pandas as pd


# Heading
st.header("Car Price Prediction App")

# Using the pandas to import the dataset
df = pd.read_csv("car_price.csv")

# st.dataframe can be used to print the dataset
#st.dataframe(df)

