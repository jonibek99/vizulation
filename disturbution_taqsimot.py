import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('cars.csv')
# plt.figure(figsize=(16,8))
sns.displot(data=df,col='transmission',x='price',height=5,aspect=2)
plt.savefig('hislot.png')
plt.xticks()
plt.xticks(rotation=90)
plt.xlabel('uqi')
plt.ylabel('uzunligi')
plt.show()