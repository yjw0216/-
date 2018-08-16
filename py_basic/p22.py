

# 참조 카운트 : 객체 속성
import sys
a = 1 
print(a, type(a) , sys.getrefcount(1))

b = 1
print(b , type(b) , sys.getrefcount(1))     ## reference count : 참조수 세기
print( a is b)
del(a)

print(sys.getrefcount(1))
# print(a is b)    ### 오류나는게 정상임  #### 밑에 코드 검사하려고 잠시 막아놓은것 !!!

# 파이썬에서 존재하는 모든 요소는 객체이다.
# 파이썬에서 사용하는 것들 중에 예로 1,2,3 같은 것들도 객체이고 단지 참조를 통해서 해당 개체를 사용할 뿐이다.

from a.b.mod import A
obj = A()
print('객체A : ' , sys.getrefcount(A))
del(obj)
print('객체A : ' , sys.getrefcount(A))
obj2 = A()
print('객체A : ' , sys.getrefcount(A))


#### 핵심 : 파이썬에서 존재하는 모든 요소는 객체이다. ( 심지어 1,2,3 일지라도)