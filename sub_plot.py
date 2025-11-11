# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df=pd.read_csv('cars.csv')
# fig,ax=plt.subplots(2,2,figsize=(15,5))
# fig.suptitle('grafick 2')
# sns.histplot(data=df,x='price',ax=ax[0,0])
# sns.scatterplot(data=df,x='brand',ax=ax[0, 1])
# sns.barplot(data=df,x='model',ax=ax[1, 0])
# sns.lineplot(data=df,x='transmission',ax=ax[1, 1])
# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cars.csv')

fig, ax = plt.subplots(2, 2, figsize=(15, 8))
fig.suptitle('Grafik 2')

# 1 - Histogram (narx taqsimoti)
sns.histplot(data=df, x='price', ax=ax[0, 0]).set_title('price')

# 2 - Scatterplot (brand va price)
sns.scatterplot(data=df, x='brand', y='year', ax=ax[0, 1]).set_title('brand and year')

# 3 - Barplot (brand bo‘yicha o‘rtacha price)
sns.barplot(data=df, x='brand', y='engine_type', ax=ax[1, 0]).set_title('brand and engine_type')

# 4 - Lineplot (yillar bo‘yicha o‘rtacha price)
sns.lineplot(data=df, x='year', y='horsepower', ax=ax[1, 1]).set_title('year and horse_power')
plt.tight_layout()
plt.savefig('all_iin_one.png')
plt.show()
