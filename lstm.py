import requests
import json
from datetime import datetime, timedelta

def get_historical_candles(instrument_key, to_date, interval='day', from_date=None):
    # Base URL for the API
    base_url = "https://api.upstox.com/v2/historical-candle"
    
    # Construct the request URL
    url = f"{base_url}/{instrument_key}/{interval}/{to_date}"
    
    if from_date:
        url += f"?from_date={from_date}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['data']['candles']
        else:
            print("Error: ", data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    
    return None

#the average over the last 10 years of daily OHLC data for a given stock
def display_daily_ohlc(instrument_key, days=3650):
    to_date = datetime.today().strftime('%Y-%m-%d')
    from_date = (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    candles = get_historical_candles(instrument_key, to_date, 'day', from_date)

    if candles:
        print(f"{'Date':<15} {'Open':<10} {'High':<10} {'Low':<10} {'Close':<10}")
        for candle in candles:
            date = candle[0].split('T')[0]
            open_price = candle[1]
            high_price = candle[2]
            low_price = candle[3]
            close_price = candle[4]
            print(f"{date:<15} {open_price:<10} {high_price:<10} {low_price:<10} {close_price:<10}")

# Example usage
instrument_key = "NSE_EQ%7CINE848E01016"
display_daily_ohlc(instrument_key)
