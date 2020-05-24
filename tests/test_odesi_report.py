from dateparser import parse

from decimal import Decimal
import pytest

from freezegun import freeze_time
import datetime

import pymysql
import pymysql.cursors

from top_downloads import __version__
from top_downloads import get_top_10_odesi_downloads_for_this_month
from top_downloads import get_date

from odesi.odesi_queries import sql_query_top_downloads_on_odesi_for_last_month

from odesi.query_helper import execute_this_query
from odesi.query_helper import get_connection
from odesi.query_helper import clean_decimal_data

from odesi.sp_utils import read_json_file
from odesi.sp_utils import save_result_in_json_file

ROOT_DIR = "/root/sp_odesi/"

def test_version():
    assert  __version__ == '0.1.4'

class TestTopDownloadsGetDate(object):

    @freeze_time("2020-03-14")
    def test_get_date_year(self):
        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        assert year == this_day.year

    def test_get_date_month(self):
        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        assert month == this_day.month

    def test_get_date_day(self):
        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        assert day == this_day.day

class TestTopDownloads(object):

    @freeze_time("2020-03-14")
    def setUp(self):
        self.this_day = datetime.datetime.now()
        self.year, self.month, self.day = get_date(self.this_day)

    def test_get_top_10_odesi_downloads_for_this_month(self):
        pass

class TestOdesiQueries:

    @freeze_time("2020-03-14")
    def test_sql_query_top_downloads_on_odesi_for_last_month(self):
        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        qty = 20
        query = sql_query_top_downloads_on_odesi_for_last_month(year, month, qty)
        assert query == """SELECT S.survey_name AS 'Survey', S.survey_id AS 'Survey ID', SUM(counter) AS 'Download Count', LEFT(MAX(D1.date), 7) AS 'Month' FROM OdesiDailyAccess AS O1 INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id LEFT JOIN Surveys AS S ON S.id=O1.survey_id WHERE D1.date LIKE '{0}-{1}-%' AND O1.mode_id=5 AND O1.execute_download=True GROUP BY O1.survey_id ORDER BY SUM(counter) DESC LIMIT {2};""".format(year, f'{month:02d}', qty)

@freeze_time("2020-03-14")
class TestOdesiQueryHelper(object):
    def test_execute_this_query(self):
        decimal_0, decimal_1 = [Decimal(23),Decimal(45)]
        result = [
            {'Download Count':decimal_0},
            {'Download Count':decimal_1}
                  ]
        data = clean_decimal_data(result)
        assert data[0]['Download Count'] == 23

    def test_get_connection(self):
        file_content =read_json_file(ROOT_DIR+"secrets.json")
        connection = get_connection(file_content)
        assert isinstance(connection, pymysql.connections.Connection)

    @freeze_time("2020-02-14")
    def test_clean_decimal_data(self):
        file_content =read_json_file(ROOT_DIR+"secrets.json")
        connection = get_connection(file_content)

        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        sql = sql_query_top_downloads_on_odesi_for_last_month( year, month, qty=20)
        
        data = execute_this_query(connection, sql)
        assert isinstance(data[0]['Download Count'], Decimal)

        data = clean_decimal_data(data)
        assert isinstance(data[0]['Download Count'], int)


class TestDBConnectionFromDocker(object):
    
    @freeze_time("2020-02-14")
    def test_execute_this_query(self):
        file_content =read_json_file(ROOT_DIR+"secrets.json")
        connection = get_connection(file_content)

        this_day = datetime.datetime.now()
        year, month, day = get_date(this_day)
        sql = sql_query_top_downloads_on_odesi_for_last_month( year, month, qty=20)
        
        data = execute_this_query(connection, sql)
        assert isinstance(data, list)
        assert isinstance(data[0], dict)

class TestSPUtils(object):
    def test_read_json_file(self):
        with pytest.raises(Exception):
            read_json_file("hello-wolrd")

    def test_read_json_file_content(self):
            data = read_json_file(ROOT_DIR+"secrets.json")
            assert "usser" in data.keys()

    def test_save_result_in_json_file(self):
        pass