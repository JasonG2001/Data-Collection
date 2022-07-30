from numpy import number
from selenium import webdriver 
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:

    def __init__(self):

        self.driver: webdriver = webdriver.Chrome()
        self.driver.get("https://www.myprotein.com/")
        self.accept_cookies_and_exit_signup()

        #self.get_all_product_links()
        self.scrape_all_product_links()
        
        self.driver.quit()

    def accept_cookies_and_exit_signup(self) -> None:

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[4]/div/div[2]/button'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[1]/div/div/div[2]/button'))).click()


    def get_button_links(self) -> list[str]:
    
        button_links: list[str] = []
        button_container = self.driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div[2]')
        buttons = button_container.find_elements(by=By.TAG_NAME, value='a')

        for button in buttons:

            button_link: str = button.get_attribute('href')

            button_links.append(button_link)
        
        return button_links

    def get_all_product_links(self):
        all_product_links = []
        
        for button_link in self.get_button_links():
            product_links: list[str] = self.get_product_links(button_link)
            all_product_links.extend(product_links)

        return all_product_links

    def get_product_links(self, button_link): # For each button

        self.driver.get(button_link) # enter 1 button

        try:
            product_container = self.driver.find_element(By.CLASS_NAME, 'productListProducts') 
            products = product_container.find_elements(by=By.TAG_NAME, value='a') # get all products in the button

            product_links: list[str] = [] 

            for product in products:
                
                product_link: str = product.get_attribute('href') # get link of each product in the 1 button

                product_links.append(product_link)

            return product_links

        except: # For the vitamins and vegan page
            product_container = self.driver.find_element(By.CLASS_NAME, 'sectionPeek_grid')
            products = product_container.find_elements(by=By.TAG_NAME, value='a')

            product_links: list[str] = []

            for product in products:

                product_link: str = product.get_attribute('href')

                product_links.append(product_link)

            print(product_links)
            return product_links


    def scrape_all_product_links(self):
        for product_link in self.get_all_product_links():
            self.scrape_product_links(product_link)


    def scrape_product_links(self, product_link):
        
        self.driver.get(product_link)
       
        dict = {

        }

        try:
            name: str = self.driver.find_element(By.CLASS_NAME,"productName_title").text
            dict["Name"] = str(name)

        except:
            dict["Name"] = None
            pass

        try: # Needs fixing
            description: str = self.driver.find_element(By.CLASS_NAME,"productDescription_synopsisContent").text
            dict["Description"] = str(description)

        except:
            dict["Description"] = None
            pass
        
        try:
            price: str = self.driver.find_element(By.CLASS_NAME, "productPrice_price  ").text
            dict["Price"] = str(price)

        except:
            dict["Price"] = None
            pass

        try:
            number_of_stars: str = self.driver.find_element(By.CLASS_NAME, "athenaProductReviews_aggregateRatingValue").text
            dict["Number of stars"] = str(number_of_stars)

        except:
            dict["Number of stars"] = None
            pass

        try:
            number_of_reviews: str = self.driver.find_element(By.CLASS_NAME, "productReviewStars_numberOfReviews").text
            dict["Number_of_reviews"] = str(number_of_reviews)
        
        except:
            dict["Number_of_reviews"] = None
            pass

        try:
            src = self.driver.find_element(by=By.XPATH, value='//img[@class="athenaProductImageCarousel_image"]').get_attribute('src')
            dict["Source of image"] = src

            urllib.request.urlretrieve(src)

        except:
            dict["Source of image"] = None
            pass

        print(dict)
        return dict


if __name__ == "__main__":
    scraper = Scraper()
