# pip install matplotlib
# pip install seaborn

import matplotlib.pyplot as plt
import numpy as np

# 두가지 그래프를 따로 그리고 싶을때
t = np.arange(0, 5, 0.5)

plt.figure(figsize=(10,6))
plt.plot(t,t**2,'bs')
plt.figure(figsize=(10,6))
plt.plot(t,t**3,'g^')
plt.show()

# 시각화 추가
t = [0,1,2,3,4,5,6]
y = [1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dashed',marker='o',markerfacecolor='blue' ,markersize=12)
plt.show()

# scatter
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,6,4,2,4,5,6,7])
plt.figure(figsize=(10,6))
plt.scatter(t,y)
plt.show()

# scatter ~ marker
plt.figure(figsize=(10,6))
plt.scatter(t,y,marker='>')
plt.show()

# 색표현
colormap = t
plt.figure(figsize=(12,6))
plt.scatter(t,y,s=50,c=colormap,marker='>')
plt.colorbar()
plt.show()

# 정규분포
s1 = np.random.normal( loc=0 , scale=1 , size=1000)
s2 = np.random.normal( loc=5 , scale=0.5 , size=1000)
s3 = np.random.normal( loc=10 , scale=2 , size=1000)
plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()

# boxplot
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.grid()
plt.show()

# 한 화면에 분할해서 보여주기
plt.figure(figsize=(10,6))
plt.subplot(221)
plt.subplot(222)
plt.subplot(223)
plt.show()

t = np.arange(0,5,0.01)
plt.figure(figsize=(10,12))
plt.subplot(411)
plt.plot(t,np.sqrt(t))             # subplot 의 의미는 4x2 사각형에서 
plt.grid()

plt.subplot(423)
plt.plot(t,t**2)
plt.grid()

plt.subplot(424)
plt.plot(t,t**3)
plt.grid()

plt.subplot(413)
plt.plot(t,np.sin(t))
plt.grid()

plt.subplot(414)
plt.plot(t,np.cos(t))
plt.grid()

plt.show()