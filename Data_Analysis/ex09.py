# ex09.py

import pandas as pd
input_file = 'datasets/supplier_data.csv'
output_file = 'outputs/output03.csv'

df = pd.read_csv(input_file)
print(df['Cost'])

df['Cost'] = df['Cost'].str.strip('$').astype(float)    ## 칼럼선택 / 문자열 / 문자대체 / 형태변환  / .~.~ 찍으며 가는게 함수형코드
print(df)

df2 = df.loc[df['Supplier Name'].str.contains('Z') | (df['Cost'] > 600) , :]  # 뒤에 [~~~: ] 는 전체라는 뜻  R에서 [1:3]은 1행3열
print(df2)

df2.to_csv(output_file,index=False)


# 해당 조건을 따르는 특정 칼럼을 뽑는 코드

df2 = df.loc[df['Supplier Name'].str.contains('Z') | (df['Cost'] > 600) , ['Supplier Name' ,  'Cost']]