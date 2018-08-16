
# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
## 요청 : http + :// + IP + : + 포트 + / + 세부 페이지이름
@app.route('/')
def home():
    return 'home page'

## http://127.0.0.1:5000/users/login 를 처리할 페이지를 구성하시오
## 세부 요청페이지를 어떤 함수가 처리할 것 인지를 매칭하는 기능이 route이다!
@app.route('/users/login') # 페이지 주소(URL) 정의
def login():
    return 'Login Page'

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')   