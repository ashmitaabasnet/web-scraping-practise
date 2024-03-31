import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
gecko_driver_path =r"C:\Users\ACER\Documents\WebDriver\geckodriver.exe"

firefox_options = Options()
firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://ekantipur.com/")

main_file = driver.find_element(By.XPATH,'//*[@id="mainnnns-wrap"]')
news_list =[]
if main_file:
    news_data = main_file.find_elements(By.TAG_NAME,"article")
    for data in news_data:
       headline = data.find_element(By.TAG_NAME,'a').text
       details = data.find_element(By.TAG_NAME,'p').text

       article_data = {
           "Headline": headline,
           "Details": details
       }
    
       news_list.append(article_data)
    #    print("Headlines:",headline)
    #    print("Details",details)

with open('Ekantipur.json', 'w', encoding='utf-8') as json_file:
    json.dump(news_list, json_file, ensure_ascii=False, indent=4)

print("Data saved to 'Ekantipur.json'")            

