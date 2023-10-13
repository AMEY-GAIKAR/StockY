import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpl
from pyti.bollinger_bands import upper_bollinger_band, lower_bollinger_band, middle_bollinger_band

class Entity:
    def __init__(self, df_daily: pd.DataFrame, df_intraday: pd.DataFrame):
        self.df_daily = df_daily
        self.df_intraday = df_intraday
        self.create_bollinger_bands_intraday()
        self.create_bollinger_bands_daily()
        self.detect_points_intraday()
        self.detect_points_daily()
        self.positions_intraday()
        self.positions_daily()

    def create_bollinger_bands_intraday(self, WINDOW=7):
        self.df_intraday['mbb'] = middle_bollinger_band(self.df_intraday['close'], WINDOW)
        self.df_intraday['ubb'] = upper_bollinger_band(self.df_intraday['close'], WINDOW)
        self.df_intraday['lbb'] = lower_bollinger_band(self.df_intraday['close'], WINDOW)

    def create_bollinger_bands_daily(self, WINDOW=20):
        self.df_daily['mbb'] = middle_bollinger_band(self.df_daily['close'], WINDOW)
        self.df_daily['ubb'] = upper_bollinger_band(self.df_daily['close'], WINDOW)
        self.df_daily['lbb'] = lower_bollinger_band(self.df_daily['close'], WINDOW)

    def plot_bollinger_bands_intraday(self):
        plt.title('Intraday Bollinger Bands')
        plt.plot(self.df_intraday['close'], c='blue')
        plt.plot(self.df_intraday['mbb'], c='grey')
        plt.plot(self.df_intraday['ubb'], c='green')
        plt.plot(self.df_intraday['lbb'], c='red')

    def plot_bollinger_bands_daily(self):
        plt.title('20-Day Bollinger Bands')
        plt.plot(self.df_daily['close'], c='blue')
        plt.plot(self.df_daily['mbb'], c='grey')
        plt.plot(self.df_daily['ubb'], c='green')
        plt.plot(self.df_daily['lbb'], c='red')

    def mpl_intraday_plot(self, type='candle', mav=()): 
        mpl.plot(self.df_intraday.set_index(pd.to_datetime(self.df_intraday['timestamp'])), type=type, mav=mav)

    def mpl_daily_plot(self, type='candle', mav=()): 
        mpl.plot(self.df_daily.set_index(pd.to_datetime(self.df_daily['timestamp'])), type=type, mav=mav)

    def detect_points_intraday(self):
        self.BUY_POINTS_INTRADAY = np.array(self.df_intraday[(self.df_intraday['close'] < self.df_intraday['lbb'])]['timestamp'])
        self.SELL_POINTS_INTRADAY = np.array(self.df_intraday[(self.df_intraday['close'] > self.df_intraday['ubb'])]['timestamp'])

    def detect_points_daily(self):
        self.BUY_POINTS_DAILY = np.array(self.df_daily[(self.df_daily['close'] < self.df_daily['lbb'])]['timestamp'])
        self.SELL_POINTS_DAILY = np.array(self.df_daily[(self.df_daily['close'] > self.df_daily['ubb'])]['timestamp'])

    def plot_points_intraday(self):
        plt.plot(self.df_intraday['close'])
        for n in range(len(self.BUY_POINTS_INTRADAY)):
            plt.plot(self.df_intraday[self.df_intraday['timestamp'] == self.BUY_POINTS_INTRADAY[n]]['close'], '^', color='g')
        for n in range(len(self.SELL_POINTS_INTRADAY)):
            plt.plot(self.df_intraday[self.df_intraday['timestamp'] == self.SELL_POINTS_INTRADAY[n]]['close'], 'v', color='r')

    def plot_points_daily(self):
        plt.plot(self.df_daily['close'])
        for n in range(len(self.BUY_POINTS_DAILY)):
            plt.plot(self.df_daily[self.df_daily['timestamp'] == self.BUY_POINTS_DAILY[n]]['close'], '^', color='g')
        for n in range(len(self.SELL_POINTS_DAILY)):
            plt.plot(self.df_daily[self.df_daily['timestamp'] == self.SELL_POINTS_DAILY[n]]['close'], 'v', color='r')
    
    def positions_intraday(self):
        self.df_intraday['long_open'] = self.df_intraday[(self.df_intraday['close'].shift() < self.df_intraday['lbb'].shift())]['open']
        self.df_intraday['short_open'] = self.df_intraday[(self.df_intraday['close'].shift() > self.df_intraday['ubb'].shift())]['open']

        self.df_intraday['long_close'] = self.df_intraday[(self.df_intraday['close'].shift() > self.df_intraday['mbb'].shift())]['open']
        self.df_intraday['short_close'] = self.df_intraday[(self.df_intraday['close'].shift() < self.df_intraday['mbb'].shift())]['open']

    def positions_daily(self):
        self.df_daily['long_open'] = self.df_daily[(self.df_daily['close'].shift() < self.df_daily['lbb'].shift())]['open']
        self.df_daily['short_open'] = self.df_daily[(self.df_daily['close'].shift() > self.df_daily['ubb'].shift())]['open']

        self.df_daily['long_close'] = self.df_daily[(self.df_daily['close'].shift() > self.df_daily['mbb'].shift())]['open']
        self.df_daily['short_close'] = self.df_daily[(self.df_daily['close'].shift() < self.df_daily['mbb'].shift())]['open']


    
