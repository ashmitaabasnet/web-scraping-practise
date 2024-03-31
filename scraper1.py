import requests
import pandas as pd
from bs4  import BeautifulSoup
req = requests.get("https://ekagaj.com/")
soup = BeautifulSoup(req.content ,"html.parser")
titles = soup.select('h1')
list = []

for title in titles:
   for a_tag in title.find_all('a'):
      a_details = a_tag.text

   list.append({'Titles: ':a_details})

df_list = pd.DataFrame(list)
df_list.to_csv("Scrapper1.csv", index=False)
print("CSV file saved")

    
