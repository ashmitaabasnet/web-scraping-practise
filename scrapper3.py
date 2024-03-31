from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
gecko_driver_path =r"C:\Users\ACER\Documents\WebDriver\geckodriver.exe"

firefox_options = Options()
firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://ekantipur.com/")

elements = driver.find_elements(By.XPATH,'//h2/a[@data-type="title"]')

for element in elements:
    print("Title:", element.text)
            
driver.quit()