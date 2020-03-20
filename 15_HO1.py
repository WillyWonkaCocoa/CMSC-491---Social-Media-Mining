import requests
import html5lib
from bs4 import BeautifulSoup

URL = "http://www.businessinsider.com/antarctica-giant-iceberg-2016-12"
webpage = requests.get(URL)
print type(webpage)
    
html = webpage.text
print type(html)

soup = BeautifulSoup(html, 'html5lib')
print type(soup)
