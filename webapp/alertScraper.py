# -*- coding: utf-8 -*-
"""
pasted into spyder on Tue Apr  2 09:50:34 2019

@author: Jessie
"""

#Code for scraping alerts from dublin bikes website about station closures

from bs4 import BeautifulSoup
import urllib.request
import json

#scrape current links of dublin bike alerts from webpage and place in array
resp = urllib.request.urlopen("http://www.dublinbikes.ie/Magazine/News")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
listOfLinks = []
for line in soup.find_all('a', href=True):
    links = str(line['href'])
    if links not in listOfLinks:#was many duplicates of same link
        listOfLinks.append(links)

#remove useless links, and complete links for useful ones 
i = 0
listlength = len(listOfLinks) - 1
while i < listlength:
    if listOfLinks[i].startswith("/Magazine/News") and "offset" not in listOfLinks[i]:
        temp = "http://www.dublinbikes.ie" + listOfLinks[i]
        listOfLinks[i] = temp
    else:
        listOfLinks[i] = 0
    i += 1

for i in listOfLinks:
    if i == 0:
        listOfLinks.remove(i)

#first item in array is overall link to page, not articles in page so remove
listOfLinks.pop(0)
listOfLinks = listOfLinks[:-14]
alerts = {}
for currentLink in listOfLinks[:10]:
    response = urllib.request.urlopen(currentLink)
    articlesoup = BeautifulSoup(response, from_encoding=resp.info().get_param('charset'))
    #seperate out title from file
    title = articlesoup.find("h3",{"class":"titr_aricle"}).get_text()#.get_text() removes html tags 
    #seperate out text from file
    desc = articlesoup.find("div",{"class":"desc_article"}).get_text() 
    alerts[title] = desc
#print(alerts)
    
#change list with scraped alerts to JSON file for web use
dbAlerts = json.dumps(alerts)




#Code for scraping alerts from aa roadwatch twitter about road closures or incidents

resp = urllib.request.urlopen("https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
dublinTweetsList = []
for line in soup.find_all("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
    currentTweet = line.get_text()
    if currentTweet.startswith("#DUBLIN"):
        dublinTweetsList.append(currentTweet)
#print(dublinTweetsList)

#change dict with roadwatch alerts to json file for web use
aaAlerts = json.dumps(dublinTweetsList)