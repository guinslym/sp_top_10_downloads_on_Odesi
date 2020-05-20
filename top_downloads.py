__version__ = '0.1.0'
__author__ = "Carlos McGregor and Guinsly Mondésir"

#Python Standard library
import datetime
from decimal import *
import json

#Python packages to be installed
from dateparser import parse
import pymysql
import pymysql.cursors

def get_top_downloads_on_odesi_for_last_month(year, month, qty=10):
    """[summary]

    Keyword Arguments:
        year {[type]} -- [description] 
        month {[type]} -- [description] 
        qty {[type]} -- [description] (default: 10)})

    Returns:
        [type] -- [description]
    """
    # pymysql query needs to be in one line
    sql = """SELECT S.survey_name AS 'Survey', S.survey_id AS 'Survey ID', SUM(counter) AS 'Download Count', LEFT(MAX(D1.date), 7) AS 'Month' FROM OdesiDailyAccess AS O1 INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id LEFT JOIN Surveys AS S ON S.id=O1.survey_id WHERE D1.date LIKE '{0}-{1}-%' AND O1.mode_id=5 AND O1.execute_download=True GROUP BY O1.survey_id ORDER BY SUM(counter) DESC LIMIT {2};""".format(year, f'{month:02d}', qty)
    
    return sql

def get_date(this_date = parse('1 month ago')):
    """[summary]

    Keyword Arguments:
        this_date {[type]} -- [description] (default: {parse('1 month ago')})

    Returns:
        [type] -- [description]
    """
    this_date = parse('1 month ago')
    month = this_date.month
    year = str(this_date.year)

    return [year, month]


def read_secrets(file="secrets.json"):
    """[summary]

    Keyword Arguments:
        file {str} -- [description] (default: {"secrets.json"})

    Returns:
        [type] -- [description]
    """
    try:
        #reading secrets.json to connect to db
        with open('secrets.json') as json_file:
                data = json.load(json_file)
        return data
    except:
        print( "File {0} not found".format(file))
        return False

def get_connection(data):
    """[summary]

    Arguments:
        data {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    user = data["USER"]
    password = data["PASSWORD"]
    db = data["DATABASE"]

    # Connect to the database using secrets.json 
    try:
        connection = pymysql.connect(
            user=user,
            password=password,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        print("connection is working")
        return connection
    except:
        print("user:{0}\npass:{1}\ndb:{2}\n".format(user, password, db))
        return False

def execute_this_query(connection):
    """[summary]

    Arguments:
        connection {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    try:
        #run the SQL query
        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql, )
            result = cursor.fetchall()
            print(result)
            return result
    except:
        print("error on query")
        return False

def clean_decimal_data(data):
    """[summary]

    Arguments:
        data {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    #convert Decimal to Int Type
    for data in result:
        data['Download Count'] = int(data['Download Count'])
    return data

def save_result_in_json_file(file="downloads.json"):
    """[summary]

    Keyword Arguments:
        file {str} -- [description] (default: {"downloads.json"})

    Returns:
        [type] -- [description]
    """
    try:
        #save the data in JSON file so that the Flask app can read it
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
    except:
        print("error on file creation")
        return False

if __name__ == '__main__':
    this_date = parse('1 month ago')
    get_date(this_date)
    sql = get_top_downloads_on_odesi_for_last_month( year, month, qty=20)