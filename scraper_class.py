from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from web_navigator import WebNavigator

class Scraper:

    def __init__(self):
        
        self.products = self.driver.find_elements(By.CLASS_NAME, "athenaProductBlock")
        self.price = self.product.find_element(By.CLASS_NAME, "athenaProductBlock_priceBlock").text
    
    def scrape_links(self):
        pass


    def scrape_price(self):
        
        price_list = []

        for self.product in self.products:
            
            price_list.append(self.price)

        print(price_list)

        self.driver.quit()


    def scrape_review(self):
        pass

    def scrape_description(self):
        pass


wn = WebNavigator()
wn.run()

scrape = Scraper()
scrape.scrape_price()

