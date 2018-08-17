# ex04.py
from math import exp,log,sqrt
import re
from datetime import date , time ,datetime , timedelta
from operator import itemgetter
import sys 
import glob
import os

# python ex04.py ex04.tsv
my_letters = ['a','b','c','d','e','f','g','h','i','j']
max_index = len(my_letters) ## 10
output_file = sys.argv[1]
filewriter = open(output_file,'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+ '\t')
    else:
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()
print('Output')