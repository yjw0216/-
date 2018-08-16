from flask import Flask, request, render_template, redirect, url_for
from d1_8 import loginSql

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return loginProcess()
    elif request.method == 'GET':
        return render_template('login.html', name='test')

def loginProcess():
    uid = request.form['uid']
    upw = request.form['upw']
    # 디비 쿼리 수행
    rows    = loginSql( uid, upw )
    if rows:#uid=='1' and upw=='1':
        # ~/service?name=멀티
        # 회원 정보를 포워딩할때 get방식에 맞춰서 전달
        return redirect( url_for('main2') + '?name=%s' % rows[0]['name'] )
    else:
        return render_template('alert2.html', msg='회원아님')

@app.route('/service')
def main2():
    return "main page %s" % request.args.get('name')

if __name__ == '__main__':
    app.run(debug=True)