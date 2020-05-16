from feedgen.feed import FeedGenerator
from flask import make_response
from flask import Flask, Response, send_from_directory
from dateparser import parse
import json

import pymysql
import pymysql.cursors

from environs import Env
env = Env()

with open('secrets.json') as json_file:
        data = json.load(json_file)

user = data["USER"]
password = data["PASSWORD"]
db = data["DATABASE"]


# Create the flask server
app = Flask(__name__)

def get_top_downloads():
    # Read .env into os.environ
    env.read_env()
    environment = env("ENVIRONMENT", "STAGING")

    if environment == "STAGING":
        with open('downloads.json') as json_file:
            downloads = json.load(json_file)
    else:
        raise ValueError('A very specific bad thing happened')# throw error 
    return downloads

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/rss')
def rss():
    fg = FeedGenerator()
    fg.title('Odesi top downloads for last month')
    fg.description('Retrieving at least the top 10 downloads in Odesi during last month')
    fg.link(href='https://odesi.ca')

    downloads = get_top_downloads()
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

if __name__ == '__main__':
    app.debug=True
    app.run()