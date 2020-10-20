import requests 
import sqlite3
from bs4 import BeautifulSoup

# Request URL
response = requests.get("http://books.toscrape.com/catalogue/category/books/science_22/index.html")
# Init BS
soup = BeautifulSoup(response.text, "html.parser")
# Scrape book info
books = soup.find_all("article")

# Method to extract the book title
def get_title():
    for book in books:
        title = book.find("h3").find("a")["title"]
        return title

# Method to extract book price
def get_price():
    for book in books:
        price_text = book.select(".price_color")[0].text
        price = float(price_text.replace("Â","").replace("£",""))
        return price

# Method to extract book rating
def get_rating():
    ratings = {"Zero":0, "One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    for book in books:
        p = book.select(".star-rating")[0] 
        rating = p.get_attribute_list("class") [-1]
        int_rating = ratings[rating]
        return int_rating


# Driver code
if __name__ == "__main__":
    get_title()
    get_price()
    get_rating()