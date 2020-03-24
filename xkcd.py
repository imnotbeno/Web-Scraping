#! python3
import requests
import bs4
import os

url = "https://xkcd.com/"
os.makedirs('xkcd', exist_ok = True)
while not url.endswith('#'):
    #Downloading the page
    print("Downloading the page " + url + "\n")
    page = requests.get(url)
    page.raise_for_status()

    #Convert the downloaded page to text
    html_text = bs4.BeautifulSoup(page.text, 'lxml')

    #Find element that contains the url
    find_element = html_text.select('#comic img')

    #Check if obtaining an image url was successful
    if find_element == []:
        print("No image was found!")
    else:
        img_url = 'http:' + find_element[0].get('src')

        #Downloading the image
        print("Downloading image " + img_url + "\n")
        img_download = requests.get(img_url)
        img_download.raise_for_status()

    #Saving the image into ./xkcd file
    imageFile = open(os.path.join('xkcd', os.path.basename(img_url)), 'wb')
    for i in img_download.iter_content(100000):
        imageFile.write(i)
    imageFile.close()

    #Get 'previous' button url
    previous_url = html_text.select('a[rel = "prev"]')
    #Set main url to previous post url and repeat
    url = 'https://xkcd.com' + previous_url[0].get('href')

print('Finished!')
