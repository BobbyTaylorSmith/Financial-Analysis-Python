# -*- coding: utf-8 -*-
"""Using RSI and Python to Determine if Bitcoin is Oversold.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WyXM9in2PGIhxx4dcmMrYExaJMI4SfqK
"""

#This program determines if BTC is over bought or over sold

#Import the dependecies 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

#Load the data 
from google.colab import files 
files.upload()

#Store the data 
df = pd.read_csv('BTC-USD.csv')

#Set teh data as the index 
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

#Show the data 
df

#Create and plot the grapgh 

plt.figure(figsize = (12.2,4.5))
plt.plot(df.index, df['Close'], label = 'Close')
plt.title('Close Price')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.show()

#Calculate the RSI 
delta = df['Close'].diff(1)
delta = delta.dropna()
up = delta.copy()
down = delta.copy()
up[up < 0 ] = 0 
down [ down > 0 ] = 0
time_period = 14 
AVG_Gain = up.rolling(window=time_period).mean()
AVG_Loss = abs( down.rolling(window=time_period).mean() )
RS = AVG_Gain / AVG_Loss 
RSI = 100.0 - (100.0/ (1.0 + RS))

#Plot the RSI 
plt.figure(figsize=(12.2, 4.5)) 
RSI.plot()
plt.show()

#Plot the RSI with over bought and over sold RSI lines/levels 
fig, ax = plt.subplots(1, 1, figsize=(15,5))
ax0=RSI.plot(ax=ax)
ax0.axhline(30, color='green')
ax0.axhline(70, color='green')
ax0.axhline(20, color='yellow')
ax0.axhline(80, color='yellow')
ax0.axhline(10, color='red')
ax0.axhline(90, color='red')