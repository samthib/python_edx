# -*- coding: utf-8 -*-
"""
Created on Tue May  5 01:39:56 2020

@author: Sam
"""

# DO NOT EDIT THIS CODE
import pandas as pd
import numpy as np
birddata = pd.read_csv("bird_tracking.csv", index_col=0)
birddata.head()


# Exercice 1

# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby(["bird_name"])

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds["speed_2d"].mean()

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds["altitude"].mean()


#print(mean_altitudes)


# Exercice 2

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata["date_time"])

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby(["date"])

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates["altitude"].mean()

#print(mean_altitudes_perday.iloc[20:40])


# Exercice 3

# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday["altitude"].mean()

#print(mean_altitudes_perday)

# Exercice 4

import matplotlib.pyplot as plt

eric_daily_speed  = grouped_birdday["speed_2d"].mean()['Eric']
sanne_daily_speed = grouped_birdday["speed_2d"].mean()['Sanne']
nico_daily_speed  = grouped_birdday["speed_2d"].mean()['Nico']

#print(nico_daily_speed.tail(30))

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
