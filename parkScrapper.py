##### Import Necessary Libraries
"""

import pandas as pd
import requests
from bs4  import BeautifulSoup as bs
from selenium import webdriver
import time

"""##### Load the Web Page"""

driver = webdriver.Chrome()
url = 'https://www.google.com/search?client=firefox-b-d&q=Parque+Bot%C3%A2nico+' \
      'da+Vale#ip=1&lrd=0xb819af7b273e05:0xa6cb675203cd8d3a,1,,,,'

driver.get(url)

time.sleep(10)

"""##### Click the Reviews"""

element_show_all = driver.find_element('xpath', '/html/body/span[2]/g-lightbox/div/div[2]/div[3]/span/div/div/div/div[2]/div[3]/g-scrolling-carousel/div[1]/div/div[2]')
element_show_all.click()

entries = driver.find_elements(By.XPATH, '//div[contains(@class, "WMbnJf vY6njf gws-localreviews__google-review")]')

# Iterate through each entry and extract the required data
for entry in entries:
    labels = []
    try:
    # Extract the name using the correct XPath
        name = entry.find_element(By.XPATH, './/div[@class="TSUbDb"]/a').text
        rating = entry.find_element(By.XPATH, ''
        labels.append(name)
    except NoSuchElementException:
            print("Name element not found in this entry.")

    print(labels)























































