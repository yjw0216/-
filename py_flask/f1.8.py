from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')     
def home():      
    teams = [{'rank' :1 ,'team' :'프랑스'},
    {'rank':2,'team' :'벨기에'},
    {'rank':3,'team' :'잉글랜드'},
    {'rank':4,'team' :'크로아티아'}]
    # teams 안에 팀을 하나씩 출력하시오
   
    for i in teams :
        print(i['rank'],i['team'])
    # 응답
    return render_template('index.html' , title = '제목' ,teams=teams)

if __name__ == '__main__':
    app.run(debug=True)   
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다')    