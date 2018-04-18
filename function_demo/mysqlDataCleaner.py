# -*- coding:utf-8 -*-
import pymysql
# reload(sys)
# sys.setdefaultencoding('utf-8')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fund', charset='utf8')
cur = conn.cursor()
# for num in range(1,2):
for num in range(1,2395858):
    sql_text_front = 'select code,accumulated,date from fund_eastmoney where id = %s'
    cur.execute(sql_text_front,(str(num),))
    # print cur.fetchone()
#get accumolated price on last trading day
    # unistr = int(basestring.encode('utf-8'))
    results_front = cur.fetchone()
    if results_front is None:
        continue
    code_front = results_front[0].encode('utf-8')
    accumulated_front = results_front[1].encode('utf-8')
    date_front = results_front[2]
#get accumolated price on current trading day
    sql_text_current = 'select code,accumulated,date from fund_eastmoney where code = %s and date > %s order by date asc'
    cur.execute(sql_text_current, (code_front, str(date_front)))
    results_current = cur.fetchone()
    code_current = results_current[0].encode('utf-8')
    accumulated_current = results_current[1].encode('utf-8')
    date_current = results_current[2]
#insert enhance data
    try:
        enhance = float(accumulated_current) / float(accumulated_front) - 1
    except ValueError:
        log_out = str(date_current) + '日基金代码' + code_current + '累计净值为空'
        print log_out
        logfile = open('/Users/liyuhe/PycharmProjects/blquant/logs/mysqlDataCleaner.log', 'a')
        logfile.writelines('id:' + str(num) + '\t\t\t' + log_out + '\n')
    if enhance > 0.1:
        enhance_normalization = 2
    elif 0 < enhance <= 0.1:
        enhance_normalization = 1
    elif -0.1 < enhance <= 0:
        enhance_normalization = -1
    elif -0.2 < enhance:
        enhance_normalization = -2
    sql_insert = 'update fund_eastmoney_enhance set enhance = %s,enhance_normalization = %s where code = %s and date = %s '
    cur.execute(sql_insert,(enhance, enhance_normalization, code_current, str(date_current)))
    conn.commit()
    print num

conn.close()