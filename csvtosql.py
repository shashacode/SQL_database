import csv
import pandas as pd

data = pd.read_csv (r'C:\Users\fresh\Documents\Overall python\coding\coviddata.csv', encoding = "unicode_escape")   
# df = pd.DataFrame(data, columns= ['Location','cases','deaths', 'recoveries'])

# print(df)

import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        db='covid19',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()

# cursor.execute('CREATE TABLE covid20(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Location VARCHAR(50), cases INT(30), deaths INT(30), recoveries INT(30) )')
 

for _, row in data.iterrows():
    # print(row)
    Location, cases, deaths, recoveries = row
    with conn.cursor() as cursor: 
        # Create a new record
        sql = f"INSERT INTO covid20 (Location, cases, deaths, recoveries) VALUES('{Location}',{cases},{deaths},{recoveries})"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()
