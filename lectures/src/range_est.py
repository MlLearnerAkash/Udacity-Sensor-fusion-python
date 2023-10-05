#!/usr/bin/env python3

#@Author: Akash Manna
#@Date:05/10/2023

'''
Write a Python program to get the range from the beat frequency
'''

#Constants
c=3*10**8

#Parameters
maxRange=300
rangeRes=1
factor= 5.5 #FMCW ssytem has sweep time of 5 to 6 times of its round trip time

#measured Beta Frequency
betaFreq=[0, 1.1 * 10**6, 13 * 10**6, 24 * 10**6]

#Task:1 Find the Bsweep of chirp for 1 m resolution
Bsweep= 0.5*c/rangeRes
print("Bsweep=", Bsweep)

#Task:2 Chirp time calculation
Ts= factor*2*maxRange/c

#Task:3 Find the range for each beta frequency
for i in range(len(betaFreq)):
    range= (betaFreq[i]*Ts*c)/(2*Bsweep)
    print("Range for beta frequency", betaFreq[i], "is", range)
#Range calculation