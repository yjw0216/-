# # 절차적 프로그래밍
# #print(len("Enjoy number matching game")+2)
# # step 0
# # 아무것도 않으면 모라하고 다시 입력 받으세요
# while True:
#     gameTitle = input("게임 제목을 입력하시오").strip()
#     # 입력된 게임 제목의 길이가  28보다 크면 다시 입력
#     if len(gameTitle) > 28:
#         print('''
#         입력하신 "%s" 게임 제목은 최대 28자(현재 %s자 입력)
#         를 초과할수 없습니다. 다시 입력하세요.. '''
#         % (gameTitle, len(gameTitle)) )
#     #elif not gameTitle:
#     elif len(gameTitle)==0:
#         print('아무것도 입력하지 않았습니다. 다시!!\n')
#     else:
#         break
# #print( gameTitle )
# # step 1-1 : 여러줄 문자열, 포멧팅, 치환식
# introComment = '''
# ==============================
# = {0:^26} =
# =           v1.0.0           =
# ==============================
# '''.format(gameTitle)
# print( introComment.strip() )
# # step 2-2 : 게이머의 이름을 입력받는다?
# # 입력하지 않았을 경우에만 모라하고, 그외는 ok
# #while True:
# nameCheck = True
# while nameCheck:
#     g_name = input('게이머의 이름을 입력하세요?').strip()
#     # not => 부정한다 => 타언어 !
#     if not g_name: 
#         # 이름을 입력않하면 ""=> 조건식에서는 False =>
#         # False 부정하면 True
#         # 이름을 입력하지 않았다고 판단
#         print('이름이 입력되지 않았습니다. 다시~')
#         # continue:를 만나면 다시 반복 조건식으로 이동
#         continue
#     #break
#     nameCheck = False

# step 3 : 게임 방식 간단히 설명하고, 0 ~ 99까지 값을 
# 입력하라고 코멘트 -> 아무것도 않넣으면 모라하고, 0이하 99이상
# 넣어도 모라하고
game_rule = '''
본 게임음 ...
'''
print( game_rule )
g_value = input('0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요').strip()
if not g_value:# 공백을 넣으면
    print('값을 정확하기 입력하세요')
elif g_value.isalpha() and not g_value.isdecimal():
    print('숫자가 아닙니다')
else:
    print('ok')
# 정수변환
g_value = int(g_value)
# 0보다크고(0포함), 100보다 작고
#if g_value >= 0 and g_value < 100:
if  0 > g_value or g_value >= 100:
    print('값이 범위를 넘어었습니다. 0~99 사이로 다시 입력')
else:
    print('ok')




# step 4 : AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99

# step 5 : AI의 숫자보다 유저가 입력한 숫자가 크거나 
#          작으면 코멘트를 해준다 => 맞출때까지 반복

'''
 step 6 : 
 -> 최종 숫자를 맞출때까지 시도 횟수를 기록하여 최종 맞추면
 -> 적절한 축하 코멘트 + 시도 회수를 보여주고 + 
    100-시도회수*10점을 보상으로 부여하여 보여준다
 -> 다시 게임할것인지 물어보고 동의하면 다시 게임 시작
'''