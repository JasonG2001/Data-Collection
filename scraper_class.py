from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from web_navigator import WebNavigator

class Scraper:

    def __init__(self, web_navigator: WebNavigator) -> None:
        
        self.web_navigator = web_navigator
        self.products: list = self.web_navigator.get_driver().find_elements(By.CLASS_NAME, "athenaProductBlock")
        
        time.sleep(1)
        self.scrape_name()
        self.scrape_links()
        self.scrape_price()
        self.scrape_number_of_reviews() 

    def scrape_name(self) -> list:

        name_list: list = []

        for product in self.products:
            
            try:
                name: str = product.find_element(By.CLASS_NAME, "athenaProductBlock_productName").text
                name_list.append(name)

            except:
                pass
        
        print(name_list)
        return name_list

    
    def scrape_links(self) -> list:
        
        link_list: list = []

    
        for product in self.products:
            
            try:
                a_tag = product.find_element(by=By.TAG_NAME, value='a')
                link: str = a_tag.get_attribute('href')
                link_list.append(link)

            except:
                pass

        print(link_list)        
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


    def scrape_price(self) -> list:
        
        price_list: list = []


        for product in self.products:

            try:
                price: str = product.find_element(By.CLASS_NAME, "athenaProductBlock_priceBlock").text
                price_list.append(price)

            except:
                pass

        print(price_list)
        return price_list




    def scrape_number_of_reviews(self) -> list:

        review_list: list = []

        
        for product in self.products:
            try:
                number_of_reviews: str = product.find_element(By.CLASS_NAME, "athenaProductBlock_reviewCount").text
                review_list.append(number_of_reviews)

            except:
                print("")
                pass

        
        print(review_list)
        return review_list

    def scrape_reviews(self) -> list: # Needs fixing

        rating_list: list = []

        try:
            for product in self.products:
                ratings: str = product.find_element(By.CLASS_NAME, "productBlock_ratingStarsContainer")
                rating_list.append(ratings)

            return rating_list

        except:
            print("Not all products have reviews")

if __name__ == "__main__":
    web_navigator = WebNavigator()
    web_navigator.open_creatine_page() # For specific page

    scrape = Scraper(web_navigator)

    web_navigator.driver.quit()

