
while True :   
    gameTitle = input('게임 제목을 입력하세요')
    if   len(gameTitle) > 33 :
        print('입력하신 "%s"의 길이는 최대 35자( 현재 : %d)를 초과할 수 없습니다.' % (gameTitle,len(gameTitle)))
    else :
        break