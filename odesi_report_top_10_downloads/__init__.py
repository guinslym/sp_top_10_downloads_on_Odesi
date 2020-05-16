__version__ = '0.1.0'
__author__ = "Carlos McGregor and Guinsly Mondésir"

from feedgen.feed import FeedGenerator
#https://feedgen.kiesow.be/#installation
from dateparser import parse
import pymysql
import pymysql.cursors


from environs import Env
env = Env()
# Read .env into os.environ
env.read_env()

#Constant
# environment = env("ENVIRONMENT", "STAGING")
# if environment == "STAGING":

this_date = parse('1 month ago')
month = this_date.month
year = str(this_date.year)



sql2 = """SELECT left(S.survey_name, 100 )AS 'Survey', left(S.survey_id, 100) AS 'Survey ID', SUM(counter) AS 'Download Count', LEFT(MAX(D1.date), 7) AS 'Month' FROM OdesiDailyAccess AS O1 INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id LEFT JOIN Surveys AS S ON S.id=O1.survey_id WHERE D1.date LIKE '{0}-{1}-%' AND O1.mode_id=5 AND O1.execute_download=True GROUP BY O1.survey_id ORDER BY SUM(counter) DESC LIMIT 10;""".format(year, f'{month:02d}')

#for pymysql query needs to be on one line
sql2 = """SELECT left(S.survey_name, 40 )AS 'Survey', left(S.survey_id, 20) AS 'Survey ID', SUM(counter) AS 'Download Count', LEFT(MAX(D1.date), 7) AS 'Month' FROM OdesiDailyAccess AS O1 INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id LEFT JOIN Surveys AS S ON S.id=O1.survey_id WHERE D1.date LIKE '2020-02-%' AND O1.mode_id=5 AND O1.execute_download=True GROUP BY O1.survey_id ORDER BY SUM(counter) DESC LIMIT 10;"""

# connection = pymysql.connect(
#     user=env("USER"),
#     password=env("PASSWORD"),
#     db=env("DATABASE"),
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor
#     )



with connection.cursor() as cursor:
    # Read a single record
    cursor.execute(sql2, )
    result = cursor.fetchall()
    print(result)



