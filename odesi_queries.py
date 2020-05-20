__author__ = "Carlos McGregor and Guinsly Mondésir"

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




