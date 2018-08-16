# 모듈

## 변수

PI = 3.14

## 함수
def sum(x,y):
    return x+y

## 클래스
class A:
    name ='멀티'
    def __init__(self):
        print(self.name)


## 테스트일때
if __name__=='__main__':
    print(__name__,sum(1,2))   # (= print(sum(1,2)) )

### __name__의 값은 파이썬이 구동시 결정
### python mod.py로 실행하면 (!단축키) __main__으로 설정
### python modRun.py 처럼 다음 파이선이 구동해서 모듈로 가져오게 되면
### mod로 설정된다.