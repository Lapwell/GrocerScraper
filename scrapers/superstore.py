from selenium import webdriver
from bs4 import BeautifulSoup
import web_scraper as wb

#Defining constants
BASE_URL = "https://www.realcanadiansuperstore.ca/"
X_PATH_0 = "/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/div[1]/nav/ul/li[1]/button"
X_PATH_1 = "/html/body/div[1]/div/div[2]/main/div/div/div/div[2]/div/div[2]/div[4]/div/ul"

#This block to to open the main page of the Superstore website and get the links for all the food departments.
#It also creates the global-constant options for the browser.
DRIVER_OPTIONS = ["--headless"]
DRIVER_PREFERENCES = [("permissions.default.image", 2)]
browser = pm.PageManager(BASE_URL, DRIVER_OPTIONS, DRIVER_PREFERENCES, X_PATH_0)
page_content = browser.get_page_source()
browser.close_driver()

#[Parser]
soup = BeautifulSoup(page_content, 'html.parser')
food_element = soup.find("ul", "primary-nav__list primary-nav__list--level-1")

links = []
for item in food_element:
    link = item.find('a', "primary-nav__list__item__link", href=True)
    links.append(link.get('href'))


# y = len(links) - 1
# while y > 0:
#     links.pop()
#     y -= 1

loop = 0
souped_content = []
food_list = [["GROUP ", "NAME ", "PRICE "]]
for item in links:
    item = str(item)
    new_link = BASE_URL + item
    print(f'Navigating to link num{loop}: ' + item)
    browser = pm.PageManager(new_link, DRIVER_OPTIONS, DRIVER_PREFERENCES, X_PATH_1)
    page_source = browser.get_page_source()
    souped_content = BeautifulSoup(page_source, 'html.parser')  #Convert the page source into usable string data
    loop += 1
    browser.close_driver()

print(links)
