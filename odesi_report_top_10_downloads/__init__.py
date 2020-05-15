__version__ = '0.1.0'
from feedgen.feed import FeedGenerator

from dateparser import parse

#https://feedgen.kiesow.be/#installation


def get_top_10_downloads_from_last_month():
    this_date = parse('1 month ago')
    query =  """
        SELECT 
            left(S.survey_name, 60 )AS "Survey", 
            left(S.survey_id, 40) AS "Survey ID", 
            SUM(counter) AS "Download Count", 
            LEFT(MAX(D1.date), 7) AS "Month" 
        FROM OdesiDailyAccess AS O1 
            INNER JOIN Dates AS D1 ON O1.date_id=D1.date_id 
            LEFT JOIN Surveys AS S ON S.id=O1.survey_id 
        WHERE 
            D1.date LIKE "2020-02-%" 
            AND 
            O1.mode_id=5 
            AND 
            O1.execute_download=True 
        GROUP BY O1.survey_id 
        ORDER BY SUM(counter) 
        DESC LIMIT 10;
        """
    return query