ALPHAVANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query?"
ALPHAVANTAGE_APIKEY = "KE7MBHHWS14Q5O95"

import requests

def fetch_data_intraday(stock):
    '''GET request to alphavantage API to download csv and save it in assets'''
    parameters_intraday = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': stock,
    'interval': '5min',
    'apikey': ALPHAVANTAGE_APIKEY,
    'datatype': 'csv'
}
    response = requests.get(url=ALPHAVANTAGE_API_ENDPOINT, params=parameters_intraday)
    if response.status_code == 200:
        daily_data = response.text
        with open(f'intraday_data/{stock}_intraday.csv', mode='w') as file:
            file.write(daily_data)

def fetch_data_daily(stock):
    '''GET request to alphavantage API to download csv and save it in assets'''
    parameters_daily = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': stock,
    'apikey': ALPHAVANTAGE_APIKEY,
    'datatype': 'csv'
}
    response = requests.get(url=ALPHAVANTAGE_API_ENDPOINT, params=parameters_daily)
    if response.status_code == 200:
        daily_data = response.text
        with open(f'daily_data/{stock}_daily.csv', mode='w') as file:
            file.write(daily_data)