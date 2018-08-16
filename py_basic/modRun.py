# 모듈 사용

# from mod import PI,sum,A
# print( PI )

## 안되는 케이스 ... 패키지가 아니라고함
# import mod.PI 
# print( PI )

from a.b.mod import PI
print(PI)

from a.b import mod
print(mod.PI)

# 별칭
from a.b import mod as m
print(m.PI)

import a.b.mod as m2
print(m2.PI)

# python 3.x 버젼에서 자동지원가능 (2.x는 추가적으로)
from a.b import *  ## *의 의미는 모든 것 
print(mod.PI)


####################################
# a > b > __init__.py 모듈 가져오기 #
####################################

import a.b as bx
print(bx.sumEx(3,4))

from a.b import sumEx
print(sumEx(9,8))

## a파일의 init 파일의 NAME 가져오기

from a import NAME
print(NAME)
