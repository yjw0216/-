
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 깨짐 해결 코드 
import platform 
from matplotlib import font_manager ,rc  # resource controll
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin' :  # Mac
    rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    path='c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font' , family = font_name)
else:
    print('리눅스안씀')



## data02.py 꺼 csv파일로 해놓음 .
# data_result.to_csv('data/data_result.csv',index=True)
data_result = pd.read_csv('data/data_result.csv')


# visualization 
plt.figure()
data_result['소계'].plot(kind='barh',grid=True , figsize=(10,10))
plt.show()

# sort
plt.figure()
data_result['소계'].sort_values().plot(kind='barh',grid=True , figsize=(10,10))
plt.show()

# 이미지파일로 저장
data_result['CCTV비율'] = (data_result['소계'] / data_result['인구수']) *100
data_result['CCTV비율'].sort_values().plot(kind='barh' , grid=True , figsize=(10,10))
plt.savefig('cctv1.png')
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'],data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# 상관관계분석
fp1 = np.polyfit(data_result['인구수'],data_result['소계'] , 1) # 1차원에서
print(fp1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000,700000,100)
plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'],data_result['소계'], s=50)
plt.plot( fx , f1(fx) , ls='dashed' , lw =3 , color = 'g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


fp1 = np.polyfit(data_result['인구수'],data_result['소계'] , 1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000,700000,100)
data_result['오차'] = np.abs(data_result['소계']- f1(data_result['인구수']))
print(data_result.head())

df_sort = data_result.sort_values(by='오차' , ascending=False)
print(df_sort.head())

# 반복문 추출 + 시각화
plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'] , data_result['소계'] , c=data_result['오차'] , s=50) # c는 색깔 !!!!!!!!!!!!!! 중요 !!!!
plt.plot(fx , f1(fx), ls='dashed' , lw=3 , color='r')
for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02 , df_sort['소계'][n]*0.98 , df_sort.index[n] , fontsize=15)
   # 텍스트 뽑기

plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.colorbar()
plt.grid()
plt.show()