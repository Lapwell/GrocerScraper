from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class PageManager():
    def __init__(self,url, driver_options, driver_preferences, cookies, wait_target):
        self.wait_target = wait_target
        self.url = url
        options = Options()
        #Add any driver options if needed
        if driver_options:
            for item in driver_options:
                options.add_argument(item)
        #Add any profile preferences needed
        if driver_preferences:
            for item in driver_preferences:
                options.set_preference(item[0], item[1])
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.url)
        #add any cookies that are needed
        if cookies:
            for item in cookies:
                self.driver.add_cookie(cookies)
        self.driver.refresh()
        print("Waiting")
        #Wait for the browser to load. The program waits until an element with a specific ID
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, self.wait_target))
        WebDriverWait(self.driver, 30).until(element_present)
        sleep(4)
        print("Done Waiting")

    def click_element(self, click_target):
        #This method clicks elements at the bottom of the page. Will probably need to change it scrolling only to the bottom
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, click_target)))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()

    def get_page_source(self):
        return self.driver.page_source

    def close_driver(self):
        self.driver.close()
