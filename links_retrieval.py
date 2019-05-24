from requests_html import HTML , HTMLSession
import numpy as np
links = ['http://www.espncricinfo.com/ipl/engine/series/313494.html','http://www.espncricinfo.com/ipl2009/engine/series/374163.html','http://www.espncricinfo.com/ipl2010/engine/series/418064.html',
			'http://www.espncricinfo.com/ipl2010/engine/series/418064.html','http://www.espncricinfo.com/indian-premier-league-2011/engine/series/466304.html',
			'http://www.espncricinfo.com/indian-premier-league-2012/engine/series/520932.html','http://www.espncricinfo.com/indian-premier-league-2013/engine/series/586733.html',
			'http://www.espncricinfo.com/indian-premier-league-2014/engine/series/695871.html','http://www.espncricinfo.com/indian-premier-league-2015/engine/series/791129.html',
			'http://www.espncricinfo.com/indian-t20-league-2016/engine/series/968923.html','http://www.espncricinfo.com/indian-premier-league-2017/engine/series/1078425.html',
			'http://www.espncricinfo.com/ci/engine/series/1131611.html'
			]
scorecard_links =[]
for link in links:
	session = HTMLSession()
	r = session.get(link)
	a = r.html.find('.reports-list.content_link')
	for b in a:
    			c = b.find('.potMatchMenuLink',first=True)
    			d=c.links
    			(scorecard_link,) = d
    			scorecard_links.append(scorecard_link)
    			print(scorecard_link)

print(scorecard_links)