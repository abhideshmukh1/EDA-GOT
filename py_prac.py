import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pandas import Series

location = "C:/Users/TKMAL5U/Downloads/game-of-thrones/battles.csv"
battles = pd.read_csv(location)
battles  = pd.DataFrame(battles)

battles['attacker_size'] = pd.to_numeric(battles['attacker_size'])
battles['defender_size'] = pd.to_numeric(battles['defender_size'])
print("head",battles.head())
print("info",battles.info())
print("describe", battles.describe())

###################################################################################3
"""scatter plot - the attacker size for each battle"""

plt.scatter(battles['attacker_size'], battles['name'])
plt.grid(axis='y')
plt.title('scatter plot for the GOT battle name and the attacker size')
plt.xlabel('battle name')
plt.ylabel('attacker_size')
plt.show()
#########################################################################


"""scatter plot -  the defender size for each battle"""

plt.scatter(battles['defender_size'], battles['name'])
plt.grid(axis='y')
plt.title('scatter plot for the GOT battle name and the defender size')
plt.xlabel('battle name')
plt.ylabel('defender_size')
plt.show()
#########################################################################


"""bar plots to compare the size if the attacker and defender armies for each battle"""

#******       still figuring out how subplots for attackers and defender for each battle     ******************

#data to plot
n_groups = battles['name']
attacker = battles['attacker_size']
defender = battles['defender_size']

#create plot
fig, ax = plt.subplots()
#index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(n_groups, attacker, bar_width, alpha=opacity, color = 'b', label = 'attacker')

rects2 = plt.bar(n_groups+bar_width, defender, bar_width, alpha=opacity, color = 'r', label = 'defender')

plt.xlabel('Battle name')
plt.ylabel('army sizes')
plt.title('Size of the attacking and defending armies for each battle')
#plt.xticks(index + bar_width)
plt.legend()

plt.tight_layout()
plt.show()
