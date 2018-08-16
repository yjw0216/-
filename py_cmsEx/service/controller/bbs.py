from flask import Flask , render_template , redirect , url_for , session ,request , jsonify , make_response
from service.controller import bp_bbs as app
# DB
from service.model import dbHelper, PostModel
from service import config
import os


# ~/bbs        >> GET방식  >> 등록된 글 리스트
@app.route('/')
def home():
    pass

# ~/bbs/upload >> GET방식  >> 폼
# ~/bbs/upload >> POST방식 >> 등록
@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET': # get >> 업로드 폼 
        return render_template('upload.html', config=config)
    else: # post >> 업로드 처리
        title   = request.form['title']
        content = request.form['content']
        writer  = session['uid']
        f       = request.files['file']
        # 서버 구동 위치에 따라 경로가 달라질 수 있다. 특히 단축키 사용에 주의 !!!!
        path = "%s/service/static/upload/img/%s" % (os.getcwd() , f.filename )   ## 경로지정
        path = path.replace('\\','/')                                            ## 경로 정규표현식으로 변형
        f.save(path)               ## 파일 저장하기 코드 
                                   ## 파일이름 중복을 방지하기 위해 경로 밑에 계정별로 폴더를 만들어서 저장 하거나 >> os모듈
        file_path='/upload/img/%s' % f.filename
        param = PostModel( title , content , writer , file_path )
        print('나와라')
        dbHelper.insertPost(param)
        # 원래 insert 후 affected_rows 가 1 이나오고 이를 체크해서 성공여부를 결정해야한다!!

        # 게시판 리스트 화면을 구현하지 않아서 그냥 돌아가겠음
        return render_template('common/alert2.html' , msg = '등록성공 XD ')