import requests 
import sqlite3
from bs4 import BeautifulSoup

# Request URL
response = requests.get("http://books.toscrape.com/catalogue/category/books/science_22/index.html")
# Init BS
BeautifulSoup(response.text, "html.parser")


