import pandas as pd
import numpy as np

df = pd.read_csv('datasets/supplier_data.csv')    ## read_csv 로 csv 파일 읽고
print(df)

df.to_csv('outputs/output_file02.csv', index=False ) ## to_csv로 csv 파일 저장하기
