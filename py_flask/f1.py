## 프로젝트 절차 
# 기획(아이템 수집 -> 제안서/기획서) -> 개발(요구사항 분석 -> 개발계획서[개발일정/업무분담/기술분석]) -> 테스팅/디버깅 -> 수정 -> 런칭

# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(서버생성)
app = Flask(__name__)  ## __name__은 임의의 인자값을 부여한것이고 의미없다!

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():
    return 'home page'

@app.route('/login')
def login():


@app.route('/logout')
def logout():
    return 'logout page'
    return 'login page'



# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   ### 초기값 부여하기 debug // 디버깅 모드를 사용하면 수정한내용이 반영되어 자동으로 재 가동됨!

