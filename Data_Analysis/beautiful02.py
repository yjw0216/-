from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://nlotto.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup( html , 'html.parser')
# print( soup.prettify() )
hoi = soup.find('h3', {'class':'result_title'})   ## h3 밑에 class가 ~ 인 것을 찾는 법
print(hoi)
print('='*50)
print(hoi.strong.string, '회') ## hoi 자체는 h3 밑~ class~ 인거 이고 거기서 <strong>안에 문자열을 찾고 싶다 

p = soup.find('p' , {'class':'number'})
print(p)

'''
1. p로 부터 img 태그를 얻자
2. img태그 속 alt 값을 추출하자
'''

imgs = p.find_all('img')  
# print(imgs)            ## 이러면 리스트에 담김
numbers = []
for img in imgs:      #  속성에 접근하고 싶을때는 
    print(img['alt']) #  [ <img alt="12" src="/img/common_new/ball_12.png"/>, ~~]  여기서 alt 값을 뽑는 방법..
                        # 내부적으로 'alt' : '12' 처럼 딕셔너리 구조로 가지고 있기때문에 인덱싱이 가능하다 !!!!
    numbers.append(img['alt'])

bonus = numbers.pop()
print(numbers)
print(bonus)


## 리스트 표현식 ##  
# (위 23번 코드를 훨씬 깔끔하게 줄여보기)
 
numbers = [ img['alt'] for img in imgs]   # List 안에 반복문을 담은 것 ! 


print(numbers)

# 리스트 표현식 심화
# 1~100까지의 숫자중 짝수를 obj란 리스트에 담으시오 
obj =  [ i for i in range(1,101) if i % 2 ==0  ]
print(obj)  # 리스트 안에 for 문과 if 문을 같이 사용 가능 