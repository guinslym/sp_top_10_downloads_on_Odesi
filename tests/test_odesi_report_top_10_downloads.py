
from top_downloads import get_top_10_odesi_downloads_for_this_month
from top_downloads import get_date

from odesi_queries import sql_query_top_downloads_on_odesi_for_last_month

from query_helper import execute_this_query
from query_helper import get_connection
from query_helper import clean_decimal_data

from sp_utils import read_json_file
from sp_utils import save_result_in_json_file

def test_version():
    assert __version__ == '0.1.0'
