# pip install matplotlib
# pip install seaborn

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.plot([1,2,3,4,5,6,7,6,5,4,4,3,2,1,0])
plt.show()

t = np.arange(0,12,0.01)
y = np.sin(t)

plt.figure(figsize=(10,6)) # 가로로10 세로로6의 크기
# plt.plot(t,y)

# 두가지 그래프를 동시에 시각화 가능
plt.plot(t,np.sin(t), lw=3 ,label='sin' )  # lw는 굵기   
plt.plot(t,np.cos(t), 'r' , label='cos' )   # 'r' 은 색 지정

plt.grid()  # 눈금선
plt.legend() # 우측상단에 구분해주는 표시 넣기
plt.xlabel('time')      # 범례지정
plt.ylabel('Amplitude')
plt.title('Example of sinewave') # 제목넣기 
plt.ylim(-1.2,1.2) # 영역설정
plt.xlim(0,np.pi)  # np.pi = 3.14... 
plt.show()

# 시각화 추가
plt.figure(figsize=(10,6))
plt.plot(t,t,'r--')     # 빨간 점선
plt.plot(t,t**2,'bs')   # 파란 사각형
plt.plot(t,t**3,'g^')   # 초록색 삼각형
plt.show()