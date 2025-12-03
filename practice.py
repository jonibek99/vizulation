import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('english.csv')

plt.figure(figsize=(10,6))
sns.lineplot(data=data)
plt.title("Asadbek teacher's students' English scores")
plt.xticks(rotation=45*2)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('english_scores.png')
plt.show()
