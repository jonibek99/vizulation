import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('p.csv')

city=pd.read_csv('city.csv')
print(df)

plt.figure(figsize=(12,5))
sns.barplot(data=df)
plt.title('')
plt.xticks(rotation=90)
plt.savefig('p.png')
plt.show()

