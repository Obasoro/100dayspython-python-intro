# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:38:58 2019

@author: Toyin Obasoro
"""
# Synthetic dataset 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X, y = datasets.make_wave(n_samples = 40)
plt.plot (X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel('Features')
plt.ylabel('Target')