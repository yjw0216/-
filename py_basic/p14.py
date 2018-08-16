'''
2. 연속 데이터 관련 / 시퀀스 타입
- 리스트: [] , 순서( =인덱스 : 0~ , ~-1 )가 있다 , 값의 중복을 허용
- 딕셔너리 : {} , 순서가 없다 , 키와 값의 세트로 멤버가 구성됨 , 키는 고유하고 값은 중복되도 상관없음
- 튜플 : () , 순서가 있다, 값의 중복을 허용 , 값을 묶는다(본질적 의미)
- 집합 : set() --- 내장함수 , 중복제거 , 순서는 중요하지 않음 , ---set으로 중복제거하고 리스트를 가는 식으로 진행됨!

'''
print('-'*45)

nums = None # 타입이 없다 , 값이 없다 파이썬에선 Null 이 아니라 None이다
nums = []
print(nums,len(nums),type(nums))  #len : length
nums = list()
print(nums,len(nums),type(nums))  # 13번과 15번은 같은 표현 
                                  # 비어져있는 리스트 생성(= 비어있는 리스트 객체를 생생해 반환)

# 0보다크고 10보다 작은 정수중 홀수만 멤버인 리스트를 생성하기
nums = [1,3,5,7,9]
print(nums,len(nums), type(nums))
anis = ['dog','cat','bird']
print(anis,len(anis), type(anis))
mix = [1,2,3,'dog','cat']  ## 리스트의 멤버들의 타입이 달라도 되는가 ?
print(mix,len(mix), type(mix)) ## 타입이 동일할 필요가 없다!!!
multiMatix = [1,2,3,['dog',10]] # 차원이 달라도 상관없는가 ? 
print(multiMatix,len(multiMatix), type(multiMatix))  ## 상관없다,멤버가 또 리스트가 되어도 상관없다.


print('-'*45)

# mix라는 리스트에서 3을 출력하시오 -- indexing & 파이썬은 0부터 시작 !! & 리스트는 순서가 있다
print(mix[2])
# multiMatix에서 dog를 출력하시오 -- 리스트안에 리스트의 멤버를 추출하기..
print(multiMatix[3][0]) ## multiMatix[3]자체를 또하나의 리스트로 이해하면 된다!!!


# 슬라이싱
nums = [1,3,5,7,9]
# nums 리스트에서 3,5,7만 멤버로 가진 리스트를 생성하시오
print('사본작업',nums[1:-1])

nums1 = list(nums[1:-1])
print(nums1)

## 값 바꾸기
print(nums)
nums[0] = 100
print(nums)

nums[1:-1] = (-1,-1,-1) ### nums[1:-1] = -1 이 안되는 이유는 -1이 연속적이지 않다 
                        ### 즉 슬라이싱된 리스트의 값을 대입하려면 연속값형태로 대입해야함
                        ### nums[1:-1] = '888' or 'hello' or 'he' 등은 가능하다!!
print(nums)


print('-'*45)

## 리스트 삭제
nums = [1,3,5,7,9]
print(nums)
del nums[0] # 인덱싱으로 삭제
print(nums)
del nums[:2] # 슬라이싱으로 삭제
print(nums)
nums.remove(7)  ## remove는 순서가 아니라 특정값을 인자로 가짐
print(nums)
nums.clear()
print(nums)

## 추가 와 정렬
nums.append(100)  ## 추가
print(nums)
nums = [4,2,34,23,5,6,45,47,3,4,5,6,3,87,4357,123,53234]

nums.sort()     ## 정렬
print(nums)
# 원본은 훼손하지 않고 오름차순으로 정렬한 3번째 값을 출력하기
nums.sort() ### nums에 직접 sort를 가하는 것 자체가 원본을 훼손하는것이다 ! 새로운 사본을 만들어야 함
print(nums[2])   
# ++
nums2 = nums[:]
nums[:].sort()
print(nums2[2])

## 연속 데이터(컬렉션,시퀀스데이터), 여러개 데이터를 하나의 이름(변수명)으로 관리하고
## 프로그램을 좀 더 편하게 구성하기 위해서 나온 방식
n=[1,3,5,7,9]
print(n[0],n[1],n[2],n[3],n[4])


print('-'*45)

'''
연속형 데이터
- 딕셔너리 : {} , 순서가 없다 , 키와 값의 세트로 멤버가 구성됨 , 키는 고유하고 값은 중복되도 상관없음
'''
## {키:값 , 키:값 , 키:값 ...}
dic = {}
print(dic,len(dic),type(dic))
# B반의 멤버를 가진 딕셔너리를 생성하시오
dic = {'name' : '홍길동A' ,'name' : '홍길동B'} ### 키가 고유하지 않다 !! ERROR !!
dic = {'name' : '홍길동A', 'age' : 100 , } ### 딕셔너리는 키를 통해 값의 본질,형태,의미를 이해할 수 있다.
                                          ### DB와 관련지어 생각해보면 편하다 !
print(dic,len(dic),type(dic))

# 딕셔너리의 인덱싱 -- 홍길동을 출력하시오
print(dic['name'])   ### 딕셔너리는 인덱싱을 할때 순서가 없으므로 Key를 통해 인덱싱을 할 수 있다.
# 요소 추가
dic[2] = 'hi'
print(dic)  ### 키가 반드시 문자열만 되는 것은 아니다(= 타입 제한이 없다 ) + 2를 순서가 아닌 Key로 해석해야한다!!!!!
            ### 딕셔너리 인덱싱에서 숫자는 순서의 숫자아니라 키의 이름이다.

print(dic.keys())  ### 딕셔너리의 키를 뽑아라 + 그걸 리스트로 보여줌
print(dic.values()) ### 딕셔너리의 값만 뽑아라

# 해당 키가 있는 지 확인하는 법 (딕셔너리에)
print( 'name' in dic)


print('-'*45)
'''
연속형 데이터
- 튜플(tuple) : () , 순서가 있다, 값의 중복을 허용 , 값을 묶는다(본질적 의미)
- 튜플의 멤버가 1개일 경우 (멤버1) 이 아니라 (멤버1,) 이런식으로 해야한다!!!!
- 함수 내부에서 여러개의 값이 리턴될때 많이 활용한다!
'''

tu = ()
print(tu,len(tu),type(tu))
a = (1)
print(a,type(a))   ## 결과값이 int
a= (1,)
print(a,type(a))   ## 결과값이 tuple

# tuple의 특징은 값의 변화/삭제/변경이 불가하다 -> immutable --- 값을 묶는데 의미가 있음

tu = (1,2,3,4)
print(tu[0])   # 튜플의 인덱싱
print(tu[:2])  # 튜플의 슬라이싱
a = (5,6,7,8)
print(a + tu)  # 튜플이나 리스트의 합은 2개가 이어져서 하나의 튜플이나 리스트가 된다!



print('-'*45)
'''
연속형 데이터
- 집합 : set() --- 내장함수 , 중복제거 , 순서는 중요하지 않음 , ---set으로 중복제거하고 리스트를 가는 식으로 진행됨!
'''

a= 'helloworld'
b= set(a)
print(b)  ## a문자열의 중복된 문자 제거하고 나옴 
c= list(b)
c.sort()
print(c)  ## 원본 데이터 > set()으로 중복제거 > 특정 시퀀스타입으로 변화 > 다음작업 처리


### 합집합/교집합/차집합
a= set( [1,3,5,7,9,2,6,5])
b= set( [2,4,6,8,1,5,4,1])
print(a,b)
# 합집합
print(a.union(b))
# 교집합
print(a.intersection(b))
# 차집합 : 방향이 중요 a-b ? b-a ?
print(a.difference(b))
print(b.difference(a))
