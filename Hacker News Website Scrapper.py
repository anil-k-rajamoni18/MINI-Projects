#programicatlly using the laguage to grabbing the data from the website
# uses:
# recruitment
# sales Leads
# marketing
# real estate
# automotive
# banking
# finance
# search engine optimization
# social media
# E-commerce

# Reduce a lot of time 
# Most websites don't want to scrap the data 
# sometime it's illegal 

# ---- Before the Web Scrapping Check the robots.txt----#


import requests

from bs4 import BeautifulSoup

import pprint

res=requests.get('https://news.ycombinator.com/news')

res2=requests.get('https://news.ycombinator.com/news?p=2')


# print(res.json)

soup=BeautifulSoup(res.text,'html.parser')

soup2=BeautifulSoup(res2.txt,'html.parser')

# print(soup.body.contents)

# print(soup.find_all('div'))


# print(soup.find_all('a'))

# print(soup.title)

# print(soup.head)

# print(soup.a)

# print(soup.find(id="score_25415172"))

link=soup.select(".storylink")
subtext=soup.select('.subtext')


link2=soup2.select(".storylink")
subtext2=soup2.select('.subtext')


mega_links=link+link2
mega_subtext=subtext+subtext2
# for idx,item in enumerate(link):
#     print(item)

# print(link[0].getText())

# print(votes)


def sort_stories_by_votes(hn):
    return sorted(hn,key=lambda k:k['vote'],reverse=True)


def create_custom_hn(links,subtext):
    hn=[]
    for idx,item in enumerate(links):
        title=item.getText()
        href=item.get('href',None)
        
        vote=subtext[idx].select('.score')

        if len(vote): #if has length
            points=int(vote[0].getText().replace('points',""))
            print(points)
            if points>99:

                hn.append({'title':title,'link':href,'vote':points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))









# https://www.udemy.com/robots.txt
# https://www.airbnb.co.in/robots.txt
# https://news.ycombinator.com/robots.txt



