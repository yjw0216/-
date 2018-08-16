from flask import Flask,request,render_template,redirect

app = Flask(__name__)

# 하나의 주소(URL)에 get,post를 다 받아서 내부에서 나눠 처리하게 하는 방법
# 하나의 주소에서 get,post와 같이 다양한 메소드를 지원하여 마치 여러개의 페이지(주소)가 존재하도록
# 처리하는 방식을 restful이라고 한다.
@app.route('/login', methods=['GET','POST'])     
def login():   ## ★ 하나의 주소로 화면이 쪼개진다 get은 화면으로 post는 프로세스로 나눠 주소를 최대한 줄이는게 포인트!!★
    if request.method == 'POST':
        return loginProcess()
    else:
        return render_template('login.html')

def loginProcess():
    #아이디 비번 획득
    uid = request.form['uid']
    upw = request.form['upw']
    print(uid,upw)
    # DB 쿼리 수행
    if uid=='1' and upw=='1':
        # 회원이면 처리 -> 메인서비스로 이동 -> 포워딩
        # 포워딩 : 요청에 응답하지 않고 요청을 다른 주소로 이어주는 방법
        # return redirect('/main?uid='+ uid)    ## redirect가 포워딩을 해주는 함수
        return render_template('alert2.html', msg=' 로그인 성공 ! ' , url='/main')    
    else:
        # 회원아니면 처리 -> 경고창 -> 되돌아 가기
        return render_template('alert.html', msg='회원 아닙니다')   ## alert2로해도 가능 (alert2가 확장버전임 !! )
    # return 'login process'

# 지금은 그냥 이 페이지를 진입할 수 있으나 향후 세션을 이용하여 로그인 후에만 접근할 수 있게 제한 할것임
@app.route('/main')
def main():
    return '현재 main page이며 %s의 아이디를 가집니다' % request.args.get('uid')


if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')    