import random


class Lotto:
    num = []


    for i in range(1,7):
        i = random.randint(1,45)
        num.append(i)

    num.sort()

    def excp( x ):
        a = set(x)
        b = list(a)
        return b


    if len(excp(num)) == 6:
        print( '성공 ! ')
    else:
        print('실패 :  중복 값이 있습니다 ')

    def __init__(self):
        pass

obj = Lotto()
print('번호는 : ' , obj.num)

if 100<= sum(obj.num)<=170:
    print('난수 조합을 신뢰할 수 있습니다.')
else:
    print('Warning : 신뢰 구간을 벗어난 조합입니다.')