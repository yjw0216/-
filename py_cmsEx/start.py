from service import create_app,config

# 플라스크 어플리케이션 서버 생성
application = create_app()       ## 보안 절차 !  

# 구동
if __name__ == '__main__':
    print(application.config['TEST_PORT'])
    print(application.config['REAL_URL'])
    host = None
    port = None
    if application.config['ENV'] == 'production': ## 상용
        host=application.config['REAL_URL']
        port=application.config['REAL_PORT']
    else: ## 개발/테스트
        host=application.config['TEST_URL']
        port=application.config['TEST_PORT']     ## IP나 Port를 자동으로 설정할 수 있게 설정 ( 환경 변수로 __init__ line 16)
    application.run(
        host=host,
        port=port,                        ## 실제 배포한다는 가정을 하면 ~
        debug=application.config['SERVER_RUN_MODE_DEBUG'])
