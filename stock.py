import yfinance as yf
import streamlit as st
import datetime

# Heading
st.header("Stock Analysis App")


# Taking the stock name as text input from user and also start and end dates as input
stock = st.text_input('Enter the Stock Abreviation here', 'MSFT')
st.write(f"Currently Analysis {stock}")

# Creating the two columns to take the start and end dates from user input
col1, col2= st.columns(2)

with col1:
    start_date= st.date_input("Enter the Start date",datetime.date(2019,1,1))

with col2:
    end_date = st.date_input("Enter the end date",datetime.date(2022,12,31))

# yfinance brings/scrapes the realtime stock market values from internet. MSFT is Microsoft shortcut stock market code
data = yf.Ticker(stock)

# get historical market data of period of one day from 2019 jan to 2022 December end or from user defined dates.
hist = data.history(period="1d", start = start_date, end = end_date)




# just to write the Microsoft historical data in web site
st.write(hist)

st.subheader("Trend in closing prices")
st.line_chart(hist['Close'])

st.subheader("Trend in Volumes")
st.bar_chart(hist['Volume'])
