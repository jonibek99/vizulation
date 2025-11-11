import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('cars.csv')

# sns.displot(data=df,kde=True,x='price',height=5,aspect=2)
# plt.grid()
# plt.savefig('kde.png')
# plt.show()

plt.figure(figsize=(16,8))
sns.kdeplot(data=df,x='price',hue='engine_type',shade=True,color='red')
plt.show()