# ex06.py
import sys
my_numbers = [0,1,2,3,4,5,6,7,8,9]
max_index = len(my_numbers) # 10
output_file = sys.argv[1]
# python ex06.py ex06.csv  ## comma seperate value
filewriter = open(output_file,'a') # append : 추가
for index_value in range(max_index):
    if index_value < (max_index-1):
        filewriter.write( str(my_numbers[index_value])+ ',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print('output')

## 추가되는 코드여서 코드 실행마다 한 줄 씩 csv파일에 추가 된다.
