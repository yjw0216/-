# ex01.py
from math import exp,log,sqrt
import re
from datetime import date , time ,datetime , timedelta
from operator import itemgetter
import sys 

print("Output")
input_file = sys.argv[1]  ## hardCoding : input_file = "ex01.txt"
# python ex01.py ex01.txt
#           0       1
filereader = open(input_file,'r')  # 'r' =read , 'w' = write...
for row in filereader:
    print(row.strip())
filereader.close()  ## File , DataBase , 