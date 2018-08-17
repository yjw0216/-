import random

# a = range(1,46)
# b = random.sample(a,6)
# c = sorted(b)

cnt = 0 # 게임횟수

while cnt <5 :
    lotto = sorted( random.sample(range(1,46),6))
    if 100 <= sum(lotto) <= 170 :
        print(lotto)
        cnt = cnt + 1



'''
생각의 과정( 논리적 사고 방식 / 문제해결능력)

1. 1부터 45의 숫자가 필요함 (range)
2. 6개의 숫자가 필요함 (sample)
3. 정렬이 필요함 (sorted)
4. 합계가 필요 (100~170인 조건 >> if 문 필요)
5. 5 게임 ( while )
'''