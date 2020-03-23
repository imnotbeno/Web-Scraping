#! python3
import requests

#.get takes in a string of a URL to download
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res)) #returns a response object
print(res.text[:250])
