'''
파이썬에서 mariadb를 접속하고, 쿼리수행
1. 접속,해제
2. 쿼리 수행 : 쿼리(Query)는 DataBase를 조작하는 언어
'''
import pymysql as my

try: 
    # DB 오픈
    conn = my.connect(host='127.0.0.1',
            user='root',
            password='1324098',      ## 잘됬는지 보려면 비번하나 틀리게 해서 구동해보기 
            db='pythondb',
            charset='utf8')
    print('연결 성공')
    ####################################################################
 
    # 쿼리 수행 절차
    # 1. 커서 획득
    cursor = conn.cursor()
    # 2. SQL 준비
    sql = '''
        select
            *
        from
            users
        where
            uid='1' and upw='1'
        '''

    # 3. 쿼리 수행
    cursor.execute( sql )
    # 4. select -> 결과 집합이 리턴됨 -> 결과 패치라는 과정으로 값을 얻어야 함
    rows = cursor.fetchall()
    print(rows)

    for row in rows:
        print( row[3])        ## 인덱스의 문제는 순서가 바뀌면 답이 없음

   ####################################################################
    # DB 닫기 
    conn.close()
    print('닫기 성공')
except Exception as e:
    print(e)