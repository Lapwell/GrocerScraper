from selenium import webdriver
from bs4 import BeautifulSoup
import page_manager as pm

#Defining constants
BASE_URL = "https://www.fairwaymarkets.com"
DEPARTMENTS_XPATH = "unifiednav__container  "

option_list = []
preference_list = [("permissions.default.image", 2)]
browser = pm.GetPage(BASE_URL, option_list, preference_list)
content = browser.get_page_source()

#[Parser]
soup = BeautifulSoup(content, 'html.parser')
DEPARTMENTS = soup.find("nav", id="1664781648").find("ul").find("li", {"class" : "unifiednav__item-wrap", "aria-haspopup" : "true"}).find("ul", {"class" : "unifiednav__container unifiednav__container_sub-nav"})

links = [a.get('href') for a in DEPARTMENTS.find_all('a', href=True)]


link_soup = []
for item in links:
    print('Navigating to link: ' + item)
    browser.driver.get(browser.url + item)
    link_content = browser.get_page_source()
    link_soup.append((BeautifulSoup(link_content, 'html.parser'), '----------------------------------------------------------------'))
browser.close_driver()

# loop = 0
# for item in link_soup:
#     file_object = open(f"output{loop}.txt", "a")
#     file_object.writelines(str(item))
#     loop += 1
# file_object.close()
