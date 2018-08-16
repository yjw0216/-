from flask import Flask , render_template , redirect , url_for , session ,request , jsonify , make_response
from service.config import WebConfig,FlaskConfig
# from service.model.dbMgr import loginSql , searchSql ,selectAllEplList
# from service.model.dbMgr import DBHelper
from service.model import createDBHelper


config=WebConfig()
# dbHelper = None

def create_app(config_path='resource/config.cfg'):
    app = Flask(__name__)
    # 세션생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
    app.secret_key = 'anjekfsmldfmsgddjrfdkfndgrjalk'

    ###########################################################
    # 환경 변수 로드 ( 파일or클래스에서 지원해줌 )
    app.config.from_pyfile(config_path,silent=True)
    app.config.from_object(FlaskConfig)
    print('환경변수 사용 >>' , app.config['DB_URL'])
    ###########################################################

    # DB 로드 : `Web/App서비스 > 요청할때마다 DB에 접속 > 쿼리수행 > 닫기'  이렇게 하지 X
    #            동접이 높아지면 서비스가 셧다운 되거나 응답이 느려진다.
    #            풀링 기술로 DB커넥션,연결닫음을 미리 준비 해둠 ! 
    # 폴링    : 요청 > 커넥션 빌림 > 쿼리 > 반납 > 응답 
    #           접속과 닫기라는 시간을 Save!           
    

    # dbHelper = DBHelper( app )
    createDBHelper( app )  ## 바로 윗줄 코드랑 비교 !
    

    # Flask 객체가 생성된 이후에 라우트가 진행되어야 한다 ! 
    # 회원쪽 URL : ~/users/login , ~/users/logout , ~/users/join
    # epl URL  : ~/epl/allList , ~/epl/search
    # URL에 prefix를 부여하여 업무를 분할하고 API를 분류할 수 있는 방식
    # Blueprint( 블루프린트 )
    
    
    from service.controller import bp_epl,bp_user,bp_bbs
    from service.controller import user,epl,bbs
    app.register_blueprint(bp_user,url_prefix='/user')  ## 블루프린트를 등록하고 URL정의
    app.register_blueprint(bp_epl,url_prefix='/epl')
    app.register_blueprint(bp_bbs,url_prefix='/bbs')
    initRoute( app )
    
    
    
    # 에러 핸들러 등록
    return app

def initRoute ( app  ):

    ## 요청과 응답 전후로 특정 이벤트를 감지하여 전처리,후처리를 수행하는 미리 정해진 함수들
    @app.before_first_request
    def before_first_request():
        print(' 서버가 가동하고 최초 요청시 반응 ... 딱 한번만.. ')

    @app.before_request
    def before_request():
        # <중요> 세션이 없는 경우 ( 이 과정을 통해 다음 모든 페이지의 세션을 한번에 관리 할 수 있다 !! )
        if not 'uid' in session:
            if request.url.find('/login') <0:  ## find결과값은 없으면 음의 값을 반환하기 때문에 세션에 로그인이 없다는 뜻
                # 세션이 없으면 모든 요청은 로그인으로 이동한다 
                return redirect(url_for('userbp.login'))
        # print( request.url , '세션이 있나 ?' , 'uid' in session )  ## 뒤에 'uid' in session는 조건 식이라 결과는 참거짓만 나옴
        print(' 요청할때는 무조건 요기를 거칩니당 >> 전처리!  ')

    @app.after_request
    def after_request( res ):   ## after_request는 응답객체를 인자로 가져야함
        print('매 요청을 처리하고 나서 실행된다  + 응답이 지나가는 곳 ')
        return res 

    @app.teardown_request
    def teardown_request( exception ):
        print(' 브라우저가 응답하고 나서 실행 ')
        return '브라우저가 응답하고 나서 실행'         

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print('http 요청 어플리케이션 컨텍스트가 종료되고 실행함')
        
    ################################################################################################

# 환경 변수를 체크하는 함수
# configCheckTest(app.config.items()) << 요거 호출하면 됨 !
 
def configCheckTest(config):
    for key,value in config:   ## items라는 함수 ! 
        print('%s : %s ' % (key,value))