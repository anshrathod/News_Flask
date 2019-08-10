from flask import Flask, render_template, url_for
from utils import getnews
from datetime import date as dt,timedelta

app = Flask(__name__)

posts=[{
    
}]

@app.route("/")
@app.route("/home")
def home():
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key='e442517dd5d3486b8e2fa0b9674edfd4')
    articlelists,srcs,sourceid=[],[],[]
    print('main')
    today = str(dt.today())
    sources = newsapi.get_sources()
    sources = sources['sources']
    for i in range(len(sources)):
        srcs.append(sources[i]['name'])
        sourceid.append(sources[i]['id'])
    sources = zip(srcs,sourceid)
    sourceids = ','.join(sourceid)
    print(sourceids)
    # for i in sourceid:
    #     print(i)
    articlelists = getnews(sourceids,today,today)
        # for j in articlelist:
        #     articlelists.append(j)
    # print(len(articlelists))
    return render_template('news.html',sources=sources,articlelist=articlelists)

@app.route("/<string:newsid>/")
def givespecificnews(newsid):
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key='e442517dd5d3486b8e2fa0b9674edfd4')
    articlelists,srcs,sourceid=[],[],[]
    print('specific')
    today = str(dt.today())
    monthago = str((dt.today() - timedelta(1*365/12)).isoformat())
    sources = newsapi.get_sources()
    sources = sources['sources']
    for i in range(len(sources)):
        srcs.append(sources[i]['name'])
        sourceid.append(sources[i]['id'])
    sources = zip(srcs,sourceid)
    articlelists = getnews(newsid,today,monthago)
    return render_template('news.html',sources=sources,articlelist=articlelists,newsid=newsid)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)