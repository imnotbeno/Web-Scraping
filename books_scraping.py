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
    #title = book.find("h3").find("a")["title"]
    #price = book.select(".price_color")[0].get_text()
    #price = float(price.replace("£","").replace("Â",""))
    ratings = {"Zero":0, "One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class") [-1] #we want the last item
    int_rating = ratings[rating]
    print(int_rating)

