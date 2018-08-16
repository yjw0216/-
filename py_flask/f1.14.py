
#######################################################################
##                           최종적                                   ##
#######################################################################

# ~/add/<x>/<y> --> redirect --> ~/mul?res=xxx --> redirect -->  ~/show/<value>
# add 페이지는 x+y
# mul 페이지는 res*10을 던져준다
# show 페이지는 최종값을 보여준다

from flask import Flask , url_for , redirect , request

app = Flask(__name__)



@app.route('/add/<int:x>/<int:y>')    ### <int:x> == 들어올것에 제한 조건을 두는 것 
def add(x,y):
    sum = x+y
    # redirect( '/mul?res=sum값' )
    return redirect('%s?res=%s' % (url_for('mulFunc'),sum ) ) 

@app.route('/mul')
def mulFunc():
    sum = int(request.args.get('res')) * 10
    return redirect(url_for('showFunc', value = sum))

@app.route('/show/<value>')
def showFunc(value):
    return ' 최종 값 = ' + value


if __name__ == '__main__':
    app.run(debug=True)



    ## +++ flask의 정적경로 위치
    # static 폴더 밑에 리소스(이미지,js,css)가 있으면 즉시 경로를 인식한다 (= 라우팅이 불 필요 하다 !)
    ## http://127.0.0.1:5000/static/img/logo.png 으로 바로 인식 됨 !