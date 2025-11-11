import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('cars.csv')

sns.displot(data=df,kind='ecdf',x='price',height=5,aspect=2)
plt.xticks(rotation=90)
plt.grid(which='both')
plt.minorticks_on()
plt.savefig('ecdf.png')
plt.show()