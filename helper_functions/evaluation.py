import numpy as np
import pandas as pd 
    
def eval_long(x:pd.DataFrame):
    delta = []
    roi = []
    lo = x['long_open']
    lc = x['long_close']
    array = lc.dropna().index.insert(0,0)
    K = []
    SUM = []
    for n in range(2, len(array)):
        subarray = lo[array[n-1]:array[n]].dropna()
        K.append(len(subarray))
        SUM.append(subarray.sum())
    lc_lim = lc.dropna()
    for n in range(len(lc_lim)-1):
        delta.append((lc_lim.iloc[n] * K[n])-SUM[n])
        if (SUM[n] != 0):
            roi.append(((lc_lim.iloc[n] * K[n])-SUM[n])/SUM[n])
    return delta, roi

def eval_short(x:pd.DataFrame):
    delta = []
    roi = []
    so = x['short_open']
    sc = x['short_close']
    array = sc.dropna().index.insert(0,0)
    K = []
    SUM = []
    for n in range(2, len(array)):
        subarray = so[array[n-1]:array[n]].dropna()
        K.append(len(subarray))
        SUM.append(subarray.sum())
    sc_lim = sc.dropna()
    for n in range(len(sc_lim)-1):
        delta.append(SUM[n]-(sc_lim.iloc[n] * K[n]))
        if (SUM[n] != 0):
            roi.append((SUM[n]-(sc_lim.iloc[n] * K[n]))/SUM[n])
    return delta, roi

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

def mean(list):
    if len(list) != 0:
        return (sum(list)/len(list))
    else:
        return 0