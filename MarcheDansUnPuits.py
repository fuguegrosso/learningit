# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:10:41 2017

@author: Yitao
"""

import numpy as np
import matplotlib.pyplot as plt

def PieceTruquee(p):
    return 2 * (np.random.rand()<p) -1

#Histogramme: convergence vers la mesure stationnaire
K = 2000 #number of steps
n = 5 # number of states
T = 200  #duration of the simulatrion
p = 0.666667

FinalValues = []
for k in range(K):
    MarcheDansUnPuits = np.zeros((1,T))
    #MarcheDansUnPuits[0,0] = -n
    for t in range(1, T):
        if MarcheDansUnPuits[0,t-1] > 0:
            MarcheDansUnPuits[0,t] = min(MarcheDansUnPuits[0,t-1] + PieceTruquee(p),n)
        elif MarcheDansUnPuits[0,t-1] < 0:
            MarcheDansUnPuits[0,t] = max(MarcheDansUnPuits[0,t-1] + PieceTruquee(1-p), -n)
        else:
            MarcheDansUnPuits[0,t] = MarcheDansUnPuits[0,t-1] + PieceTruquee(0.5)
    FinalValues.append(MarcheDansUnPuits[0,T-1])
#print(FinalValues)
plt.hist(FinalValues, bins = 2*n+1, normed = True, facecolor = 'g', alpha = 0.2)
plt.show()