
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print(sns.__version__)
iris = sns.load_dataset('iris')
print(iris.head())

# pairplot
plt.show(sns.pairplot(iris))

# 구분기준
plt.show(sns.pairplot(iris,hue='species'))

# 색변화
plt.show(sns.pairplot(iris,hue='species', palette='husl'))

# 상관관계
plt.show(sns.pairplot(iris,size=3,vars=['sepal_width' , 'sepal_length']))

###############################################################################################

tips = sns.load_dataset('tips')
print(type(tips))    # <class 'pandas.core.frame.DataFrame'>

# set style
sns.set_style('whitegrid')

# joinplot
plt.show(sns.jointplot(x='total_bill',y='tip', data=tips))

plt.show(sns.jointplot('sepal_width','petal_width',data=iris, kind='kde',space=0 , color='b')) # kde 치우침정도를 보여줌 (위아래에)

# boxplot
plt.show(sns.boxplot(x='day',y='total_bill', hue='smoker',data=tips, palette='Set3'))

###############################################################################################

g = sns.FacetGrid(tips , col='time', size=5 , aspect=0.7)
plt.show(g.map(sns.boxplot , 'sex', 'total_bill' , 'smoker').despine(left=True).add_legend(title='smoker'))

# lmplot ( 회귀분석)
plt.show(sns.lmplot( x='total_bill' , y='tip', hue='smoker' , data =tips))

# <중요> 회귀분석 2가지 기준으로 비교할때 
plt.show(sns.lmplot( x='total_bill' , y='tip' , row='sex' , col='time' , data=tips ,size=3))


###############################################################################################

