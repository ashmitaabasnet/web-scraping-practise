from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
import sys

def download_procedure(url):
    driver = webdriver.Chrome()
    driver.get(url)
    page_html = driver.page_source
    driver.quit()
    time.sleep(5)
    page_soup = soup(page_html, "html.parser")
    matching_li_elements = page_soup.select('table#table tbody tr')
    results = []
    for container in matching_li_elements:
        td_elements = container.find_all('td')

        if len(td_elements) >= 4:
            title = td_elements[1].get_text(strip=True)
            print(title.encode('utf-8').decode('utf-8'))
            date = td_elements[2].get_text(strip=True)
            print(date.encode('utf-8').decode('utf-8'))
            
            href = td_elements[3].find('a')['href'] if td_elements[3].find('a') else None
            print(href.encode('utf-8').decode('utf-8') if href else None)


            # results.append({
            #     'title': title ,
            #     'date': date,
            #     'href': base_url + href
            # })
    print(results)
    # print(str(results).encode('utf-8', 'ignore').decode('utf-8'), flush=True, file=sys.stdout.buffer)
    
    with open('output.txt', 'w', encoding='utf-8') as output_file:
     output_file.write(str(results))


base_url = "https://dotm.gov.np/"
url = "https://dotm.gov.np/download-content/directive--working-procedure"
download_procedure(url)


