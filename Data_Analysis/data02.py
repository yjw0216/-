import pandas as pd

CCTV_Seoul = pd.read_csv('data/01. CCTV_in_Seoul.csv')
# print(CCTV_Seoul.head())

# 칼럼 확인
CCTV_Seoul.columns

# 칼럼명 변경
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:"구별"}, inplace=True ) # inplace 는 원본 데이터도 고치겠다!
# print(CCTV_Seoul.columns)
# print(CCTV_Seoul.head())


pop_Seoul = pd.read_excel('data/01. population_in_Seoul.xls' , header=2 , usecols='B,D,G,J,N' , encoding='utf-8')

pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별', 
                          pop_Seoul.columns[1]:'인구수',
                          pop_Seoul.columns[2]:'한국인',
                          pop_Seoul.columns[3]:'외국인',
                          pop_Seoul.columns[4]:'고령자'} , inplace=True )

print(pop_Seoul.head())

# 기준점으로 부터 역순으로 정렬하기 

print(CCTV_Seoul.sort_values(by='소계' , ascending=False))

CCTV_Seoul['최근증가율'] = ( (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전']  ) *100
print(CCTV_Seoul.head())

print(CCTV_Seoul.sort_values(by='최근증가율' , ascending=False))

# 열 삭제
print(pop_Seoul.drop([0] , inplace=True))

# 결측값 찾기 1
print(pop_Seoul['구별'].unique())

# 결측값 찾기 2
print(pop_Seoul[ pop_Seoul['구별'].isnull() ] )

pop_Seoul['외국인비율'] = (pop_Seoul['외국인']/ pop_Seoul['인구수'])*100

pop_Seoul['고령자비율'] = (pop_Seoul['고령자']/ pop_Seoul['인구수'])*100

######################################################################################################33

# 두 데이터 프레임 합치기
data_result = pd.merge(CCTV_Seoul , pop_Seoul , on = '구별')

# 열 삭제
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

# 새로운 인덱스 지정
data_result.set_index('구별' , inplace=True)