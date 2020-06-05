"""
Matplotlib 绘图
pip install brewer2mpl
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
midwest = pd.read_csv('./resources/csv/midwest_filter.csv')
# Create as many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1))
          for i in range(len(categories))]
# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s=20, c=colors[i], label=str(category))
# Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
xlabel='Area', ylabel='Population')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Scatterplot of Midwest Areaa vs Popilation', fontsize=22)
plt.legend(fontsize=12)
plt.show()
plt.savefig('./resources/img/散点图.png')
