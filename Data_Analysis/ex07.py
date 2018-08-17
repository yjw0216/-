# ex07.py
import sys

## Pandas가 없을때 csv파일을 부르기 위한 하드코딩 !

input_file = 'datasets/supplier_data.csv'
output_file = 'outputs/output_file01.csv'

with open(input_file,'r',newline='') as filereader:
    with open(output_file,'w',newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+ '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list)) + '\n')



# map : 하나씩 처리
# reduce : 줄인다(합친다 등)


# 반복문으로 처리
c = [1,2,3,4,5]
d = []
for i in c:
    x = i ** 2
    d.append(x)
print(d)


# Map 을 활용해 반복문 없이 데이터 처리
def square(x):
    return x ** 2

e = map(square , c)    ## map(처리할 함수 , 처리할 데이터(반복자))
print(e)
print(list(e))  ## lazy loading


### lambda 표현식을 활용 ( 익명함수(이름이x)를 사용할때 활용 됨 )
f = map(lambda x : x **2 , c)
print(list(f))


g = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
h = map(str,g)
print(list(h))


######################################################################################################33

# Reduce
from functools import reduce

i = range(1,11)

def add( x,y ):
    return x+y

j = reduce(add,i)                                        # Redece ?
print(j) # 55                                            # 1+2 , 1+2 + 3 , 1+2+3 + 4 ... 반복되는걸 
                                                         # 한번에 55로 바로 보여줌
k = reduce( lambda x,y : x+y , i)                        # [범위] / [연속된 데이터] 계산이 된다 !
print(k)