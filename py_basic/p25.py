
# 파일 처리 -> 내장 함수

'''
파일 오픈 : open(파일명,엑세스 모드 , 버퍼링)
엑세스 모드 :
r -> 읽기모드
b -> 바이너리/이진형식으로 ~
w -> 쓰기모드
+ -> 반대속성이 추가되는 것을 의미함
r+ ->  읽고 쓰기
a -> 추가 , 덧붙이기
a+ -> 덧붙이고 읽기
ab -> 이진형식 덧붙이기

버퍼링 : 
0 : 안함
1 : 라인별 버퍼링
-1(음수) : 버퍼링하는 크기를 시스템 크기에 맞춤
1 이상 : 버퍼링의 크기를 부여함 
'''

# 파일I/O (입출력) -> 반드시 사용이 끝나면 닫아야 한다.
# 파일이 없으면 만들어서 오픈

# f= open('test.txt' , 'w')
# f.close()

f= open('test.txt' , 'r+')
# 10byte를 읽겠다
s = f.read(15)
print(s,f.tell())      ## .tell() 은 현재 파일 포인터의 위치를 알려주는 함수
f.seek(4)   ## 파일포인터를 처음 위치 기준에서 이동 
s = f.read(5)
print(s,f.tell())
f.close()

f = open( 't1.txt' , 'w')
for n in range(10):
    str = '%d  line(라인) \n' % n
    f.write(str)
f.close()

f= open('t1.txt' , 'r')
while True:
    data = f.readline()  ## 한 줄 씩 읽는다
    if not data:
        break
    print( data ) 
f.close()

## 파이썬은 I/O에서 닫는 부분을 자동을 처리해주는 기능을 가지고 있다. with문 !!

with open('t1.txt' , 'r') as f:
    while True:
        data = f.readline()  ## 한 줄 씩 읽는다
        if not data:
            break
        print( data ) 

####################################################################
# 외장함수 : 구조화된 모듈 , 저장 및 로드
# 피클
import pickle as p  
data = {
    1:[1,2,3,4],
    2:{"name":'멀티'},
    3:(5,6,7,8)
}

# 기록
with open('data.p' ,'wb' ) as f1:        ## 이진데이터로 읽기
    p.dump(data,f1,p.HIGHEST_PROTOCOL)        

# 로드 -> 데이터 원복
with open('data.p' ,'rb' ) as f1:
    print(p.load(f1))

with open('data.p' ,'rb' ) as f1:
    tmp = p.load(f1)
    print(tmp,type(tmp))

####################################################################
# os 모듈
import os
print('현재 프로젝트 디렉토리(운영체계에 관계없이) ' , os.getcwd())
os.mkdir('tmp')    ## 주석처리로 빼놓고 코드 구동하기
os.chdir('tmp')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())