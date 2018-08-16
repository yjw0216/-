class FlaskConfig(object):
    DB_URL          = 'localhost'
    DB_PORT         = 3306#, 포트가 다른 사람을 변경
    DB_USER         = 'root'
    DB_PASSWORD     = '1234'
    DB_DATABASE     = 'pythondb' 
    DB_CHARSET      = 'utf8'
    MAX_POOL        = 100 # 디비 커넥션 연결 수

class WebConfig:
    # 맴버 변수
    title       = 'cms'
    site_name   = 'Flask기반 콘텐츠 관리 시스템'
    version     = 'v1.0.0'
    debug       = True
    page_title  = { 'LOGIN':'관리자 로그인', 'MENU1':'2017~18 EplList' }
    cookie_uid  = None
    # 생성자
    def __init__(self):
        print('환경설정 생성자 호출')
    # 맴버 함수

if __name__=='__main__':
    obj = WebConfig()
    print( obj.site_name )