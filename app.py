from feedgen.feed import FeedGenerator
from flask import make_response
from flask import Flask, Response, send_from_directory
from dateparser import parse

# Create the flask server
app = Flask(__name__)

downloads = [
    {
        'survey_name': "Labour force Survey", 
        'survey_id': "LFS-9243402-LM" , 
        'survey_counter': 45, 
        'url': 'www.google.ca',
        'downloads_date': "2019-02-20", 
    },
    {
        'survey_name': "Simulation Base Model", 
        'survey_id': "SMPD/S" , 
        'survey_counter': 89, 
        'url': 'www.google.ca',
        'downloads_date': "2019-02-20", 
    },
    {
        'survey_name': "College graduate", 
        'survey_id': "GDS-02384-2004" , 
        'survey_counter': 145, 
        'url': 'www.google.ca',
        'downloads_date': "2019-02-20", 
    }
]


@app.route('/rss')
def rss():
    fg = FeedGenerator()
    fg.title('Feed title')
    fg.description('Feed description')
    fg.link(href='https://awesome.com')

    for survey in downloads: 
        fe = fg.add_entry()
        fe.title(survey['survey_name'])
        fe.link(href=survey['url'])
        fe.guid(survey['survey_id'], permalink=False) # Or: fe.guid(survey.url, permalink=True)
        fe.pubDate(parse(survey['downloads_date'], settings={'TIMEZONE': 'US/Eastern', 'RETURN_AS_TIMEZONE_AWARE': True}))

    response = make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')

    return response

if __name__ == '__main__':
    app.debug=True
    app.run()