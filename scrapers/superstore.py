from selenium.common.exceptions import ElementNotVisibleException
from selenium import webdriver
from bs4 import BeautifulSoup
import web_scraper as scraper
from time import sleep
import csv

#Defining constants
BASE_URL = "https://www.realcanadiansuperstore.ca/"
#The xpaths are for making sure their relevant pages load.
MAIN_PAGE_TARGET = "primary-nav__list__item.primary-nav__list__item--with-children"
SUB_PAGES_TARGET= "product-grid__results__products"
COOKIES = {"name": "last_selected_store", "value": "1527"}
DRIVER_OPTIONS = ["--headless"]
DRIVER_PREFERENCES = [("permissions.default.image", 2), ("geo.enabled", True)]  #Preference 0 is for diabling images on webpages.

#Lists
links = []  #This is for the links pulled from the main page
target_elements = []  #For the page source that is souped up belonging to each food department
food_list = [["BRAND", "NAME", "PRICE"]]  #This is for the parsed soup data.

#This block is to open the main page of the Superstore website and get the links for all the food departments.
browser = scraper.PageManager(BASE_URL, DRIVER_OPTIONS, DRIVER_PREFERENCES, COOKIES, MAIN_PAGE_TARGET)
page_content = browser.get_page_source()
browser.close_driver()

#[Parser]
soup = BeautifulSoup(page_content, 'html.parser')
food_element = soup.find("ul", "primary-nav__list primary-nav__list--level-1")

for item in food_element:
    link = item.find('a', "primary-nav__list__item__link", href=True)
    links.append(link.get('href'))


# y = len(links) - 2
# while y > 0:
    # links.pop()
    # y -= 1
#
loop = 0
for item in links:
    item = str(item)
    new_link = BASE_URL + item  #Create a new link for the browser.
    print(f'Navigating to link num {loop}: ' + item)
    browser = scraper.PageManager(new_link, DRIVER_OPTIONS, DRIVER_PREFERENCES, COOKIES, SUB_PAGES_TARGET)
    loop = True
    while loop:
        try:
            browser.click_element(".primary-button")
        except:
            loop = False
        else:
            continue
    page_source = browser.get_page_source()
    browser.close_driver()
    souped_content = BeautifulSoup(page_source, 'html.parser')  #Convert the page source into usable string data
    target_elements.append(souped_content.find_all("div", class_="product-tile__details"))  #Gets the <ul> that holds the products
    loop += 1


for products in target_elements:
    food_list.append([])
    for element in products:
        temp_list = []
        name = element.find("span", "product-name__item product-name__item--name")
        brand = element.find("span", "product-name__item product-name__item--brand")
        price = element.find("span", "price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
        #Get the wanted text values and makre sure they're not None
        if not isinstance(name, type(None)):
            temp_list.append(name.get_text())
        if not isinstance(brand, type(None)):
            temp_list.append(brand.get_text())
        if not isinstance(price, type(None)):
            temp_list.append(price.get_text())
        for item in temp_list:
            item.replace('"', '')
        food_list[-1].append(temp_list)


with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\n")
    writer.writerows(str(food_list).format('"', ''))
    writer.close()
