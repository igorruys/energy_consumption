import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone

#df = pd.read_csv('https://raw.githubusercontent.com/igorruys/energy_consumption/main/light.csv', parse_dates=['date'], index_col='date')
df = pd.read_csv('https://raw.githubusercontent.com/igorruys/energy_consumption/main/light.csv')

# Formatting date.
# Maybe later define a new variable so we are not altering the original column but a copy.
df['date'] = df['date'].str.split('+').str[0]
df['date'] = df['date'].str.split('T').str[1]

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Light', dpi=100):
    # Setting up x-axis because there are too much readings: 1 label for each 20 seconds.
    xaxis = []
    for i in range(x.shape[0]):
        if i % 20 == 0:
            xaxis.append(i)

    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.xticks(xaxis, rotation=30)
    plt.show()

plot_df(df, x=df['date'], y=df['light'], title='Light values.')

# Code for generating points, one by one, in a graph
""" for i in range(50):
    x = np.random.uniform(0,10)
    y = np.sin(x)
    plt.scatter(x, y)
    plt.pause(0.05)

plt.show() """