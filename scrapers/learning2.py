from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import csv

#[Browser setup]
options = Options()
options.add_argument('--headless') # hide GUI
options.set_preference('permissions.default.image', 2)
#Load the browser with the defined options, then go to the page
browser = webdriver.Firefox(options=options)
browser.get('https://github.com/Lapwell?tab=repositories')

#Wait for the browser to load
title = (
    WebDriverWait(driver=browser, timeout=10)
    .until(visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    .text
)

#Grab the page source then close the browser
content = browser.page_source
browser.close()

#[Parse page_source]

soup = BeautifulSoup(content, 'html.parser')
user_repo = soup.find('div', id='user-repositories-list')
projects = user_repo.find_all('li')

parsed = [["Name", " Language", " Date"]]
for item in projects:
    name = item.find('a', itemprop='name codeRepository')
    name = name.text.split()
    language = item.find('span', itemprop='programmingLanguage')
    language = language.text.split()
    date = item.find('relative-time')
    date = date.text
    parsed.append([name, language, date])

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(parsed)
