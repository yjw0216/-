# d1_8.py 모듈을 가져와서 로그인 처리를 하겠다

from d1_8 import loginSql

# 아이디,비번을 인자로 세팅
user_id = '1'
user_pw = '1'
rows = loginSql( uid=user_id , upw=user_pw )
if rows: ## [{'id':1 ...}]
    print('회원입니다 XD')
else:
    if rows == None:
        print('시스템 오류(내부오류)')
    else:  ## () or []
        print('회원이 아닙니다 :( ')

