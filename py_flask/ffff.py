from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# 하나의 주소(URL)에 get, post를 다 받아서 내부에서 
# 나눠서 처리하게 하는 방법
# 하나의 주소에서 get,post와 같이 다양한 메소드를 지원하여
# 마치 여러개의 페이지(주소)가 존재하도록 처리해는 방식
# restful(레스트풀)
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # 응답, 로그인 실제 처리(디비연동)
        #return 'login process'
        #a ='login process'
        #return a
        #a =loginProcess()
        #return a
        return loginProcess()
    else:# get
        # 응답
        return render_template('login.html')

# 별도의 함수로 처리 루틴을 빼도 관계 없음
def loginProcess():
    # 아이디 비번 획득
    uid = request.form['uid']
    upw = request.form['upw']
    print( uid, upw )
    # 디비 쿼리 수행
    if uid=='1' and upw=='1':
        # 회원이면 처리 -> 메인 서비스로 이동 -> 포워딩
        # 포워딩 : 요청에 응답하지 않고, 요청을 다른 주소로
        # 이어주는 방법, 
        return redirect('/main')
    else:
        # 회원아니면 처리 -> 경고창 -> 되돌아가기
        return 'error'
    #return 'login process'

# 지금은 그냥 이 페이지를 진입할수 있으나, 
# 향후 세션(session)을 이용하여 로그인후에만 접근할수 있게
# 제한 할것이다
@app.route('/main')
def main():
    return "main page %s " % request.args.get('uid')

if __name__ == '__main__':
    app.run(debug=True)