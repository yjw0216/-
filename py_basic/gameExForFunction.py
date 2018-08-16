# 절차적 + 함수 지향적 프로그래밍

import random

def inputAndtrim( promptStr = '입력하세요' ) :    ## 기본값 부여한 것 
    return input(promptStr).strip()

def mmm_gamestart():
    while True:
        gameTitle = inputAndtrim("게임 제목을 입력하시오")
        if len(gameTitle) > 28:
            print('''입력하신 "%s" 게임 제목은 최대 28자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요.. ''' % (gameTitle, len(gameTitle)) )
        elif not gameTitle:
            print('아무것도 입력하지 않았습니다. 다시!!\n')
        else:
            break
    return gameTitle      ### 아래 main함수에서 gameTitle이 지역변수이기때문에 while문에서 빼내준 것 

def mmm_gameTitleDisplay(gameTitle,icon= '=') :
    introComment = '''
==============================
= {0:^26} =
=           v1.0.0           =
==============================
'''.format(gameTitle)
    print( introComment.strip() .replace('=',icon) ) ## replace는 문자열 멤버함수로 특정 문자열을 대체

def mmm_userName( prompt ) :
    nameCheck = True
    while nameCheck:
        g_name = inputAndtrim( prompt )
        if not g_name: 
          print('이름이 입력되지 않았습니다. 다시~')
          continue
        nameCheck = False
    return g_name



def mmm_gameIntro() :
    game_rule = ''' 본 게임은 ... '''
    print( game_rule )
def mmm_gameInit() :
    # 게임변수 초기화
    comp_value = None
    tryCount = 0
    return comp_value , tryCount
def mmm_gamePlaying(g_name1,comp_value1,tryCount1) :
    # 구동에 필요한 값을 전달받아서 내부 변수에 초기화 
    # >> 절차식으로 만든걸 함수지향적으로 잘라서 쓰다보니 변수간 연속성이 끊어져서 발생한 문제이다.
    g_name = g_name1
    comp_value = comp_value1
    tryCount = tryCount1                #### 이름만 같은 변수를 같게 만들어 주는 과정
    while True:
        # 사용자로부터 수치값을 입력받는다
        while True:
            g_value = inputAndtrim('0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요')
            if not g_value:# 공백을 넣으면
                print('값을 정확하기 입력하세요')
                continue
            elif g_value.isalpha() and not g_value.isdecimal():
                print('숫자가 아닙니다')
                continue
            g_value = int(g_value)
            if  0 > g_value or g_value >= 100:
                print('값이 범위를 넘어었습니다. 0~99 사이로 다시 입력')
                continue
            break

       
        if  comp_value == None:
            comp_value = random.randint(0, 99)

      
        tryCount += 1
        if g_value > comp_value:
            print( 'AI값보다 큽니다' )
        elif g_value < comp_value:
            print( 'AI값보다 작습니다' )
        else:# 정답
            print('''
            정답입니다. 게이머:{0}, AI:{1}
            {name}님의 총 시도 횟수는 {count} 입니다.
            획득 점수는 {point}입니다.
            '''.format(g_value, comp_value, name=(g_name), count=(tryCount), point=(100-tryCount*10) ))
            break



def mmm_gameAgain() :
    while True:
        res = input('다시 게임을 할까요?(yes/no)').strip().upper()
        # yes : Yes, YES, yES => 대문자로만 혹은 소문자로만 체크
        if res == 'YES':
            # 86라인 반복문 빠져나가기
            # break
            isGamePlaying = True
            break
        # no
        elif res == 'NO':
            # 전체 게임 빠져나가기 30라인
            isGamePlaying = False
            # 86라인 반복문 빠져나가기
            break
        # 이도 저도 아닐때
        else:
            print('정확하게 (yes/no)로 입력하세요')
    return isGamePlaying



def mmm_gameEnd() :
    print('game over !! bye bye~')
    


def main():
    # 프로그램 시작
    print('*'*45)
    print('함수 중심으로 구성된 게임 시작')
    print('*'*45)
    # 게임 제목 처리 함수
    gameTitle = mmm_gamestart()
    icons = ['*','t','♬','▒']
    mmm_gameTitleDisplay(gameTitle,icons[random.randint(0,3)])
    # 유저이름 받기
    g_name = mmm_userName('게이머의 이름을 입력 >> ')    ### 36의 g_name과 47의 g_name은 다른 변수이다!!!!

   ################################

    mmm_gameIntro()
   
    isGamePlaying = True
    while isGamePlaying:
        comp_value , tryCount = mmm_gameInit()
        mmm_gamePlaying(g_name , comp_value , tryCount)
        isGamePlaying = mmm_gameAgain()
   
    mmm_gameEnd()

# 게임 실행
main()




##########################################################################################################
##########################################################################################################

# '''
# step 6 : 
# -> 최종 숫자를 맞출때까지 시도 횟수를 기록하여 최종 맞추면
# -> 적절한 축하 코멘트 + 시도 회수를 보여주고 + 
#     100-시도회수*10점을 보상으로 부여하여 보여준다
# -> 다시 게임할것인지 물어보고 동의하면 다시 게임 시작
# '''