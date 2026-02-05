import streamlit as st
import joblib
import numpy as np

model = joblib.load("volatility_model.pkl")

st.title("📈 Cryptocurrency Volatility Prediction")

open_p = st.number_input("Open Price", value=100.0)
high_p = st.number_input("High Price", value=110.0)
low_p = st.number_input("Low Price", value=90.0)
close_p = st.number_input("Close Price", value=105.0)
volume = st.number_input("Volume", value=1000000.0)
rolling_vol = st.number_input("Rolling Volatility (7 days)", value=0.02)
liquidity = st.number_input("Liquidity Ratio", value=0.01)

if st.button("Predict Volatility"):
    data = np.array([[open_p, high_p, low_p, close_p,
                      volume, rolling_vol, liquidity]])
    pred = model.predict(data)
    st.success(f"Predicted Volatility: {pred[0]:.6f}")

