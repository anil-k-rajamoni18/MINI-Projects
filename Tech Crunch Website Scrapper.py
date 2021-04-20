
import requests

from bs4 import BeautifulSoup

import pprint


res=requests.get('https://techcrunch.com/')

# print(res.text)

soup=BeautifulSoup(res.text,'html.parser')

# print(soup.find_all('div'))

links=soup.select('.post-block__title')
# print(links[0].getText())

href=soup.select('a.post-block__title__link')
tc=[]
for idx,post in enumerate(links):
    title=links[idx].getText()
    title=" ".join(title.strip().split(","))
    href_link=href[idx].get('href',None)
    tc.append({"title":title,"url":href_link})

pprint.pprint(tc)



# scrapy-a framework



