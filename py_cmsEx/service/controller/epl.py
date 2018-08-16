from flask import Flask , render_template , redirect , url_for , session ,request , jsonify , make_response
from service.controller import bp_epl as app
# DB
from service.model import dbHelper
from service import config

# 라우팅

# epllist
# ~/epl/EPLlist
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
    rows = dbHelper.selectAllEplList(page=page*amt)
    
    ## 화면처리
    return render_template('eplList.html',config=config, epls = rows )

# 검색결과
# ~/epl/search
@app.route('/search',methods=['post'])
def search():
    keyword = request.form['keyword']
    tmp = dbHelper.searchSql( keyword )
    if tmp ==None:
        tmp=[]
    return jsonify(tmp)
