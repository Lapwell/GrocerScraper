from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageManager():
    def __init__(self,url, driver_options, driver_preferences, x_path):
        self.x_path = x_path
        self.url = url
        options = Options()
        if driver_options:
            for item in driver_options:
                options.add_argument(item)
        if driver_preferences:
            for item in driver_preferences:
                options.set_preference(item[0], item[1])
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.url)
        print("Waiting")
        #Wait for the browser to load. The program waits until an element with a specific ID
        elem = WebDriverWait(self.driver, 16).until(
        EC.presence_of_element_located((By.XPATH, self.x_path))
        )
        print("Done Waiting")

    def get_page_source(self):
        return self.driver.page_source

    def close_driver(self):
        self.driver.close()
