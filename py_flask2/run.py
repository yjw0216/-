from flask import Flask , request , url_for , render_template , redirect , jsonify
from model.d1_8 import searchSql , selectTeamName , updateTeamInfo  ## 내가만든 모듈(DB처리부분) import !!
app = Flask(__name__)

# 페이지 구성
# 홈페이지의 주소(URL)를  ~/ 로 정의하자
@app.route('/')
def home():
    return render_template('index.html',title='홈페이지')

@app.route('/join')
def join():
    return render_template('test.1.html', title='회원가입')

@app.route('/search' , methods=['POST'])
def search():
    keyword = request.form['keyword']
    # DB로 검색어를 보내서 쿼리 수행후 결과를 받아온다.
    # tmp={'name':'맨유','keyword':keyword}
    tmp = searchSql( keyword )
    if tmp ==None:
        tmp=[]   ## json에서 None은 받아들이지 못하므로 비어있는 리스트로 대체한다.
    # print(tmp)
    # jsonify() : 파이썬 객체를 json문자열로 처리
    return jsonify(tmp)


# 팀 세부 정보 보기
@app.route('/info/<teamName>')
def info(teamName):
    q = request.args.get('q')
    print( 'q=%s' % q )
    row = selectTeamName(teamName)
    # q값이 None이면 그냥 정보보기, update이면 수정하기 이다.
    return render_template('info.html' , team = row , flag= q)  ## team은 row라는 변수에 키 값을 부여한것 !

# 팀 정보 수정
@app.route('/updateTeam', methods = ['POST'])
def updateTeam():
    ## 전달된 데이터 중 총 경기수와 이름을 획득
    total = request.form['total']
    name = request.form['name']
    ## 수정 쿼리 수행
    result = updateTeamInfo(total,name) 
    # return '덕배 %s' % request.form['name']

    if result:
        return render_template('alert2.html' , msg='수정 성공 XD' , url='/info/'+name)
    else :
        return render_template('alert2.html', msg=' 수정 실패 :( ')

if __name__ == '__main__':
    app.run(debug=True)