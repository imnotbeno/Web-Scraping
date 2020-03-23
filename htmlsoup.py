#! python3
import bs4, requests

#res = requests.get("https://nostarch.com")
#res.raise_for_status()

example_file = open("exercise.html")
noStarchSoup = bs4.BeautifulSoup(example_file, 'lxml')
print(type(noStarchSoup))
