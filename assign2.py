import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np

data = pd.read_csv("covidIndia.csv")

sns.relplot(x="Total Confirmed cases",y="Cured/Discharged/Migrated",kind='line',data=data)
plt.show()
print(data.head())
print(data.tail())
print(data.columns)
print(data.describe())