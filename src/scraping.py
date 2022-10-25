import requests
from bs4 import BeautifulSoup as bs

x = requests.get("https://www.unair.ac.id/news/")
hasil = bs(x.text,'html_parser')

print(hasil.prettify())
