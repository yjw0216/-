# ex03.py
from math import exp,log,sqrt
import re
from datetime import date , time ,datetime , timedelta
from operator import itemgetter
import sys 
import glob
import os

# print( dir(os))

print('output')
input_path = sys.argv[1]
for input_file in glob.glob(os.path.join(input_path,'*.txt')):
    with open(input_file,'r',newline='') as filereader:
        for row in filereader:
            print(row.strip())

