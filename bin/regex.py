# for connecting to sqllite3
import sqlite3

con = sqlite3.connect('mydb.sqlite3')  # if the database is not present then it will create one.

#  in order to connect to mysql
# import pymysql
# con = pymysql.connect(user='', password='', host='', port='', database='')

cur = con.cursor()  # cursor is used to create connection.
query = '''CREATE TABLE IF NOT EXISTS LOGDATA(
            IP VARCHAR(100),
            DATE VARCHAR(100),
            PICS VARCHAR(100),
            URL VARCHAR(100))'''

cur.execute(query)  # executes the query.

import urllib.request as u  # library to access the data of a website

myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'
f = u.urlopen(myurl)

import re  # this package helps in pattern matching.
done = False
if done:
    for line in f:
        # print(line)
        # print(type(line))  # it is in bytes, so we have to convert it to string.
        # line = line.decode()
        # print(type(line))
        line = line.decode()
        # or also m = re.match('\d\d\d\.\d\d\d\.\d\d\d.\d\d\d') # . --> any character and [.] --> dot only \d --> any digit
        # \D --> non-digit.
        m = re.match(
            '(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http://\S+)</A>.*',
            line)  # [0-9] is same as \d.  * --> 0 or more
        #  + --> 1 or more, ? --> 0 or 1. we used ? before as non greedy operator without it only minimum digits will be selected.
        # ?: --> NOT CAPTURE, will not be grouped as group 3. \s --> represents space. \S --> non space \w -->word character --> [a-zA-Z0-9_] \W --> non word character.
        if m != None:
            ip = m.group(1)
            dt = m.group(2)
            im = m.group(3)
            if im == None:
                im = 'No Image.'
            wb = m.group(4)
            print(ip)
            print(dt)
            print(im)
            print(wb)
            query = f"INSERT INTO LOGDATA VALUES('{ip}', '{dt}', '{im}', '{wb}')"
            print(query)
            cur.execute(query)

    con.commit()
cur.execute('SELECT * FROM LOGDATA')
result = cur.fetchall()  # cursor will execute the query but doesnot returns so to return we use fetchall().
print('result = ', result)

import csv
f = open('dbdump.csv', 'w', newline='')
wt = csv.writer(f)
wt.writerow(['IP', 'DATE', 'PICS', 'URL'])
for each_row in result:
    wt.writerow(each_row)
f.close()

# ----------------------------------------------------------------------------------------------------------------------

f = open('dbdump.csv')
rdr = csv.reader(f)
csv_out = list(rdr)
print('csv_out = ', csv_out)

# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd
df1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index =['r1','r2'], columns = ['c1', 'c2', 'c3'])
print(df1)

L1 = list([[10, 20, 30], [40, 50, 60]])
print(L1)

df2 = pd.DataFrame(result)
print(df2)

df2.to_csv('out3.csv', index=None, header=['IP', 'DATE', 'PICS', 'URL'])

cur.execute('SELECT * FROM LOGDATA')
df3=pd.DataFrame(cur)
df3.to_csv('out4.csv')
df3.to_excel('out5.xlsx')
df3.to_json('out6.json')

df4 = df3.T
df4.to_json('out6.json')
