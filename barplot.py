import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('kutubxona.csv')
plt.figure(figsize=(16,2))
sns.barplot(data=df)
plt.savefig('barplot.png')
plt.show()