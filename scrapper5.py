import json
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url ="https://ekantipur.com/"
driver.get(url)
heading_bar = driver.find_elements(By.CLASS_NAME,'nav-item')
for data in heading_bar:
  heading_title = data.find_elements(By.TAG_NAME, 'a')
  news =[]
  for value in heading_title:
     title_text = value.text
     value.click()

     current_url = driver.current_url
     new_driver = webdriver.Firefox()
     new_driver.get(current_url)
     

     main_file = new_driver.find_elements(By.CLASS_NAME,'teaser offset')
     
     for file in main_file:
        news_head = file.find_element(By.TAG_NAME,'h2').text
        news_details = file.find_element(By.TAG_NAME,'p').text

        list_data ={
            "Headline":news_head,
            "Details":news_details
         }
        news.append(list_data)
        new_driver.quit()

with open('Ekantipur2.json', 'w', encoding='utf-8') as json_file:
    json.dump(news, json_file, ensure_ascii=False, indent=4)

print("Data saved to 'Ekantipur2.json'") 
driver.back()
driver.quit()
         

    


   
    


 