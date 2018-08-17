import numpy as np
import pandas as pd

# numpy는 주로 배열을 (1차원 ) , pandas는 dataframe을 (2차원)

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130405', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4) , index=dates, columns=['A','B','C','D']) # df의 인덱스 표시가능 ! & 컬럼명 지정 !
print(df)

print(df.head(2))
print(df.tail(2))
print(df.values)
print(df.info())
print(df.describe())  # summarize
print(df.sort_values(by='B' , ascending=False))

print('='*45)

print(df['A']) #column
print(df[0:2]) # row

print(df.loc[dates[0]])
print(df.loc[ : , ['A','B']])   # row는 전체 / col은 특정 열만 ++ loc란 명령어를 꼭 붙여 주어야 한다 !!
print(df.loc[ '2013-04-08' :  , ['A','D']])  # 특정행렬 동시 인덱싱 연습    ++  보고싶지만 떨어져있는건  [리스트]로 묶는다 !!

### loc는 이름을 알아야한다는 단점이 있다 

# iloc는 숫자를 기준으로 찾아준다 ! 
print(df.iloc[3])     # 인덱싱에 하나만 들어가면 default 값은 row
print(df.iloc[0:2,1:3])   ## 마지막 숫자는 포함 안된다 !! 0이상2미만
print(df.iloc[[0,2],[1,3]])

# 특정 열로 접근 / 조건 식 부여
print(df[df.A>0])

# 데이터프레임 복사 하기
df2 = df.copy()

# 행/열 추가
df2['E'] = ['one','two','a','b','c','d']
print(df2)

# 특정값 진위 여부 확인
print(df2['E'].isin(['two','d']))   # 결과값 블린형

print( df2[ df2['E'].isin(['two','d']) ])  # True 값 추출

# 열 전체(연속데이터) 계산
print ( df.apply(np.cumsum))    # df에 apply해라 np의 cumsum을

# 
print( df.apply( lambda x : x.max() - x.min() ))