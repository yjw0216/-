
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print(sns.__version__)
iris = sns.load_dataset('iris')
# print(iris.head())
tips = sns.load_dataset('tips')

###############################################################################################
flights = sns.load_dataset('flights')
print(flights.head())

# pivot table
flights = flights.pivot('month' , 'year' , 'passengers')
print(flights.head())

# heatmap
plt.show(sns.heatmap(flights))

plt.show(sns.heatmap(flights , annot=True , fmt='d'))

