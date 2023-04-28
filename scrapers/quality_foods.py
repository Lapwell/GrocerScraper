from selenium.common.exceptions import ElementNotVisibleException
from selenium import webdriver
from bs4 import BeautifulSoup
import web_scraper as scraper

# links = ["https://www.qualityfoods.com/grocery", "https://www.qualityfoods.com/meat__seafood", "https://www.qualityfoods.com/produce", "https://www.qualityfoods.com/bakery", "https://www.qualityfoods.com/deli", "https://www.qualityfoods.com/dairy", "https://www.qualityfoods.com/frozen_foods", "https://www.qualityfoods.com/bulk_foods", "https://www.qualityfoods.com/beer_wine_and_spirits"]
links = "https://www.qualityfoods.com/produce"

WAIT_TARGET = "#bodyContainerPlaceHolder_bodyPlaceHolder_productImageViewPanel"
DRIVER_OPTIONS = ["--headless"]
DRIVER_PREFERENCES = [("permissions.default.image", 2)]  #Preference 0 is for diabling images on webpages.

page_content_list = []

for item in links:
    browser = scraper.PageManager(links, DRIVER_OPTIONS, DRIVER_PREFERENCES, None, WAIT_TARGET)
    page_content_list.append(browser.get_page_source())
    browser.close_driver()

