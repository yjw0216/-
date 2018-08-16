## 클라이언트가 웹페이지를 요청할때 데이터를 보내고 싶다 
### 대표적인 케이스-> 검색,로그인,링크클릭 등등 
### 데이터를 보내는 방법 : method(get,post,put,delete...) , 동적 파라매터

### 데이터를 가지고 페이지를 요청하는 방법 중 : 동적 파라매터 을 해보기 

# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():
    return 'home page'

# 동적 파라매터 1 : URL(주소)에 데이터를 보내는 방법
@app.route('/news/<news_id>')   ## <>안의 news_id 는 임의로 지정한 변수
def news(news_id):
    return '전달된 데이터 %s' % news_id

@app.route('/login/<uid>/<upw>')
def login(uid,upw):
    return '아이디: %s 비밀번호: %s' % (uid,upw)    ## 이러한 데이터는 전달하면 안된다  
                                                   ## 즉 URL보내는건 보안에 취약!!

# 동적 파라매터 2 : 타입을 지정하여 보다 명확하게 데이터를 전달할 수 있다 .
## 타입 : int(정수),float(부동소수,소수),path(가변경로)

@app.route('/test/<int:num>')
def test(num):
    return '정수형 전달 데이터 : %s ' % num


@app.route('/test2/<path:num>')
def test2(num):            ## http://127.0.0.1:5000/test2/1.34/dlawhddjs/98 에서 test2 뒤의 /를 주소로 보지 않고 세가지 데이터로 인식하게 해주는 것이 가변 경로 이다 !!
    return '전달 데이터 : %s ' % num.split('/')      ### 세가지 데이터를 볼수 있으므로 분해도 할 수있다 !!! + split은 리스트로 결과 반환



# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')   