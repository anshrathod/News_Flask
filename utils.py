from datetime import date as dt,timedelta

def getnews(newsid,fromdate,todate,searchterm = None):
	from newsapi import NewsApiClient
	newsapi = NewsApiClient(api_key='e442517dd5d3486b8e2fa0b9674edfd4')
	all_articles = newsapi.get_everything(sources=newsid,
					      domains='bbc.co.uk,techcrunch.com',
	                                      from_param=fromdate,
	                                      to=todate,
	                                      language='en',
	                                      sort_by='relevancy'
	                                  	  )
	print(len(all_articles['articles']))
	# sources = sources['name']
	author,title,desc,url,imgurl,date,content,time=[],[],[],[],[],[],[],[]
	articles=all_articles["articles"]
	for i in range(len(articles)):
		if searchterm:
			if articles[i]['author'] and articles[i]['title'] and articles[i]['description'] and articles[i]['url'] and articles[i]['urlToImage'] and articles[i]['publishedAt'] and articles[i]['content']:
				if searchterm.upper() in articles[i]['title'].upper() or searchterm.upper() in articles[i]['description'].upper() or searchterm.upper() in articles[i]['content'].upper():
					author.append(articles[i]['author'])
					title.append(articles[i]['title'])
					desc.append(articles[i]['description'])
					url.append(articles[i]['url'])
					imgurl.append(articles[i]['urlToImage'])
					time.append(articles[i]['publishedAt'][11:-1])
					content.append(articles[i]['content'][:-20])
					date.append(articles[i]['publishedAt'][:-10])
		else:
			if articles[i]['author'] and articles[i]['title'] and articles[i]['description'] and articles[i]['url'] and articles[i]['urlToImage'] and articles[i]['publishedAt'] and articles[i]['content']:
				author.append(articles[i]['author'])
				title.append(articles[i]['title'])
				desc.append(articles[i]['description'])
				url.append(articles[i]['url'])
				imgurl.append(articles[i]['urlToImage'])
				time.append(articles[i]['publishedAt'][11:-1])
				content.append(articles[i]['content'][:-20])
				date.append(articles[i]['publishedAt'][:-10])
	articlelist = zip(title,content,time,imgurl,url,author,desc,date)
	return articlelist