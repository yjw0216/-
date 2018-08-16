# Blueprint 정의
from flask import Blueprint

# ~/user
bp_user = Blueprint('userbp',        ## userbp는 구분하기위해 임의의 이름을 부여한 것 정도로 이해
                    __name__,
                    template_folder='../templates',      ## ../ 경로의 주소를 올린다는 뜻
                    static_folder='../static') 

# ~/epl
bp_epl = Blueprint('eplbp',
                    __name__,
                    template_folder='../templates',
                    static_folder='../static')

# ~/bbs
bp_bbs = Blueprint('bbsbp',
                    __name__,
                    template_folder='../templates',
                    static_folder='../static')
