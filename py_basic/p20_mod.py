# 
# 
############################## 클래스 , 객체 #############################################################
# 객체 : Object << 모든 클래스의 슈퍼 클래스 (파이썬,자바,자바스크립트...)
# 모든 클래스(+ 내가 만드는 클래스)의 기원은 Object이다
# 객체의 개념 => 이 세상에 존재하는 모든 사물(유형),생각(무형)
# ㄴ> 프로그램에서 구현하고자 한다 -> 이때 필요한 도구, 형상화 할 수 있는 , 문법적으로 나타내려는 것
#  -> Class!! 
#  class의 인스턴스(instance)가 객체이다 -> 메모리에 임시로 생기는 것
# 
#  객체 : 속성과 행동이라는 두가지 특징을 가짐
#  ---  1. 속성 =특성 ex. 사람의 속성/특징 : 눈,코,입,귀,팔2개 ...
#               class의 구성원 : 멤버 변수
#  
#  ---  2. 행동 =액션 => 메소드/함수 ex. 밥을 먹는다, 잠을 잔다, 걷는다 , 말한다 ...
#               class의 구성원 : 멤버 함수 
#
# 객체 지향 프로그램 (OOP) : Object Orient Program 

###########################################################################################################

# class 문법
# 사람이라는 유형의 객체를 파이썬으로 구현해보자 -> class를 사용하여!
# 클래스의 이름은 첫글자 대문자로 이어지는 글자는 소문자로
# 클래스의 모든 함수의 첫번째 인자는 self 이다.
# self는 자기 자신 class를 가르키는 키워드(예약어) <-> 타 언어에선 this 등으로 표현
# 함수의 첫번째 인자는 self인데 실제 사용시에는 별도의 인자로 보지 않는다(= 사실상 없다고 보는 것 ! )

class Person :
  
    '''
    멤버 변수  : 객체의 속성
    '''
    name = None
    age = 0 # None도 가능
    '''
    멤버 함수  : 객체의 행동(액션)
    '''
    def eat(self):
        print('eat() call')
    def sleeping(self):
        print('sleeping() call')

    '''
    생성자(constructor) 함수: 객체(class의 인스턴스)를 생성하는 역할   
                           : 메모리에 공간을 만들고 주소를 반환하는 역할
                           : 메모리에 공간을 만들고 주소 참조값을 반환하고 참조 카운트를 증가시키는 역할 
                           : # 틀이 정해져 있다 #
    '''                     
    def __init__(self):
        print('생성자 call')
    

# 실제 사용
# 클래스는 생성자를 호출하여 객체를 생성하는데 그 방법은 클래스명() 이다.
# 생성자() >> 클래스명(인자값: 생성자에서 정의한대로 배치함)
obj = Person()
# 멤버 변수나 멤버 함수를 사용하는 방법
# 객체명.멤버변수 , 객체명.멤버함수
print(obj.name,obj.age)
obj.sleeping()



## class 심화

class Person2 :
    name = None
    age = 0 
    def eat(self):
        print('eat() call')
    def sleeping(self):
        print('sleeping() call')          
    # 생성자의 주 업무 중 하나는 멤버 변수 초기화에 있다
    def __init__(self,name,age):
        # 클래스 내부에서 멤버들을 사용할 경우 무조건 self. 을 붙인다 (그래야 구분이 가능 함)
        self.name = name
        self.age = age
        print('생성자 call')
    
p1 = Person2('임종언',25)
p2 = Person2('김미라',22)
# 이름을 출력하시오

print(p1.name , p2.name)

#########################################################################################################
# class Xman을 정의해보기
# Xman은 Person2를 상속받는다 -> Xman은 Person2이다 (O) (= is a )
# Person2는 Xman이다 (X) : Person2는 Xman을 자식으로 가진다 (O)  (= has a )


# class 클래스명(부모명):  -> 상속을 표현하는 방법
# 부모가 Object인 경우 생략가능 -> class Person2(Object) or class Person2
# Object -> Person2 -> Xman 의 순서
# 상속을 받으면 부모의 모든 것을 모두 사용 할 수 있다.
# 자식을 별도로 변수,함수를 추가할 수 있다.
# 자식은 물려받은 부모의 것을 재 정의(업그레이드) 할 수 있다.
##########################################################################################################

class Xman(Person2):
    abil = 100
    def speed(self):
        print('시속200km로 달린다')
    def eat(self):
        print('밥을 1초만에 먹는다')   # 부모로부터 받은 함수를 재정의하여 사용
    def __init__(self, name,age):
        self.name=name
        self.age=age
    

xman = Xman('임종언',25)
print(xman.name , xman.abil )
xman.eat()



print(__name__)  ## 결과값이 __ㅡmain__ 으로 나오기 때문에 구동되었다는 말

if __name__=='__main__':   ##name이 main이 아니면
    # p20_mod.py가 실행 메인코드가 되서 구동될때
    # 모듈로 사용되면 이 부분은 수행되지 않는다.
    # 일반적으로는 테스트코드 사용(모듈용도로만 사용되면)
    # if 문을 걸어주지 않으면 p21.py에서 다 구동되어버림
    p1 = Person2('임종언',25)
    p2 = Person2('김미라',22)

    print(p1.name , p2.name)
    xman = Xman('임종언',25)
    print(xman.name , xman.abil )
    xman.eat()