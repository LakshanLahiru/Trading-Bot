import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weatherData.csv')
#print(df.head())
#print(df["Temp"])
plt.hist(df["Temp"],color='green',rwidth=0.95,edgecolor='black',bins=30)
plt.xlabel("Temperature")
plt.ylabel("Count")
plt.show()

sns.histplot(df["Temp"],color='green',rwidth=0.95,edgecolor='black',bins=10)
