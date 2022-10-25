#import modules
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# get html file
url = rq.get("https://unair.ac.id/news")

# export html file
with open("index.html", 'w') as nulis:
    nulis.write(url.text)

# read html file and assign to beautifulsoup
with open("index.html", 'r') as htmll:
    soup = bs(htmll, 'html.parser')

# find_all h3 tags html
listt = soup.find_all('h3' , class_='elementor-post__title')

# declare 2 list for cleaning step
data_judul = []
filter = []

# cleaning data from \n \t etc.
for i in listt: 
    splitted = re.split(r'[\n\t\f\v\r]+', i.find('a').get_text())
    
    # Hilangkan enter depan
    for x in splitted[1:]:
        filter.append(x)

# Hilangkan enter belakang
for su in filter[0::2]:
    data_judul.append(su)


# Export Dataframe
df = pd.DataFrame(data_judul)
df.columns = ['Judul_Headline']
df.to_csv('../scraping-headlines.csv')

df.head()