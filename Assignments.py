import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("car_price.csv")
st.dataframe(df)

# st.bar_chart(data=df, x= ‘fuel_type’, y= ‘mileage’)
st.bar_chart( data = df, x = 'fuel_type', y='mileage')