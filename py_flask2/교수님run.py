from flask import Flask, request, url_for, render_template, redirect, jsonify
# 내가 만든 모듈(디비 처리부분) import
from model.d1_8 import searchSql, selectTeamName, updateTeamInfo
app = Flask(__name__)

# 페이지 구성
# 홈페이지 : ~/
@app.route('/')
def home():
    return render_template('index.html', title='홈페이지' )

@app.route('/join')
def joni():
    return render_template('test.1.html', title='회원가입' )

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']   
    # 디비로 검색어를 보내서 쿼리 수행후 결과를 받아온다
    #tmp = {'name':'맨유', 'keyword':keyword}
    tmp = searchSql( keyword )
    # None이면 json 변환에 문제가 발생하므로 비워있는 리스트로 대체함
    if tmp == None: tmp=[]
    #print( tmp )
    # jsonify() : 파이썬 객체를 json 문자열로 처리 -> 전송
    print( jsonify(tmp) )
    return jsonify(tmp)

# 팀 세부 정보 보기
@app.route('/info/<teamName>')
def info(teamName):
    q = request.args.get('q')
    print( 'q=%s' % q )
    row = selectTeamName(teamName)
    # q값이 None이면 그냥 정보보기, update이면 수정하기 이다
    return render_template('info.html', team = row, flag=q )

# 팀 정보 수정
@app.route('/updateTeam', methods=['POST'])
def updateTeam():
    # 전달된 데이터중 총경기수와 이름을 획득
    total = request.form['total']
    name  = request.form['name']
    # 수정 쿼리 수행
    result  = updateTeamInfo(total, name)
    # 결과 처리
    if result == None:
        return render_template('alert2.html', 
                                   msg='수정성공', url='/info/'+name)
    else:
        return render_template('alert2.html', msg='수정실패')

if __name__ == '__main__':
    app.run( debug=True )