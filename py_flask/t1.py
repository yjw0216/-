data = ['파리','로마','바르셀로나']
for city in data :
    print(city)
print('='*50)

data = [('프랑스','파리'),('이탈리아','로마'),('스페인','바르셀로나')]
for city2 in data:
    print(city2[1])
print('='*50)

data = [{'국가':'프랑스','수도':'파리'},{'국가':'이탈리아','수도':'로마'},{'국가':'스페인','수도':'바르셀로나'}]
for city3 in data:
    print(city3['수도'])


