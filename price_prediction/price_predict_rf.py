import datetime
import numpy as np
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# ser = pd.Series(np.arange(3.))

# data = pd.DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
#
# print data.head()
#
#


# make train data frame and test data frame(get data from mysql)

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fund', charset='utf8mb4')

all_df = pd.read_sql_query(
    sql='SELECT invest_style,date,unit,accumulated,five,ten,twenty,forty,sixty,enhance_normalization FROM fund_eastmoney_enhance where code=004532',
    con=conn, index_col='date')

# print df.head()

conn.close()

# x = train_df[['unit', 'accumulated', 'five', 'ten', 'twenty', 'forty', 'sixty']]
x = all_df[['unit', 'accumulated', 'five', 'ten', 'twenty', 'forty', 'sixty']]
y = all_df['enhance_normalization']

# split data into train df and test df by date

start_test_date = datetime.date(2017,11,1)

# Create training and test sets
X_train = x[x.index < start_test_date]
X_test = x[x.index >= start_test_date]
Y_train = y[y.index < start_test_date]
Y_test = y[y.index >= start_test_date]




# random forest classifier parameters
rf_models = ('RF', RandomForestClassifier(
    n_estimators=1000, criterion='gini',
    max_depth=None, min_samples_split=2,
    min_samples_leaf=1, max_features='auto',
    bootstrap=True, oob_score=False, n_jobs=1,
    random_state=None, verbose=0)
             )
# Train each of the models on the training set
rf_models[1].fit(X_train, Y_train)
# Make an array of predictions on the test set
pred = rf_models[1].predict(X_test)

# Output the hit-rate and the confusion matrix for each model
print("%s:\n%0.3f" % (rf_models[0], rf_models[1].score(X_test, Y_test)))
# print("%s:\n%0.3f" % (rf_models[0], rf_models[1].oob_score_))
print("%s\n" % confusion_matrix(pred, Y_test))


