import json
from bs4 import BeautifulSoup
import requests
req = requests.get('https://www.onlinekhabar.com/')
soup = BeautifulSoup(req.content, "html.parser")
details = soup.find_all('div', class_="ok-container")
news_items =[]
   
for detail in details:
    title_tag = detail.find('h2')

    if title_tag:
        anchor_title =title_tag.find('a')
        if anchor_title:
            news_title = anchor_title.text.strip()
            news_url =anchor_title['href']  
            description = detail.find('p')
            description_text = description.text if description else None

            img_tag = detail.find('img')
            img_url = img_tag['src'] if img_tag else None
            news_item ={
                'News-Title': news_title,
                'News-URL': news_url,
                'Description': description_text,
                'Image-url': img_url
            }
           
            news_items.append(news_item)

with open('news_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(news_items, json_file, ensure_ascii=False, indent=4)

print("Data saved to 'news_data.json'")