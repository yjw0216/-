from flask import Flask,request,render_template, redirect,url_for
from d1_8 import loginSql

app = Flask(__name__)


@app.route('/login',methods=['GET','POST'])
     
def login() : 
    if request.method == 'POST':
        return loginProcess()
    elif request.method == 'GET':
        return render_template('login.html', name='test')
    # 응답,로그인 실제 처리(디비연동) 
    #  
def loginProcess() :
    uid=request.form['uid']
    upw=request.form['upw']
    
    rows = loginSql( uid=uid , upw=upw )
    if rows:
    # uid=='1' and upw=='1' : 
        return redirect(url_for('main')+ '?name=%s' % rows[0]['name'] ) 
    else : 
        return render_template('alert.2.html', msg='회원이 아닙니다')
    
@app.route('/service')
def main() :
    return "main page %s"%request.args.get('name')

if __name__ =="__main__" :  
    app.run(debug=True)