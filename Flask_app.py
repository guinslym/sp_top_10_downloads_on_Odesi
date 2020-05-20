# Python Standard library
import json

# Flask package
from flask import make_response
from flask import Flask, Response, send_from_directory

# Other Python external packages
from feedgen.feed import FeedGenerator
from dateparser import parse

# Create the flask server
app = Flask(__name__)

def get_top_downloads(filename = "downloads.json"):
    """[summary]

    Returns:
        [type] -- [description]
    """
    try:
        with open(filename) as json_file:
            downloads = json.load(json_file)
        return downloads
    except:
        return False


def get_feed_object():
    """[summary]

    Returns:
        [type] -- [description]
    """
    fg = FeedGenerator()
    fg.title('Odesi top downloads for last month')
    fg.description('Retrieving at least the top 10 downloads in Odesi during last month')
    fg.link(href='https://odesi.ca')

    return fg

@app.route('/rss')
def rss():
    """[summary]

    Returns:
        [type] -- [description]
    """
    fg = get_feed_object()
    downloads = get_top_downloads()

    if downloads:

        url_root = "https://search1.odesi.ca/#/search/_term_term="
        for survey in downloads[:20]: 
            fe = fg.add_entry()
            fe.title(survey['Survey'] + " : Total downloads -> " + str(survey['Download Count']))
            #replace all underscore
            survey_id_updates = (survey['Survey ID']).replace("_", "/_")
            fe.link(href= (url_root + survey_id_updates))

            fe.guid(survey['Survey ID'], permalink=False) # Or: fe.guid(survey.url, permalink=True)
            fe.pubDate(parse(survey['Month'], settings={'TIMEZONE': 'US/Eastern', 'RETURN_AS_TIMEZONE_AWARE': True}))

        response = make_response(fg.rss_str())
        response.headers.set('Content-Type', 'application/rss+xml')

        return response
    else:
        #redirect 500
        return response

if __name__ == '__main__':
    app.debug=True
    app.run()