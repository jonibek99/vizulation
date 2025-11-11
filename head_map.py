import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('muzey.csv',parse_dates=['visit_date'])  
df['month'] = df['visit_date'].dt.month
df['year']=df['visit_date'].dt.year
df2 = df.groupby(['month','year'])['id'].max()
# print(df2)
plt.figure(figsize=(12,6))
sns.heatmap(data=df2.unstack(level=1),cmap='ocean',linewidths=0.6,square=True)
plt.xticks(rotation=90)
plt.grid()
plt.savefig('head_mp.png')
plt.show()