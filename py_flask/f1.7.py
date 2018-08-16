from flask import Flask

app = Flask(__name__)

# 데코레이터는 하나의 함수에 여러개를 연결할 수 있다.
# @~ : 데코레이터
# ~/ or ~/xx 두가지 url을 가지게 됨 
@app.route('/test')      ## 내부적으로 이렇게 호출 : home() 
@app.route('/test/<id>')  ## 내부적으로 이렇게 호출 : home('xx')  // 동적 파라매터를 받겠다
def home(id=None):      
    if id:
        return 'sub page %s ' % id
    else:
        return 'home page'

if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')    