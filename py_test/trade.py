# pip install numpy==1.14.3
# pip install pandas==0.20.3
# pip install pandas-datareader==0.5.0

import pandas as pd
import pandas_datareader.data  as web
import datetime

# 조회기간
start_day = datetime.datetime(2018,6,1)
end_day   = datetime.datetime(2018,6,30)

# 종목코드
code = '035510.KS'

# 조회
treadDate = web.DataReader( code , 'yahoo' , start_day , end_day)
print( treadDate)