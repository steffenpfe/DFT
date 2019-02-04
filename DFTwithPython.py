# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:38:32 2019

@author: Steffen
"""
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import random as rand
#sample rate
dT = 0.1
#window length
T = 100
#Amount of samples
N = T/dT
#time axis
t = np.linspace(0, T, N-1) #->DFT 0-N -> N-1
#frequency axis
f = np.linspace(0, 1/dT, N-1)
#sine
s = np.sin(2*np.pi*1*t)
#white noise
r = np.array([], dtype='f')
for i in range(int(N-1)):
    r = np.append(r, [rand.uniform(-1,1)])
#signal with noise
sr = s+r
#DFT
yf_s = fft(s)
yf_sr = fft(sr)

#plots
fig, axs = plt.subplots(3,1)
axs[0].plot(t,sr)
axs[0].set_xlabel('time')
axs[0].set_ylabel('noise')
axs[1].plot(t,s)
axs[1].set_xlabel('time')
axs[1].set_ylabel('sine')
axs[2].plot(f,abs(yf_sr))
axs[2].set_xlabel('frequency')
axs[2].set_ylabel('DFT-value')
plt.show()

plt.plot(f,abs(yf_s))