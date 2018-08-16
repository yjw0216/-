from flask import Flask,request,render_template,redirect

app = Flask(__name__)

# 페이지 요청시 -> 데이터 전달 하기
####################################################################
# get 
# http://127.0.0.1:5000/test?uid=k&upw=1
# 서버에서 데이터 획득하는 방법
user_id = request.args.get('uid')
user_pw = request.args.get('upw')
####################################################################

# post
# http://127.0.0.1:5000/test
# 데이터는 http의 body를 타고 전달되서 직접적으로 보이지 않는다.
# 서버에서 데이터 획득하는 방법
user_id = request.form['uid']
user_pw = request.form['upw']