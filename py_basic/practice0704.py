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