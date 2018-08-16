from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
# 환경설정 클레스 모듈 가져오기
from service.config import WebConfig
#from service.model.dbMgr import loginSql, searchSql,selectAllEplList
from service.model.dbMgr import DBHelper

config = WebConfig()
dbHelper= None

def create_app(config_path='resource/config.cfg'):    
    app = Flask(__name__)
    # 세션생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
    app.secret_key = 'sdkjfelifnweldqldfkwefdjlsdl'
    #######################################################
    # 환경변수 로드 (파일에서, 클레스에서)
    # 프로그램에 사용되는 고정된 정보(디비접속, 운용수치등)
    # 등은 외부파일에서 관리하는것이 일반적(소스에 고정하지 않음)
    # 통상 상수값임(변수명 대문자)
    app.config.from_pyfile(config_path, silent=True)
    from service.config import FlaskConfig
    app.config.from_object(FlaskConfig)
    print( '환경변수 사용->', app.config['DB_URL'] )
    configCheckTest( app.config.items() )
    ######################################################
    # 디비 로드 -> 웹서비스든 어플리케이션서버든 -> 요청할대마다
    # 디비에 접속->쿼리->닫기 이렇게 작업하지 않는다!!
    # 동접 천단위로 가면 -> 서비스가 셛다운됨. 살아도 응답이 느리다.
    # 풀링을 기술을 이용하여 디비 커넥션, 연결닫음 미리 준비해둔다
    # 요청 -> 커넥션 빌림 -> 쿼리 -> 반납 -> 응답
    # 접속과 닫기 라는 시간이 세이브가된다
    dbHelper = DBHelper( app )
    # Flask 객체가 생성된 이후에 라우트 진행되야 한다
    initRoute( app, dbHelper )  
    # 에러핸들러 등록
    return app

def initRoute(app, dbHelper):
    # 요청과 응답 전후로 이런 이벤트를 감지하여 전처리, 후처리
    # 를 수행하는 이미 정해져있는 함수들
    @app.before_first_request
    def before_first_request():
        print('서버가 가동하고 최초 요청시 반응 단한번')
    
    @app.before_request
    def before_request():        
        # 세션이 없는 경우
        if not 'user_id' in session:
            if request.url.find('/login')<0:
                # 세션이 없으면 모든 요청은 로그인으로 이동
                return redirect( url_for('login') )
        #print( request.url, 'user_id' in session )
        print('요청할때마다 무조건 여기를 거친다:전처리')
    
    @app.after_request
    def after_request( res ):
        print('매 요청 처리되고나서 실행됨, 응답이 지나가는 곳')
        return res
    
    @app.teardown_request
    def teardown_request(exception):
        print('브라우저가 응답하고 나서 실행')
        return '브라우저가 응답하고 나서 실행'
    
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print('http 요청 어플리케이션 컨텍스트 종료되고 실행')


    # 세션이 없어도 접근 가능한 페이지는 오직 로그인
    # 세션생성, 세션종료, 세션체크
    @app.route('/login', methods=['POST','GET'])
    def login():
        print( 'login()' )
        if request.method == 'GET':
            # 쿠키 획득
            uid = request.cookies.get('uid')
            # 쿠키가 없을 경우: None으로 나오기 때문에 기본값 처리
            if uid == None:
                uid = ''
            config.cookie_uid = uid
            return render_template('login.html', config=config)
        else:
            uid  = request.form['uid']
            upw  = request.form['upw']
            row  = dbHelper.loginSql( uid, upw )
            # false: [], (), {}, 0, ""
            # row => dict => {}
            if row:
                # 세션 처리 (필요한 정보를 세션으로 저장한다)
                # 사용자 아이디 와 이름 저장하겠다
                session['user_id'] = uid
                session['nser_nm'] = row['name']
                return redirect( url_for('home') )
            else:
                return render_template('common/alert2.html', msg='회원아님')

    # 홈페이지
    @app.route('/')
    def home():
        # 세션이 없으면 /login으로 리다이렉트
        #if not 'user_id' in session:# 세션없으면 false ->부정->참
        #    return redirect( url_for('login') )
        ########################################
        # 쿠키 적용 -> 아이디를 저장해서 로그인 페이지 뜰대
        # 자동으로 아이디가 보이게 처리
        # 응답 객체를 생성 한다.
        resp = make_response( render_template('index.html', config=config) )
        # 쿠키 세팅
        resp.set_cookie('uid', session['user_id'])
        return resp


    # 로그아웃
    @app.route('/logout')
    def logout():
        if not 'user_id' in session:# 세션없으면 false ->부정->참
            return redirect( url_for('login') )
        # 세션 종료
        print( session )
        if 'user_id' in session:
            session.pop('user_id', None)
        if 'nser_nm' in session:
            session.pop('nser_nm', None)
        print( '세션제거후->', session )
        # 페이지 요청을 리다이렉트-> 홈페이지
        return redirect( url_for('home') )

    # eplList
    @app.route('/eplList')
    def eplList():
        # 세션체크
        #if not 'user_id' in session:# 세션없으면 false ->부정->참
        #    return redirect( url_for('login') )
        # 데이터 획득
        amt  = 5; # 한번에 보여줄양
        tmp  = request.args.get('page') # 전달된 페이지값획득
        page = 0  # 최종 페이지값 초기값
        if tmp:   # 전달된 페이지가 있다면 ex) eplList?page=2, ..
            # 페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
            page = int(tmp) - 1 ;
        # 최종 결과 획득
        rows = dbHelper.selectAllEplList(page=page*amt)
        # 화면처리
        return render_template('eplList.html', 
                            config=config, epls=rows)

    # 검색 결과
    @app.route('/search', methods=['POST'])
    def search():
        keyword = request.form['keyword']   
        tmp     = dbHelper.searchSql( keyword )
        if tmp == None: tmp=[]
        return jsonify(tmp)

# 환경 변수 체크하는 함수
# configCheckTest( app.config.items() )
def configCheckTest(config):
    for key, value in config:
        print( '%s : %s ' % (key, value) )
