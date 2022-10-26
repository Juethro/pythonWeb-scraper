import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from url import url

urls = url

with open('./pythonWeb-scraper/src/index2.html', 'w', encoding= 'utf_8') as f:
    f.write(urls.text)

with open('./pythonWeb-scraper/src/index2.html', 'r') as duar:
    soup = bs(urls.text, 'html.parser')

all_links = soup.find_all('a')

print(all_links)

