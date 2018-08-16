'''
게임 제작
- 조건문,반복문,식(비교식...) 확인
- 0~99까지에 숫자를 맞추는 게임 
- step0 : "게임의 이름을 입력하시오"라는 코멘트와 아래와 같이 출력
- step1 : 게임시작하면 코멘트 안내하고 입력을 유도
===================================
=   Enjoy Number Matching Game    =         <- 게임 제목이 입력됨 (중앙정렬)
=             v1.0.0              =
===================================
게이머의 이름을 입력하세요?


- 유저는 게임을 시작할때 이름을 넣고 플레이를 시작하며 숫자를 입력하여 맞추기를 시작한다.
- 이름을 필수기입하도록 유도 / 숫자 입력 오류시 코멘트 재입력 유도
- 게임이 시작하면 AI가 숫자를 하나 생성
- AI 숫자보다 유저 의 입력숫자가 크거가 작으면 코멘트를 함
- 최종 숫자를 맞출때 까지 시도 횟루를 기록하여 최종 맞추면 시도회수 + 축하코멘트 + 100-시도회수*10점을 반환
- 다시 게임여부를 확인 
'''
## 여기서 게임 제목의 글자수 제한을 넣어야한다 (텍스트 구조가 깨지니까)
# 조건문 
## 파이썬에서 코드 블럭은 들여쓰기를 하면 된다 :로 하면 자동으로 들여쓰기 됨

## userName= input('게이머의 이름을 입력하세요?') # input은 콘솔에서 사용자의 입력을 대기하다가 사용자가 
                                                #입력후 엔터치면 반환하는 함수


while True :   
    gameTitle = input('게임 제목을 입력하세요').strip()     ## 여기서 strip은 스페이스만 꾹 눌러도 공백으로 봐야하는데 그냥 읽어버리니까 strip으로 걸러주는 것
    if   len(gameTitle) > 33 :
        print('입력하신 "%s"의 길이는 최대 35자( 현재 : %d)를 초과할 수 없습니다.' % (gameTitle,len(gameTitle)))
    elif not gameTitle :
        print('입력 값이 없습니다.\n>>')
    else :
        break

print( '''
===================================
={0:^33}=
=             v1.0.0              =
===================================
''' .format(gameTitle))


### step 2-2 : 게이머의 이름을 입력받을때 입력하지 않을경우만 제한을 두고 나머지는 통과

while True : 
    userName= input('게이머의 이름을 입력하세요?').strip()
    if not userName :   ## 이름을 입력안하면 "" 가 됨 즉 False임 // 그걸 부정하면 참이 됨 (이건 if 문을 위해)
        print('입력값이 없습니다 \n >>>')
        continue ## if문을 반복하는 것
    break

### step 3 : 게임 방식 간단히 설명하고 0~99까지 값을 입력하라고 코멘트 // 아무것도 안넣거나 0이하 99이상을 넣어도 코멘트

game_rule = '''
본 게임은 ...
'''
print(game_rule)
while True :
    userNum = input('0~99의 정수를 입력하세요 ').strip()
    if not userNum :
        print ('값을 입력하세요.')
        continue
    elif userNum.isalpha() and not userNum.isdecimal() : 
        print('숫자가 아닙니다.')
        continue

    # 정수 변환 
    userNum = int(userNum)
    if 0 > userNum  or userNum >= 100 :
        print('값이 범위를 넘어있습니다.')
        continue
    break

### step 4 : AI가 숫자 하나를 랜덤으로 생성한다.

# import random as r  ## import는 모듈 가져오기의 표현 // as r 은 일종의 단축키화,매크로화 시킨것
# for n in range(100) :     # randint(x,y) : x <= r <= y
#     print(r.randint(0,2))

import random as r
aiNum = r.randint(0,99)

### step 5 : AI의 숫자보다 크거나 작으면 코멘트를 입력한다.-> 맞출때까지 반복함

while True :
    while True :
        userNum = input('0~99의 정수를 입력하세요 ').strip()
        if not userNum :
            print ('값을 입력하세요.')
            continue
        elif userNum.isalpha() and not userNum.isdecimal() : 
            print('숫자가 아닙니다.')
            continue

        # 정수 변환 
        userNum = int(userNum)
        if 0 > userNum  or userNum >= 100 :
            print('값이 범위를 넘어있습니다.')
            continue
        break

### step 6 : 최종 숫자를 맞출때 까지 시도 횟루를 기록하여 최종 맞추면 시도회수 + 축하코멘트 + 100-시도회수*10점을 반환 / 다시 게임여부를 확인 