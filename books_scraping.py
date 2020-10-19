import requests 
import sqlite3
from bs4 import BeautifulSoup

# Request URL
response = requests.get("http://books.toscrape.com/catalogue/category/books/science_22/index.html")
# Init BS
soup = BeautifulSoup(response.text, "html.parser")
# Book titles
books = soup.find_all("article")
for book in books: 
    title = book.find("h3").find("a")["title"]
    price = float(price.replace("£","").replace("Â",""))

