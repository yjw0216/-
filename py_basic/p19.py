# 함수 : function 
# 함수를 사용하는 이유는 반복작업을 해소해 생산성이 높아짐 / 개발속도 향상 / 재사용성 높아짐

a = 1 
b = 2
c = a+b
print(c)

# def 함수명(인자) :  ... 인자 생략가능
#     함수 내부에서 할 일 기술
#     return 결과값 ... 생략가능

def sum( x , y ) :
    return x + y 

print(sum(1,2) , sum(4,56) )

# 가변 인자 (인자: arguments or params)   *args 인자가 몇개인지 모른당
def sum2( *args ) :
    # 전달된 인자가 모두 정수값이라면
    # 인자의 총합을 구해서 리턴하시오
    print(type(args))
    sum = 0
    for n in args :
        print(n)
        sum += n    # sum = sum + n 
    return sum

print(sum2(1,2,3,4))
    
# 주어진 리스트의 누적곱을 구하시오
data = [1,2,3,4]
def mul ( input ) : 
    # 중간 중간 계산값을 담고 있을 변수
    tmp = 1
    for n in input : 
        tmp = tmp* n
        print(tmp)
    return tmp 
print( '누적곱의 값 ' , mul(data))

# 주어진 리스트의 모든 멤버의 누적합,누적곱을 구해서 리턴하시오
# 함수의 리턴값이 두개다 .

def mix( list ) : 
    s = 0 # 누적합의 임시변수
    m = 1 # 누적곱의 임시변수
    for n in list :
        s += n
        m *= n  ## 이 표현 중요하므로 알아두기 
    return( s, m )
print( mix(data) , type(mix(data)) ) 
        
## 추가적으로
t_sum , t_mul = mix(data)
print('t_sum=%s , t_mul=%s' %(t_sum,t_mul))



## 딕셔너리 표현으로
def mix2( list ) : 
    s = 0 # 누적합의 임시변수
    m = 1 # 누적곱의 임시변수
    for n in list :
        s += n
        m *= n 
    return{'t_sum':s , 't_mul':m}
nRtn = mix2(data)
print ('합', nRtn['t_sum'])
print ('곱', nRtn['t_mul'])

# 문자열을 입력받아서 공백을 제거하고 리턴해주는 함수 만들기

def say( input ) :
    input = input.strip()
    return input
print(say('    아녕      키키     '))


'''
함수 카테고리
1. 사용자 정의 함수 : 개발자가 만든 함수 
2. 내장 함수 : type() , len() ...
3. 멤버 함수 : random.randint() , 'helloworld'.strip()   등  .으로 쓰이는 주인이있는 함수
'''

### return이 없는 함수 

isTest = True
def log( msg ) : 
    if isTest :     
        print('-'*45)
        print(msg)
        print('-'*45)

log("Hello World!")

## 함수에 초기값(default)을 부여하여 활용
def person( name , age, weight=80) : 
    log('이름은 %s이고 나이는 %s살이며 몸무게는 %s이다' % (name,age,weight))

print(person('임종언',25,70))
print(person('김미라',160))