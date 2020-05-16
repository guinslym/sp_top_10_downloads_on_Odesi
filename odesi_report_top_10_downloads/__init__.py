__version__ = '0.1.0'
__author__ = "Carlos McGregor and Guinsly Mondésir"

from feedgen.feed import FeedGenerator
#https://feedgen.kiesow.be/#installation

from dateparser import parse

import pymysql.cursors
import pymysql

# Connect to the database
try:
    connection = pymysql.connect(
        host='localhost',
        user='user',
        password='passwd',
        db='db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
except:
    pass
#https://stackoverflow.com/a/34503728/2581266

def get_query_for_the_top_10_downloads_from_last_month():
    
    this_date = parse('1 month ago')
    month = this_date.month
    year = str(this_date.year)

    query =  """
        SELECT 
            left(S.survey_name, 60 )AS "Survey", 
            left(S.survey_id, 40) AS "Survey ID", 
            SUM(counter) AS "Download Count", 
            LEFT(MAX(D1.date), 7) AS "Month" 
        FROM OdesiDailyAccess AS O1 
            INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id 
            LEFT JOIN Surveys AS S ON S.id=O1.survey_id 
        WHERE 
            D1.date LIKE "{0}-{1}-%" 
            AND 
            O1.mode_id=5 
            AND 
            O1.execute_download=True 
        GROUP BY O1.survey_id 
        ORDER BY SUM(counter) 
        DESC LIMIT 10;
        """.format(year, f'{month:02d}')
    return query