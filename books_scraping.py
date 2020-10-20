import requests 
import sqlite3
from bs4 import BeautifulSoup

def scrape_books(url):

    # Request URL
    response = requests.get(url)

    #Init BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape book info
    books = soup.find_all("article")
    
    # Iterate through all books and append all book data to a list
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
        print(all_books)

# Method to extract the book title
def get_title(book):
    title = book.find("h3").find("a")["title"]
    return title

# Method to extract book price
def get_price(book):
    price_text = book.select(".price_color")[0].text
    price = float(price_text.replace("Â","").replace("£",""))
    return price

# Method to extract book rating
def get_rating(book):
    ratings = {"Zero":0, "One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    p = book.select(".star-rating")[0] 
    word = p.get_attribute_list("class") [-1]
    return ratings[word]

# Driver code
if __name__ == "__main__":
    scrape_books("http://books.toscrape.com/catalogue/category/books/science_22/index.html")
