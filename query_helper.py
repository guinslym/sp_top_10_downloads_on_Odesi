from decimal import *
import pymysql
import pymysql.cursors

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