#!/usr/bin/env python3

#@Author: Akash Manna
#@Date: 2023-10-05

'''
This code provides the velocity from the doppler shift values
'''

# Doppler Velocity Calculation
c = 3 * 10**8  # speed of light
radarFreq = 77e9  # frequency in Hz

# Task 1: Calculate the wavelength
lambda_val = c / radarFreq

# Task 2: Define the doppler shifts in Hz using the information from above
dopplerShift = [3 * 10**3, -4.5 * 10**3, 11 * 10**3, -3 * 10**3]

# Task 3: Calculate the velocity of the targets  fd = 2*vr/lambda
vr = [shift * lambda_val / 2 for shift in dopplerShift]

# Task 4: Display results
print(vr)
