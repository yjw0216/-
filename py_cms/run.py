from flask import Flask , render_template , redirect , url_for , session ,request , jsonify
from service.config import WebConfig
from service.model.dbMgr import loginSql , searchSql ,selectAllEplList

app = Flask(__name__)
# 세션생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
app.secret_key = 'anjekfsmldfmsgddjrfdkfndgrjalk'
config=WebConfig()

# <설정> 세션이 없어도 접근이 가능한 페이지는 오직 로그인 ( 로그인 안하면 홈페이지 조차 못들어온 다는 설정으로 꾸미는 것임)
# 세션생성,세션종료,세션체크 세가지를 체크해야한다!

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        ## get은 렌더링 post는 
        return render_template('login.html',config=config)
    else:
        uid  = request.form['uid']
        upw  = request.form['upw']
        row  = loginSql( uid, upw )
        # false는 빈값을 의미함
        if row:  # row는 dictionary 이기에 바로 써도 된다 (빈 딕셔너리냐 아니냐~)
        ## 세션 처리 ( 필요한 정보를 세션으로 저장한다. )
            session['uid'] = uid
            session['name'] = row['name']
            return redirect( url_for('home'))
        else:
            return render_template('common/alert2.html', msg='회원이 아닙니다 :( ')

@app.route('/')
def home():
    # if 'uid' in session: 
    #     return render_template('index.html', config=config)
    # else:
    #     return redirect(url_for('login'))
    
    if not 'uid' in session:   ## 위에보다 이 코드가 더 깔끔
        return redirect(url_for('login'))
    return render_template('index.html',config=config)

@app.route('/logout')
def logout():
    if not 'uid' in session:   ## 위에보다 이 코드가 더 깔끔
        return redirect(url_for('login'))  ## 주소치고 강제로 못들어 오게 또 잠궜다

    # 세션 종료
    print(session)
    if 'uid' in session:
        session.pop('uid',None)
    if 'name' in session:
        session.pop('name',None)
    print(session)
    # 페이지 요청을 redirect (홈페이지로 ! )
    return redirect(url_for('home'))

@app.route('/EPLlist')
def eplList():
    ## 세션체크
    # if not 'uid' in session:
    #     return redirect(url_for('login'))
    
    ## 데이터 획득
    amt = 5 ## 한번에 보여줄 양
    tmp = request.args.get('page') ## 전달된 페이지 값 획득
    page = 0  ## 최종 페이지값 초기값
    if tmp:    ## 전달된 페이지가 있다면 EPLlist?page=2 ....
        page = int( tmp ) -1   ## 페이지 계산이 2로 전달되면 1로 계산해야함 (쿼리 기준)
    
    ## 최종 결과 획득
    rows = selectAllEplList(page=page*5)
    
    ## 화면처리
    return render_template('eplList.html',config=config, epls = rows )

@app.route('/search',methods=['post'])
def search():
    keyword = request.form['keyword']
    tmp = searchSql( keyword )
    if tmp ==None:
        tmp=[]
    return jsonify(tmp)




if __name__ == '__main__':
    app.run(debug=config.debug)