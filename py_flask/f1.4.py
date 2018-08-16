## 페이지를 요청할때 데이터 보내기 : method 방식
# get: url?uid=ppp&age=10           ### 딕셔너리 처럼 {uid:ppp}
#        uid,age등은 키 값
#          &은 (키=값)의 세트를 구분하는 구분자
# 문제점: 데이터가 눈에 보임 -> 보안에 취약하다 , 큰 데이터는 전송불가 (짤려서 보인다 왜냐면 http 프로토콜의 헤더에 데이터를 세팅해서 전달하기 때문에 공간이 적음)
# 장점 : 구성이 편하고 전달이 빠르다(상대적으로) 

# 1. 모듈 가져오기
from flask import Flask,request

# 2. 앱 생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# 아무런 세팅이 없으면 기본 get방식으로 요청함을 의미한다

# http://127.9.9.1:5000/url?uid=ppp&age=10

@app.route('/')
def home():
    # get방식을 통해서 전달된 데이터를 뽑으려면 request 객체
    # return 'home page %s ' % request.method   ## get 방식을 사용 함을 알 수 있다
    return'''
            <!-- html : hyper text markup language-->  
        <html>
            <head>
                <!-- html 문서의 메타 정보를 표현하는 위치 -->
            </head>
            <body>
                <!-- 눈에 보이는 모든 부분이 body에 있다-->
                <!--사용자로부터 아이디와 비번을 입력받기
                    로그인 버튼을 누르면 로그인 처리하는 페이지로 
                    아이디와 비번을 가지고 요청한다 
                    -> 해당 페이지는 아이디 비번 가지고 DB에 쿼리
                    -> 쿼리 결과 회원이면 정상처리(서비스 이동)
                    -> 회원 아니면 메세지 처리(가입,재로그인 유도)
                -->
                <fieldset>
                    <form action = '/login' method="GET">
                        <input type='text' name= 'uid' placeholder="아이디를 입력" autofocus required/> 
                        <br/>                  <!--    단독태그하려면 < ~~ /> 이렇게 쓴다    -->
                        <input type='password' name = 'upw' placeholder="비밀번호 입력" required/>
                        <br/>
                        <input type='submit' value = '로그인' />
                    </form>
                </fieldset>
            </body>
        </html>
    '''

@app.route('/login')
def login():
    ## request.args.get('키')
    ## 전달될 데이터 획득해서 변수에 담기
    uid = request.args.get('uid')
    upw = request.args.get('upw')
    ## DB에 쿼리했다 치고
    if uid == 'test' and upw == '1234':
        return '회원입니다'
    else:
        return '''
        <script>
            alert('%s');    // 팝업 띄우기
            history.back(); // 이전 페이지 이동
        </script>
        ''' % '일치하는 회원정보가 없습니다 가입하시겠습니까?'


    ## 뻑나는거 방지하려면~
    # try:
    #     ## request.args.get('키')
    #     return 'UserID : %s   UserPASSWORD : %s' % (request.args.get('uid'),request.args.get('upw'))
    # except Exception as e:
    #     return 'UserID : %s   UserPASSWORD : %s' % (request.params.get('uid'),request.params.get('upw'))


# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')   