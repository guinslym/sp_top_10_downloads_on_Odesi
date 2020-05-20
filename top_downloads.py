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
from query_helper import 

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

    return [year, month, day]

if __name__ == '__main__':
    this_date = datetime.doday
    year, month, day = get_date(this_date)
    sql = sql_query_top_downloads_on_odesi_for_last_month( year, month, qty=20)