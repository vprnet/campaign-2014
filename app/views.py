from index import app
from query import api_feed, reporter_list
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'Vermont Legislature'
    stories = api_feed([170839705], numResults=10, thumbnail=True)
    featured = api_feed([291752955, 292002570], numResults=2, thumbnail=True, sidebar=True)
    print featured
    reporters = reporter_list([170839705])

    social = {
        'title': "VPR: Vermont Legislature 2014",
        'subtitle': 'www.vpr.net/apps/legislature/',
        'img': 'http://mediad.publicbroadcasting.net/p/vpr/files/201401/statehouse-january.jpg',
        'description': "VPR's guide to the Vermont Legislature. Latest coverage, statehouse streams and legislative resources, all in one place.",
        'twitter_text': "VPR's guide to the VT legislature. Latest coverage, statehouse streams and legislative resources",
        'twitter_hashtag': 'VTpoli'
    }

    return render_template('content.html',
        page_title=page_title,
        stories=stories,
        social=social,
        featured=featured,
        reporters=reporters,
        page_url=page_url)
