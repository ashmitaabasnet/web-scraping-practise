from bs4  import BeautifulSoup
import requests
import pandas as pd
req = requests.get("https://ekagaj.com/")
soup = BeautifulSoup(req.content ,"html.parser")
topics = soup.find_all('div', class_='row')
for topic in topics:
    titles = topic.find_all('h1')
    description = topic.find_all('p')

    for title in titles:
        print("Title:", title.text)
    for data in description:
             print("Data:", data.text)

    