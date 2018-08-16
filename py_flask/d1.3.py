'''
파이썬에서 mariadb를 접속하고, 쿼리수행
1. 접속,해제
2. 쿼리 수행 : 쿼리(Query)는 DataBase를 조작하는 언어
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 테이블 칼럼의 위치가 변경되거나,쿼리문이 조정되면
   순서가 바뀌게 되면 소스를 수정해야 하는 상황이 벌어진다.
   >> 해결방안 >> 칼람이 따라와서 딕셔너리 형태로 가면 순서의 의미를 안받게 된다 !
'''
import pymysql as my

try: 
    # DB 오픈
    conn = my.connect(host='127.0.0.1',
            user='root',
            password='1324098',      ## 잘됬는지 보려면 비번하나 틀리게 해서 구동해보기 
            db='pythondb',
            charset='utf8',
            cursorclass=my.cursors.DictCursor)   # >>>>>>>>>>>>>>>>>>>>>>>>>1.2와 다른점 미리 할것이냐 후에 할 것이냐 의 차이이다!
    print('연결 성공')
    ####################################################################
 
    # 쿼리 수행 절차
    # 1. 커서 획득 : 
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
        print( row['name'])

   ####################################################################
    # DB 닫기 
    conn.close()
    print('닫기 성공')
except Exception as e:
    print(e)