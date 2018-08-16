'''
파이썬에서 mariadb를 접속하고, 쿼리수행
1. 접속,해제
'''
import pymysql as my

try: 
    # DB 오픈
    conn = my.connect(host='127.0.0.1',
            user='root',
            password='1324098',      ## 잘됬는지 보려면 비번하나 틀리게 해서 구동해보기 // try로 완전 죽는거 방지(빼고 해보기)
            db='pythondb',
            charset='utf8')
    print('연결 성공')
    # DB 닫기 
    conn.close()
    print('닫기 성공')
except Exception as e:
    print(e)