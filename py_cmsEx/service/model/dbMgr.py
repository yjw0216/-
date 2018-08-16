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

'''
pip install DBUtils

DBUtils의 풀링 기술을 이용하여 전체적으로 쿼리 처리 업그레이드 
'''

import pymysql as my
from DBUtils.PooledDB import PooledDB
#from service.model import PostModel

DB_URL         ='localhost'
DB_USER        ='root'
DB_PASSWORD    ='1324098'
DB_DATABASE    ='pythondb'
DB_CHARSET     ='utf8'
MAX_POOL       = 100  ## DB커넥션 연결 수 설정 (환경 세팅 시에)

class DBHelper:
    # 멤버 변수
    app = None
    ## 풀링객체 ( DB와 연결된 커넥션을 가지고 있는 객체 )
    connectionPool = None
    # 생성자
    def __init__(self,application=None):
        self.app = application   # 멤버변수를 클래스 내에서 부를땐 꼭 self. 을 붙여줘야 함 
        if self.app: ## Flask 객체가 존재하면  >> 환경변수에서 뽑아서 세팅
            DB_URL         = self.app.config['DB_URL']
            DB_USER        = self.app.config['DB_USER']
            DB_PASSWORD    = self.app.config['DB_PASSWORD']
            DB_DATABASE    = self.app.config['DB_DATABASE']
            DB_CHARSET     = self.app.config['DB_CHARSET']
            MAX_POOL       = self.app.config['MAX_POOL']
        
        self.initPool()
    #소멸자(<->생성자) / del 객체명
    def __del__(self):
        self.freePool
    # 멤버 함수
    # 커넥션 풀 생성
    def initPool(self):
        self.connectionPool = PooledDB(  creator=my,
                                    host=DB_URL,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    database=DB_DATABASE,
                                    autocommit=False,
                                    charset=DB_CHARSET,
                                    cursorclass=my.cursors.DictCursor,
                                    blocking=False,
                                    maxconnections=MAX_POOL
                                                                     ) 
    # 커넥션 풀 해제
    def freePool(self):
        ## DB와 연결된 모든 커넥션을 닫음
        self.connectionPool.close()
    # 개별 쿼리

    # 로그인 처리
    def loginSql(self,uid,upw):
        rows = None   
        try: 
            conn = self.connectionPool.connection() ##커넥션을 풀링객체에서 빌려온다 ! 
            ##### 쿼리 수행 ########################################################
            cursor = conn.cursor()  
            sql = '''
                select
                    *
                from
                    users
                where
                    uid=%s and upw=%s;
                '''
            cursor.execute( sql,( uid , upw ) )  
            rows = cursor.fetchone()
            cursor.close()
            ########################################################################
            # 풀링에 반납한다
            conn.close()
        except Exception as e:
            print(e)
        finally:
            return rows 

    # 검색 처리
    def searchSql(self,keyword):
        rows = None    #>>>>>>> cursor.fetchall을 rows에 받기 때문에 초반에는 값이 없다로 설정 ! // 변수를 받는 일종의 그릇 (비우기!)
        try: 

            conn = self.connectionPool.connection()
        
            # 쿼리 수행 절차
            # 1. 커서 획득 : 

            cursor = conn.cursor()
            # 2. SQL 준비
            sql = '''
                select
                    name,rank
                from
                    tbl_epl
                where
                    name like "%{0}%";              
                '''.format(keyword)                  ## 약식표현으로 하면 겹침 

            # 3. 쿼리 수행
            cursor.execute( sql )  
            # 4. select -> 결과 집합이 리턴됨 -> 결과 패치라는 과정으로 값을 얻어야 함
            rows = cursor.fetchall()
            cursor.close()
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
            rows = None
        return rows 
    
    # 팀 검색
    def selectTeamName(self,teamName):
        rows = None    
        try: 
            conn = self.connectionPool.connection()
        
            # 쿼리 수행 절차
            # 1. 커서 획득 : 

            cursor = conn.cursor()
                # 2. SQL 준비
            sql = '''
                select
                    *
                from
                    tbl_epl
                where
                    name = %s;              
                '''                  ## 약식표현으로 하면 겹침 

            # 3. 쿼리 수행
            cursor.execute( sql, (teamName) ) ## teamName이 튜플

            # 4. select -> 결과 집합이 리턴됨 -> 결과 패치라는 과정으로 값을 얻어야 함
            rows = cursor.fetchone()  ################################################################# 중요 one!
            cursor.close()
            # print(rows)            >>52~55 임시 막음                                 #### fetchone() :1개만 가져온다 -> 리스트의 형태 제외됨

            # for row in rows:
            #     print( row['name'])


            # 5. 커서 닫기  >>>>>>>>>>>  with문 사용으로 자동으로 처리 됨 !
            # cursor.close()
        ####################################################################
            # DB 닫기 
            conn.close()
            print('닫기 성공')
        except Exception as e:
            rows = None
        return rows 
    
    # 팀 정보 수정 (일단 총 경기수만 설정하는 함수 짜기)
    def updateTeamInfo(self,total,teamName):
        result = None    
        try: 
            conn = self.connectionPool.connection()
            cursor = conn.cursor()
            # 2. SQL 준비
            sql = '''
                update
                    tbl_epl
                set
                total = %s
                where
                    name = %s;              
                '''                   
            cursor.execute( sql, (total,teamName) ) 
            ## 커밋( DB에 실제 반영한다 )
            cursor.close()
            conn.commit()
            # 영향받은 row의 수로 설정
            result = conn.affected_rows()
            conn.close()
            print('닫기 성공')
        except Exception as e:
            result = None
        return result 
    
    # 모든 팀 가져오기 (정렬 기준 칼럼 , 정렬방식 , 시작페이지 , 한페이지의 양 을 인자로 )
    def selectAllEplList(self,stdCol='rank',order='asc',page=0,amt=5):    ## 추가로 인자에 기본값 설정
        rows = None    
        try: 
            conn = self.connectionPool.connection()

            cursor = conn.cursor() 
            sql = '''
                select
                    rank,name,winPoint,win
                from
                    tbl_epl
                order by %s %s
                limit %s , %s;          
                '''  % (stdCol,order,page,amt)
            cursor.execute( sql ) 
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            print('닫기 성공')
        except Exception as e:
            rows = None
        return rows 



    # 게시물 모두 가져오기 
    def selectAllBbs():
        pass


    # 게시물 등록
    def insertPost( self , pm ):
        result = None    
        try: 
            conn = self.connectionPool.connection()
            cursor = conn.cursor()
            # 2. SQL 준비
            sql = '''
                insert into tbl_bbs(title,content,`file`,writer,regdate)
                values(%s , %s , %s , %s ,now());
                '''                   
            cursor.execute( sql, ( pm.title , pm.content , pm.file , pm.writer )) 
            ## 커밋( DB에 실제 반영한다 )
            cursor.close()
            conn.commit()
            # 영향받은 row의 수로 설정
            # result = conn.affected_rows()
            conn.close()
            print('닫기 성공')
        except Exception as e:
            print(e)
            result = None
        return result 
    



if __name__=='__main__':
    # result = selectAllEplList()
    # print(result)
    # pass
    obj = DBHelper()
    # print(obj.loginSql('admin','2'))
    # print(obj.searchSql('시티'))

    # 게시물 한개를 담는 그릇 (최소한 필요한 것만 정의함 )
    class PostModel:
        title   = None
        content = None
        writer  = None
        file    = None
        def __init__(self,title,content,writer,file):
            self.title      = title
            self.content    = content
            self.writer     = writer
            self.file       = file
            
            
    param = PostModel('제목1','내용1','작성자1','파일경로1')
    # print(obj.insertPost(param))
    import os
    print(os.getcwd())