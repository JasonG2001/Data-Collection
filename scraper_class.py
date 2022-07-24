from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from web_navigator import WebNavigator

class Scraper:

    def scrape_links(self):
        item_container = self.driver.find_element(by=By.XPATH, value='')
        item_list = item_container.find_element(by=By.XPATH, value='./div')
        link_list = []

        for item in item_list:
            a_tag = item.driver.find_element(by=By.XPATH, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

    def scrape_price(self):
        pass

    def scrape_review(self):
        pass

    def scrape_description(self):
        pass


