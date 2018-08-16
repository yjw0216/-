
## if 문 학습

money = int(input(' 커피값은 얼마 입니까 ?  : '))   ## 문자열을 정수값으로 변환!!

if money > 3500 :
    print('비싸다')
elif money == 3500 :
    print('적당하다')
else : 
    print('싸다')


### 반복문 학습
# for -> 반복횟수 : 지정된 횟수 , 정해진 횟수
# while -> 반복횟수 : 0 ~ 무한대
a= [1,2,3,4,5]

## 한개씩 멤버를 제거하면서 출력하시오
# 조건식 : 언제까지? -> 멤버가 없을때까지 -> while 문 !!

while len(a) > 0 :
    print(a.pop())

a= [1,2,3,4,5]
while a :
    print(a.pop())

## 반복문이 정상적으로 다 돌아서 끝났음을 아는 방법 ( 파이썬에만 있는 구문 )

a= [1,2,3,4,5]
while a :
    print(a.pop())
else :
    print('정상적으로 루프를 다 돌았다.')

### a의 개수가 2개가 되면 종료

a= [1,2,3,4,5]
while a :
    print(a.pop())
    print('-------')
    if len(a) == 2  :
        # 루프 중단
        break # while문을 빠져 나감 
else :
    print('정상적으로 루프를 다 돌았다.')
