from flask import Flask,request,render_template, redirect,url_for

app = Flask(__name__)

# 하나의 주소(URL)에 get,post를 다 받아서 내부에서 나눠서 처리하게 하는 방법
# restful(레스트풀)
# 하나의 주소에서 get,post와 같이 다양한 메소드를 지원하여 
# 마치 여러개의 페이지(주소)가 존재하도록 처리하는 방식 
        
@app.route('/login',methods=['GET','POST'])
#로그인페이지에서         
def login() : 
    #get은 화면 process는 post
    if request.method == 'GET' :
        return render_template('login.html')

    elif request.method=='POST' :
        return loginProcess()
    # 응답,로그인 실제 처리(디비연동)  
def loginProcess() :
    uid=request.form['uid']
    upw=request.form['upw']
    print(uid,upw)
    # 아이디 비번 획득
    # 디비 쿼리 수행
    # 회원이면 처리
    # 회원 아니면 처리
    if uid=='1' and upw=='1' : 
        return redirect(url_for('main')) # return '/service'
        # return redirect(url_for())
        # url_for("특정 url과 연결된 함수명"
        #  - url을 직접 연결해주지않고  함수보고 url주소 찾아가서 알아서 됨
        #내부적으로 참조하는 것은 모든 url_for()을 쓰고 url을 하드코딩 해주지 않음
        # return render_template('alert.2.html',msg='로그인 성공',url='/main')
        #메인서버에 uid 보내기

    #메인 서비스로 이동 ->포워딩
    #포워딩 : 요청에 응답하지 않고, 요청을 다른 주소로
    #이어주는 방법
   
    else : return render_template('alert.2.html',msg='회원이 아닙니다')
    #경고창 ->되돌아가기

#지금은 그냥 이 페이지를 진입할 수 있으나, 향후 세션(session) 을 이용하여 로그인후에만 접근할 수 있게
#제한할 것 
@app.route('/service')
def main() :
    return "main page %s"%request.args.get('uid')

if __name__ =="__main__" :  
    app.run(debug=True)
