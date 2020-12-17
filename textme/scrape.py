#WEB SCRAPPING/HACKER NEWS PROJECT TO GET TWO PAGES OF THE HACKER NEWS WEBSITE
#Using robots.txt to check the terms and conditions of the website you want to scrap/ Googlebots
#Check out this link--->https://www.synerzip.com/blogs/web-scraping-introduction-applications-and-best-practices/#:~:text=Web%20scraping%20typically%20extracts%20large,show%20data%20from%20a%20website.
#Check out this link too--->https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Check out this link on BeautifulSoup selectors--->https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
#Check out this link on pprint--->https://docs.python.org/3/library/pprint.html
import requests #the requests allows us to download dat from the html
from bs4 import BeautifulSoup #bs4 allows us to use the html and grab diff data
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

#scrapy can also help you scrape a website..
#Scrapy also helps one to get access to databases and use that data related to eg. PostgresSQL etc.
#SCRAPY WEBSITE--->https://scrapy.org/