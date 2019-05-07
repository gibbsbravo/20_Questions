# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:49:27 2019

@author: ACZD071
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random


def moving_average(a, n=3):
    if isinstance(a, pd.Series):
        return plt.plot(a.rolling(n).mean())
    else:
        ret = np.cumsum(a, dtype=float)
        ret[n:] = ret[n:] - ret[:-n]
        return plt.plot(ret[n - 1:] / n)


data = pd.read_csv('model_results.txt', sep=" ", header=None, names = ['episode','return','epsilon'],
                  dtype = {'episode':np.int,'return':np.float32,'epsilon':np.float32})

moving_average(data['return'],500);

len(data)