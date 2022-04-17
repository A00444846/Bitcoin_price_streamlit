# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:54:03 2022

@author: prati
"""

import pandas as pd
import requests
import streamlit as st

no_of_days = st.slider('No of days', 1, 365, 90)

currency = st.radio(
     "Currency",
     ('CAD', 'USD', 'INR'))

API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency="+ currency +"&days="+str(no_of_days)+"&interval=daily"
req = requests.get(API_URL)
if req.status_code == 200:
    raw_data = req.json()['prices']
    df = pd.DataFrame(data=raw_data, columns=['Date', 'Price'])
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df = df.set_index('Date')
    st.line_chart(df)
    st.text('Average price during this time was '+ str(df['Price'].mean()) + ' '+ currency)
    
    
