from decimal import *
import pymysql
import pymysql.cursors

def clean_decimal_data(result):
    """Convert Decimal(number) object to int

    Arguments:
        data {list of dict} -- List of Dict containing top downloads

    Returns:
        list -- list of dict
    """
    #convert Decimal to Int Type
    new_result = []
    for data in result:
        data['Download Count'] = int(data['Download Count'])
        new_result.append(data)

    return new_result

def get_connection(data):
    """Connect to db

    Arguments:
        data {dict} -- dict of credentials to connect to db

    Returns:
        pymsqlConnection -- connection to database
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

def execute_this_query(connection, sql):
    """sql command to execute in db

    Arguments:
        connection {Connection} -- Connection to database
        sql {string} -- sql querry

    Returns:
        List of dict -- list of result found from the database query
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
