from flask import Flask , render_template , redirect , url_for , session ,request , jsonify , make_response
from service.controller import bp_user as app
# DB
from service.model import dbHelper
from service import config

# 라우팅

# 홈페이지
# ~/user
@app.route('/')
def home():
    # if 'uid' in session: 
    #     return render_template('index.html', config=config)
    # else:
    #     return redirect(url_for('login'))
    
    # if not 'uid' in session:   ## 위에보다 이 코드가 더 깔끔
    #     return redirect(url_for('login'))   >>>>>>>>>>>>>>>>>>>>>>>>> 막을 수 있는 이유는 세션없는경우 전처리를 해줬기 때문에
    ###########################################################################################
    
    # 쿠키 적용 : 유저의 브라우저에 특정정보를 남기는 것

    ## 아이디를 저장해서 로그인 페이지 뜰때 자동으로 아이디가 보이게 처리
    ## 응답객체를 생성함
    resp = make_response( render_template('index.html',config=config) )
    # 쿠키 세팅
    resp.set_cookie('uid', session['uid'] )    # 브라우저 ctrl+shift+J 에서 Application > Cookie 에서 확인
    return resp


# 로그인
# 실제 URL : ~/user/login
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        ## get은 렌더링 post는 
        #  쿠키 획득 : GET 방식일때 
        uid = request.cookies.get('uid')
        if not uid: ## 쿠키가 없을 경우 None값뜨는것 방지하기 위해 기본값 처리
            uid=''
        config.cookie_uid = uid
        return render_template('login.html',config=config)
    else:
        uid  = request.form['uid']
        upw  = request.form['upw']
        row  = dbHelper.loginSql( uid, upw )
        # false는 빈값을 의미함
        if row:  # row는 dictionary 이기에 바로 써도 된다 (빈 딕셔너리냐 아니냐~)
        ## 세션 처리 ( 필요한 정보를 세션으로 저장한다. )
            session['uid'] = uid
            session['name'] = row['name']
            return redirect( url_for('userbp.home'))
        else:
            return render_template('common/alert2.html', msg='회원이 아닙니다 :( ')


# 로그아웃
# ~/user/logout
@app.route('/logout')
def logout():
    if not 'uid' in session:   ## 위에보다 이 코드가 더 깔끔
        return redirect(url_for('userbp.login'))  ## 주소치고 강제로 못들어 오게 또 잠궜다

    # 세션 종료
    print(session)
    if 'uid' in session:
        session.pop('uid',None)
    if 'name' in session:
        session.pop('name',None)
    print(session)
    # 페이지 요청을 redirect (홈페이지로 ! )
    return redirect(url_for('userbp.home'))
