__version__ = '0.1.0'
__author__ = "Carlos McGregor and Guinsly Mondésir"

from feedgen.feed import FeedGenerator
#https://feedgen.kiesow.be/#installation
from dateparser import parse
import pymysql
import pymysql.cursors

from freezegun import freeze_time
import datetime
from decimal import *

import json

with open('secrets.json') as json_file:
        data = json.load(json_file)

user = data["USER"]
password = data["PASSWORD"]
db = data["DATABASE"]

#Constant
# environment = env("ENVIRONMENT", "STAGING")
# if environment == "STAGING":


def get_top_downloads_on_odesi_for_last_month(year, month, qty=10):
    #for pymysql query needs to be on one line
    sql = """SELECT S.survey_name AS 'Survey', S.survey_id AS 'Survey ID', SUM(counter) AS 'Download Count', LEFT(MAX(D1.date), 7) AS 'Month' FROM OdesiDailyAccess AS O1 INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id LEFT JOIN Surveys AS S ON S.id=O1.survey_id WHERE D1.date LIKE '{0}-{1}-%' AND O1.mode_id=5 AND O1.execute_download=True GROUP BY O1.survey_id ORDER BY SUM(counter) DESC LIMIT {2};""".format(year, f'{month:02d}', qty)
    
    return sql

with freeze_time("2020-03-14"):
    this_date = parse('1 month ago')
    month = this_date.month
    year = str(this_date.year)

sql = get_top_downloads_on_odesi_for_last_month( year, month, qty=20)

# Connect to the database   
try:
    connection = pymysql.connect(
        user=user,
        password=password,
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
    print("connection is working")
except:
    print("connection not working ")
    print("user:{0}\npass:{1}\ndb:{2}\n".format(user, password, db))

with connection.cursor() as cursor:
    # Read a single record
    cursor.execute(sql, )
    result = cursor.fetchall()
    print(result)

for data in result:
    data['Download Count'] = int(data['Download Count'])

with open('downloads.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

#TODO ---Load json
#TODO ---Add it to Feedgen
#TODO ----Change limit 10 to 30
#TODO ------Work with Environment variables instead
#TODO Load to DOCKER to connect to DB
#           #WHY: 
#TODO Load to DOCKER for app.py (Flask)
#TODO ----create package for top 10 downloads
#TODO quick quick KSKS