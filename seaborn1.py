import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('p.csv')
d=pd.read_csv('muzey.csv')
# print(df)
plt.figure(figsize=(25,12))
sns.lineplot(data=df)
sns.lineplot(data=d)
plt.grid(color='red')
plt.savefig('muzey.png')
plt.show()