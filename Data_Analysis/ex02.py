# ex02.py
from math import exp,log,sqrt
import re
from datetime import date , time ,datetime , timedelta
from operator import itemgetter
import sys 

input_file = sys.argv[1]
print('output')
with open(input_file,'r',newline='') as filereader:                 ## with 문을 사용하면 close를 안해줘도 상관없음 !
    for row in filereader:
        print('{}'.format(row.strip()))

