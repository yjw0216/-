'''
1. 단일 데이터 관련
- 문자열("",'')
'''
print("-"*40)
#문자열 표기법 
# "..." , '...'  , """...""" , '''...'''
# 1줄로 표현을 할 경우 : '...' , "..."
# 여러줄 표현 및 구조를 유지하는 문자열 : """...""", '''...''' , 주석#사용

### 파이썬의 문자열은 변경이 불가능 하다 
#새로이 조작을 해야하지 변경은 불가능하다


a='Hi'
print(a)

a= 'adcedf"KKK"ppiowd'
print(a)

a= "asdfasf'IMJONGUN'asdfsss"
print(a)

a = 'asdfsf\'IMJONGUN\'sdfsff'
print(a)   ### 정규표현식 활용

print("-"*40)
a= '''
dkfmlslsl
fkdmfmls
fkfkfkdkdk
fjffjfjfjfj
'''
print(a)

## 문자열 합치기 ( 파이썬이 편하네..)
a= '123'
b= '567'
print(a+b)

## 문자열 반복
print(a*30)

print("-"*40)
## 인덱싱   (대괄호 뒤에 순서를 적고 0부터 시작이다 !)
a= '1234442236'
print(a[1])   ## 결과값이 1이 아니라 2 이다 (왜냐면 0부터 시작이니까)

## 중요. 역방향으로 인덱싱하기 -> -1,-2,-3...
print(a[-1])

# 범위에 해당되는 데이터 획득 -> 슬라이싱
url = 'http://google.com/img/sdfkekemdmd.jpg'
# 변수[시작인덱스:끝인덱스]
print(a[1:8])
print(a[1:-4]) ## 정방향과 역방향을 동시에 사용가능하다!!!
print(url[:-5]) ## 처음부터 할꺼면 처음 자리 비워놓으면 된다
print(url[22:])
print(url[-10:]) ## 역방향을 앞부분에 쓸수도 있다!!
print(url[::2]) ## ::(스텝)의 의미는 숫자만큼 뛰어넘어 인덱싱하라 (2라면 홀수번째만 인덱싱하라)
print(a[::1])

## 포맷팅 : 어떤 데이터를 문자열과 결합하여 특정형태로 표현하는 방식
a=1
b=2
### x + y = z 라는 형태로 출력되게 문자열을 구성하시오
print('%d + %d = %d ' %  (a,b,a+b))
print('%d / %d = %f' %  (a,b,a/b))
## 출력하고자 하는 변수의 타입과 포멧팅의 표현이 일치하지않으면 부정확하게 나오거나 오류를 출력할수도 있다.

## 그냥 문자열로 받아버리기
print('%s / %s = %s' % (a,b,a/b))

###################################################
# % 표시는 요약형이고 정확한 표현식은 .format(~)이다.#
###################################################


## 인덱스로 포멧팅을 구성하고 싶다.
print('{0} / {1} = {2}' .format(a,b,a/b))
print('{1} / {2} = {0}' .format(a,b,a/b))
print('{0} / {1} = {result}' .format(a,b,result =(a/b)))  ## 인자에 이름을 부여하여 포멧팅하기


print("-"*45)
# 문자열 지원함수
a = '0123456789'
print('문자열의 특정 문자 개수?' , a.count('1'))     ## a에 1이 몇개있는지
print('문자열의 특정 문자 개수?' , a.count('-1'))   ## a에 -1이 몇개있는지

print(a.count('A') == 0)

## 조인기능
b= ','
print(b.join(a))

## 공백제거
a= '        mdfeiidmdmdmm  dkfmfmfoeodp          '
print(a)
print( '[%s]' % (a))  ## []는 그냥 시각적 도움을 위해 설정한것.의미없음.
### 왼쪽 공백제거
print( '[%s]' % a.lstrip() )
print( '[%s]' % a.rstrip() )
print( '[%s]' % a.strip() )


print("-"*45)
## 대소문자 변환 
a = 'abcdADWE멀티123!@#'
print(a)
print(a.lower() , a.upper())


## 포멧팅에서 자리칸 표현하기
### 20칸 자리에 문자열을 배치하기
print('[%20s]' % '12345')
print('[%-20s]' % '12345')
print('[%0.2f]' % 3.14756787654)
print('[%0.2f]' % 3.14111111111)  ## 반올림된다! 그렇기에 값의 변화가능성이 있다

print("-"*45)
## 나누기 <-> 조인
a= 'helloworld'
b= ','
c= b.join(a)
# , 를 구분자 라고 칭함
print(c)

print(c.split(','))   ### []가 쳐진것은 리스트의 형태 !!

print(url.split('/')[4])
print(url.count('/'))
print(url.split('/')[url.count('/')])  ### 코드의 일반화 과정

## 치환식 <- 포멧팅 + 치환식 + 자리수 : 인덱스로 포멧팅방식과 비슷
a= '123{0}456'.format('K')
print(a)
### 자리수 10개
a= '123{0:<10}456'.format('K')
print(a)
a= '123{0:>10}456'.format('K')
print(a)

## K를 가운데 넣고 11자리
a= '123{0:^11}456'.format('K')
print(a)
a= '123{0:*^11}456'.format('K')
print(a)