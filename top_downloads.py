__version__ = '0.1.0'

#Python Standard library
import datetime
import json

#Python packages to be installed
from dateparser import parse

from odesi_queries import sql_query_top_downloads_on_odesi_for_last_month
from query_helper import execute_this_query
from query_helper import get_connection
from query_helper import clean_decimal_data
from sp_utils import read_json_file
from sp_utils import save_result_in_json_file

def get_date(this_date):
    """[summary]

    Keyword Arguments:
        this_date {[type]} -- [description] (default: {parse('1 month ago')})

    Returns:
        [type] -- [description]
    """
    this_date = parse('1 month ago')
    month = this_date.month
    year = str(this_date.year)

    return [year, month, day]

def get_top_10_odesi_downloads_for_this_month():
    """[summary]
    """
    this_date = datetime.doday
    year, month, day = get_date(this_date)
    sql = sql_query_top_downloads_on_odesi_for_last_month( year, month, qty=20)
    
    file_content =read_json_file("secrets.json")
    connection = get_connection(file_content)

    data = execute_this_query(connection, sql)
    data = clean_decimal_data(data)

    return data

if __name__ == '__main__':
    data = get_top_10_odesi_downloads_for_this_month
    save_result_in_json_file(data, filename="downloads.json")


