from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from web_navigator import WebNavigator

class Scraper():

    def __init__(self, web_navigator):
        
        self.web_navigator = web_navigator
        self.products = self.web_navigator.get_driver().find_elements(By.CLASS_NAME, "athenaProductBlock")

    def scrape_links(self):
        
        link_list = []

        for product in self.products:
            a_tag = product.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

        return link_list


    def scrape_price(self):
        
        price_list = []

        for product in self.products:
            price = product.find_element(By.CLASS_NAME, "athenaProductBlock_priceBlock").text
            price_list.append(price)

        return price_list


    def scrape_number_of_reviews(self):

        review_list = []

        for product in self.products:
            number_of_reviews = product.find_element(By.CLASS_NAME, "athenaProductBlock_reviewCount").text
            review_list.append(number_of_reviews)

        return review_list

    
    def scrape_description(self):
        pass


web_navigator = WebNavigator()
web_navigator.open_creatine_page()

scrape = Scraper(web_navigator)
print(scrape.scrape_links())

web_navigator.driver.quit()

