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

class TestTopDownloads(object):
    def test_get_date(self):
        pass
    def test_get_top_10_odesi_downloads_for_this_month(self):
        pass

class TestOdesiQueries:
    def test_sql_query_top_downloads_on_odesi_for_last_month(self):
        pass

class TestOdesiQueryHelper(object):
    def test_execute_this_query():
        assert True
    def test_get_connection():
        assert True
    def test_ clean_decimal_data():
        assert True

class SPUtils():
    def test_read_json_file():
        pass
    def test_save_result_in_json_file():
        pass