from service.model.dbMgr  import DBHelper

dbHelper = None

# 이 함수는 DBHelper 객체를 생성하는 역할만 한다.
def createDBHelper( app ):
    global dbHelper
    dbHelper = DBHelper( app )


# 게시물 한개를 담는 그릇 (최소한 필요한 것만 정의함 )
class PostModel:
    title   = None
    content = None
    writer  = None
    file    = None
    def __init__(self,title,content,writer,file):
        self.title      = title
        self.content    = content
        self.writer     = writer
        self.file       = file