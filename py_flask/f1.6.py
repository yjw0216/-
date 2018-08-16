## html을 직접 작성하는게 아니라 템플렛에서 가져오기 하는 방법 1. render_template 모듈을 통해 가져오기


# 1. 모듈 가져오기
from flask import Flask,request, render_template

# 2. 앱 생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)


@app.route('/')
def home():

    # 보여주고자하는 html을 만들어서 templates 폴더 밑에 위치시키고
    # render_template('html파일명)하고 html을 렌더링해서 뿌려준다
    return render_template('login.html' , name='멀티' )

@app.route('/login')
def login():

    uid = request.args.get('uid')
    upw = request.args.get('upw')

    if uid == 'test' and upw == '1234':
        return '회원입니다'
    else:
        return '''
        <script>
            alert('%s');    // 팝업 띄우기
            history.back(); // 이전 페이지 이동
        </script>
        ''' % '일치하는 회원정보가 없습니다 가입하시겠습니까?'

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')   