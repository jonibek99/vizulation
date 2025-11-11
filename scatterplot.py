import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('cars.csv')
plt.figure(figsize=(20,10))
sns.scatterplot(data=df,x='horsepower',y='price')
# sns.regplot(data=df,x='year',y='price')
# sns.crayon_palette(df)
plt.xticks(rotation=90)
plt.savefig('scatter_plot.png')
plt.show()