# 반복문 (while , for )
a= [1,2,3,4,5]
# 리스트 a에서 멤버들을 하나씩 꺼내서 출력하시오

# 파이썬에선 for each 방식만 지원한다 (for문에서)
for item in a :
    print (item) 

# 튜플의 경우 데이터를 개별적으로 받을 수 있다.
a=[(1,2),(3,4),(5,6)]
for i,j in a :
    print(i,j)
for item in a :
    print(item)
for item in a :
    print(item[0], item[1])

## 연속수 -> range()
for n in range(1,11) :     # x이상 y미만이라는 범위 
    print(n)

print('-'*45)

'''
구구단 3단부터 7단까지 출력하시오
3 x 1 = 3
3 x 2 = 6
...
7 x 9 = 63
'''

for n in range(3,8) :
    for a in range(1,10) :
        print( '{0} x {1} = {2}' .format(n,a,n*a))


# 축약할 수 있다!!!
#똑같은 결과를 바로 리스트에 담기 
print(['{0} x {1} = {2}' .format(n,a,n*a) for n in range(3,8) for a in range(1,10)  ])