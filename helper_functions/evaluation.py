import numpy as np
import pandas as pd 

def eval(x):
    position = 0
    long_open = []
    long_close = []

    for idx, data in x.iterrows():
        long_open.append(data['long_open'])
        long_close.append(data['long_close'])

        if position == 1 and np.isnan(data['long_close']) == False:
            position = 0
        elif position == 0 and np.isnan(data['long_close']) == False:
            long_close[len(long_close)-1] = np.nan
        elif position == 0 and np.isnan(data['long_open']) == False:
            position = 1
        elif position == 1 and np.isnan(data['long_open']) == False:
            long_close[len(long_open)-1] = np.nan

    x['long_open'] = long_open
    x['long_close'] = long_close

    position = 0
    short_open = []
    short_close = []

    for idx, data in x.iterrows():
        short_open.append(data['short_open'])
        short_close.append(data['short_close'])

        if position == 1 and np.isnan(data['short_close']) == False:
            position = 0
        elif position == 0 and np.isnan(data['short_close']) == False:
            short_close[len(short_close)-1] = np.nan
        elif position == 0 and np.isnan(data['short_open']) == False:
            position = 1
        elif position == 1 and np.isnan(data['short_open']) == False:
            short_close[len(short_open)-1] = np.nan

    x['short_open'] = short_open
    x['short_close'] = short_close

def net(x):
    lo = np.array(x['long_open'].dropna())
    lc = np.array(x['long_close'].dropna())
    so = np.array(x['short_open'].dropna())
    sc = np.array(x['short_close'].dropna())

    net = 0

    if len(lo) > 0:
        for n in range(len(lc)):
            if lo[n]:
                net += lc[n] - lo[n]

        for n in range(len(sc)):
            if so[n]:
                net += sc[n] - so[n] 
        return net
    else:
        return 0