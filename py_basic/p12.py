# 파이썬 기초 순서

'''
1. 단일 데이터 관련
- 수치형(정수,부동소수,8~10~16진수)
- 문자열("",'')
'''
print('='*20)
# 수치형 값 변수에 담기
a = 10 
print(a)

# 파이썬은 문자의 끝에 아무것도 쓰지 않는다 ( 타 언어는 ; 를 사용)
# 예외적으로 사용할때는 여러문자를 한줄에 표현할때 이다.
# a라는 변수에 10을 담아라 -> 10은 객체다 -> a라는 변수는 10이라는 객체의 주소를 가르키고 있다

a= 1.1
print(a , type(a))
a= '점심시간'
print(a, type(a))
## 타입추론으로 타입을 결정한다. type(a)!! 
## java 나 C++ 은 int a = 10 ; 이런식으로 코드를 쳐야한다.

# 변수명 : 알파벳, _ , 숫자로 시작할 경우와 특수문자는 안됨
## 통상적으로 단어를 이여서 사용할땐 이어지는 글자를 대문자로 작성해주는게 편하다
## 관습적으로 첫글자는 소문자로 쓴다.
##           상수의 경우는 대문자로 사용한다.

userName = 'Imjongun'   ## 변수지정 (문자열)
print(userName)

PI = 3.142482728    ## 상수
print(PI)

# 수치형 : 숫자로 정의된 자료형
# 정수 : 1, -1 , 0
# 실수 : 1.1 , -1.1
# 8진수 : 0o12 -> 0o
# 10진수 : 255
# 16진수 : 0xFF (0~9 , A(=10) ~ F(=15) ) 

print("="*20)
## 정수값 
a = 1238
print(a)

## 실수값
a= 1.1
print(a)
a= -1.1
print(a, type(a))

a = 0xFF
print(a)

print("="*20)
# 기본연산확인
a=10
b=5
c = a+b
print(c)
print(a/b)
print(a*b)

# 나머지 획득
print(a%b)

# 제곱
print( 2**3)

# 몫
print(7//4)

# 괄호치기
print("-"*20)
print((1+2+3)*5)

## 실습 a=90 ,b=86 , c=100 의 평균을 출력
a=90
b=86
c=100
print((a+b+c)/3)