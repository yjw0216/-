'''
파이썬에서 mariadb를 접속하고, 쿼리수행
1. 접속,해제


2. 쿼리 수행 : 쿼리(Query)는 DataBase를 조작하는 언어

3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 테이블 칼럼의 위치가 변경되거나,쿼리문이 조정되면
   순서가 바뀌게 되면 소스를 수정해야 하는 상황이 벌어진다.
   >> 해결방안 >> 칼람이 따라와서 딕셔너리 형태로 가면 순서의 의미를 안받게 된다 !

4. 쿼리문에 인자를 전달하여 수행하기 >> 일반화 기본 작업  Line 37 참고

5. with문을 이용하여 커서 닫기를 자동으로 처리

6. 함수화를 통해서 누구나,여러번 호출만으로 이 기능을 사용하게 처리 

7. 함수에 return값을 부여하여 쿼리결과를 돌려주게 처리

8. 모듈화를 위한 처리  (p1.8.py 인걸 p1_8.py 로 바꿔줌) >> 이름에 . 2개 면 오류날 가능성 있음

'''
import pymysql as my


# >>>>> 고정값을 변수로 바꾸는게 일반화 과정이다
 
def loginSql(uid,upw):
    rows = None    #>>>>>>> cursor.fetchall을 rows에 받기 때문에 초반에는 값이 없다로 설정 !
    try: 
        # DB 오픈
        conn = my.connect(host='127.0.0.1',
                user='root',
                password='1324098',      ## 잘됬는지 보려면 비번하나 틀리게 해서 구동해보기 
                db='pythondb',
                charset='utf8',
                cursorclass=my.cursors.DictCursor)  
        ####################################################################
    
        # 쿼리 수행 절차
        # 1. 커서 획득 : 

        with conn.cursor() as cursor :  
            # 2. SQL 준비
            sql = '''
                select
                    *
                from
                    users
                where
                    uid=%s and upw=%s;
                '''

            # 3. 쿼리 수행
            cursor.execute( sql,( uid , upw ) )  
            # 4. select -> 결과 집합이 리턴됨 -> 결과 패치라는 과정으로 값을 얻어야 함
            rows = cursor.fetchall()
            # print(rows)            >>52~55 임시 막음

            # for row in rows:
            #     print( row['name'])


            # 5. 커서 닫기  >>>>>>>>>>>  with문 사용으로 자동으로 처리 됨 !
            # cursor.close()
        ####################################################################
            # DB 닫기 
            conn.close()
        print('닫기 성공')
    except Exception as e:
        print(e)
    # else
    finally:
        return rows 


## 테스트 코드는 if문 으로 처리하기 : 모듈화 중 불필요한 코드 이동!
if __name__=='__main__':
    results = loginSql('admin','2')
    print(results)         ## >>>> 모듈로 땡겨쓸때 (테스트 코드가) 작동 안하게 하려고 if문을 걸어주는 것 