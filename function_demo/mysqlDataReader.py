import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fund', charset='utf8mb4')

df = pd.read_sql_query(sql='SELECT * FROM fe where code=004532', con=conn, index_col='id')

print df.head()


conn.close()