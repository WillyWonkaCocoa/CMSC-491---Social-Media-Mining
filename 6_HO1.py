import json
import requests
import html5lib
from bs4 import BeautifulSoup

search_term = 'twitterapi'

URL = 'https://mobile.twitter.com/search?q=' + search_term
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html5lib')
div_text = soup.find_all(class_="tweet-text")
for div in div_text:
    print div.text.encode('utf-8')
