# 모듈 가져와서 사용하기 및 만들기
# p20_mod.py를 가져와서 p21.py 본 코드에서 사용하겠다
# 문법 :  from 모듈명 import 모듈(클래스,함수,변수 모두 가능)
## Xman class를 가져다가 사용하고 싶다
from p20_mod import Xman
obj = Xman('멀티',20)
obj.eat()
print(obj.name)