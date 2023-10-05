#!/usr/bin/env python3

#@Author: Akash
#@Date: 2023-10-05

'''
This code is to find the find the signal component using FFT
'''

import numpy as np
import matplotlib.pyplot as plt

#Constants
Fs= 1000
T= 1/Fs
#Length of the signal
L=1500
#Time vector
t=np.arange(0, L)*T

#Task:1 Generate the signal of 77Hz of 0.7 and 43Hz of amplitude 2
A1=0.7
f1=77
A2=2
A2=2
f2=43

#Signal generation
s= A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t)

#Corrupt the signal by adding noise
sn=s+2*np.random.randn(len(t))

#Plot the signal and its difficult to seperate out two frequency compont
plt.plot(1000*t[:50], s[:50])
plt.xlabel('Time(ms)')
plt.ylabel('Amplitude')
plt.title('Signal with noise')
plt.show()

#Task:2 Find the FFT of the signal
signal_fft= np.fft.fft(sn)

#Task:3 compute the two sided spectrum P2. The compute the single sided 
#Spectrum P1 using P2
P2= np.abs(signal_fft)
P1= P2[:L//2+1]

#Task:4 Plot the spectrum
f= Fs* np.arange(0, L//2+1)/L
plt.plot(f, P1)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of the signal')
plt.show()


