from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from web_navigator import WebNavigator

class Scraper():

    def __init__(self, web_navigator: WebNavigator):
        
        self.web_navigator = web_navigator
        self.products = self.web_navigator.get_driver().find_elements(By.CLASS_NAME, "athenaProductBlock")

    def scrape_name(self):

        name_list = []

        for product in self.products:
            name = product.find_element(By.CLASS_NAME, "athenaProductBlock_productName").text
            name_list.append(name)

        return name_list
    
    def scrape_links(self):
        
        link_list = []

        for product in self.products:
            a_tag = product.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

        return link_list


    '''

    def scrape_description(self):

        description_list = []

        # gets a list of the link for each product page
        product_links = list(map(lambda product : product.find_element(by=By.TAG_NAME, value="a").get_attribute("href"), self.products))

        for product in product_links:
            self.web_navigator.go_to_product_link(product)
            # TODO:: after the web navigator goes to the product link self.products elements are stale and cannot be used - needs fixing

            description = self.web_navigator.get_driver().find_element(By.CLASS_NAME, "productDescription_synopsisContent").text
            description_list.append(description)

        return description_list

    '''


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


web_navigator = WebNavigator()
web_navigator.open_creatine_page()

scrape = Scraper(web_navigator)
print(scrape.scrape_links())

web_navigator.driver.quit()

