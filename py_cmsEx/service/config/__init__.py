class FlaskConfig(object):
    DB_URL         ='localhost'
    DB_USER        ='root'
    DB_PASSWORD    ='1324098'
    DB_DATABASE    ='pythondb'
    DB_CHARSET     ='utf8'
    MAX_POOL       = 100

class WebConfig:
    # 멤버 변수
    title       ='cms'
    site_name   ='Flask 기반 콘텐츠 관리 시스템'
    version     = 'v1.0.0'
    debug       = True
    page_title  = {'LOGIN':'관리자 로그인','MENU1':'17/18 EPL List'}
    cookie_uid  = None

    # 생성자
    def __init__(self):
        print('환경설정 생성자 호출')
    # 멤버 함수
    
    
if __name__ == '__main__':
    obj = WebConfig()
    print(obj.site_name)