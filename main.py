from requests import request, Session
import json
import streamlit as st
import apikey
import pprint
from PIL import Image
import time
import yfinance as yf

cryptoName = st.sidebar.text_input("Crypto Currency Name")


def api_request_data():
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    parameters = {
        "slug": "ethereum",
        "convert": "USD"
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": apikey.KEY
    }

    s = Session()
    s.headers.update(headers)
    response = s.get(url, params=parameters).json()
    pprint.pprint(response)

    # data variable defining here

    coin_name = response["data"]["1027"]["name"]
    coin_symbol = response["data"]["1027"]["symbol"]
    coin_price = response["data"]["1027"]["quote"]["USD"]["price"]
    coin_volume_24hr = response["data"]["1027"]["quote"]["USD"]["volume_24h"]
    coin_volume_change_24hr = response["data"]["1027"]["quote"]["USD"]["volume_change_24h"]
    percent_change_1hr = response["data"]["1027"]["quote"]["USD"]["percent_change_1h"]
    percent_change_24hr = response["data"]["1027"]["quote"]["USD"]["percent_change_24h"]
    percent_change_7d = response["data"]["1027"]["quote"]["USD"]["percent_change_7d"]
    percent_change_30d = response["data"]["1027"]["quote"]["USD"]["percent_change_30d"]
    market_cap = response["data"]["1027"]["quote"]["USD"]["market_cap"]

    # streamlit styling here

    st.write("# Crypto Currency Price Tracker - By Atrin Shahroudi")
    st.write(f"### {coin_name}, {coin_symbol} | \n #### Market Cap: ${market_cap}")
    col1, col2 = st.columns(2)
    col1.metric("Coin Name", f"{coin_name}")
    col2.metric("Coin Price", f"${round(coin_price, 2)}", f"{percent_change_1hr}")
    col3, col4, col5 = st.columns(3)
    col3.metric("Percentage change 24 hour", "", f"{percent_change_24hr}")
    col4.metric("Percentage change 7 days", "", f"{percent_change_7d}")
    col5.metric("Percentage change 30 days", "", f"{percent_change_30d}")
    st.write(f"#### Coin Volume: {round(coin_volume_24hr, 2)}")
    st.metric(label="Coin Volume Change", value="", delta=f"{coin_volume_change_24hr}")


if __name__ == '__main__':
    api_request_data()
