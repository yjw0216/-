
# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():       
    ## html은 응답데이터의 뼈대 및 콘텐츠 담당
    ## css는 스타일,레이아웃,디자인 담당
    ## java script(js)는 사용자의 인터렉션,이벤트 담당
    # return "<h1 style = 'color:red;background:black'>home page</h1>"    
    ## 작은 따옴표 큰 따옴표 구분해서 써야 함!
    # return "<script>alert('hi');</script>"
    return 'home page'



# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   ### 초기값 부여하기 debug // 디버깅 모드를 사용하면 수정한내용이 반영되어 자동으로 재 가동됨!
    # app.debug = True 
    # app.run()               ## line 22,23코드는 line 21 코드와 같은 의미 이다!
    ## 기본 포트는 5000번을 사용하는데 통상 80번( :80) 은 생략이 가능하다
    ## 포트(port) : 포트는 기본 ip에서 0~65535(65536개)의 포트를 사용할수 있다(채널이라고 생각 하면 쉬움 !)
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')     ## 실수로 땡겨 쓸때를 방지하기 위해서 코멘트 달아 주는것 