#! python3
import requests

#.get takes in a string of a URL to download
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

'''
print(type(res)) #returns a response object
print(res.text[:250])
'''
