from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from web_navigator import WebNavigator

class Scraper:
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.myprotein.com/")

    def accept_cookies_and_exit_signup(self):

        self.driver.implicitly_wait(3)

        exit_signup_button = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[4]/div/div[2]/button')
        exit_signup_button.click()

        accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[1]/div/div/div[2]/button')
        accept_cookies_button.click()

    def scrape_price(self):
        pass

    def scrape_review(self):
        pass

    def scrape_description(self):
        pass


