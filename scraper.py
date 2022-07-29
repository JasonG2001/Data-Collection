from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:

    def __init__(self):

        self.driver: webdriver = webdriver.Chrome()
        self.driver.get("https://www.myprotein.com/")
        self.accept_cookies_and_exit_signup()

        self.get_all_product_links()
        #self.scrape_all_product_links()
        
        self.driver.quit()

    def accept_cookies_and_exit_signup(self) -> None:

        #WAIT_TIME: int = 2
        #self.driver.implicitly_wait(WAIT_TIME)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[4]/div/div[2]/button'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[1]/div/div/div[2]/button'))).click()

        #exit_signup_button = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[4]/div/div[2]/button')
        #exit_signup_button.click()

        #accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[1]/div/div/div[2]/button')
        #accept_cookies_button.click()


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

    def get_product_links(self, button_link):

        self.driver.get(button_link) # enter 1 button

        #product_container = self.driver.find_element(By.CLASS_NAME, 'productListProducts') 
        products = self.driver.find_elements(by=By.TAG_NAME, value='a') # get all products in the button

        product_links: list[str] = [] 

        for product in products:
            try:
                product_link: str = product.get_attribute('href') # get link of each product in the 1 button

                product_links.append(product_link)

            except:
                pass
        
        return product_links

    def scrape_all_product_links(self):
        for product_link in self.get_all_product_links():
            self.scrape_product_link(product_link)


    def scrape_product_link(self, product_link):
        
        self.driver.get(product_link)

        try:
            name: str = self.driver.find_element(by=By.XPATH, value='//div[@class=productName]').text
            print(name)

        except:
            pass
        
        try:
            price: str = self.driver.find_element(By.CLASS_NAME, "productPrice").text
            print(price)

        except:
            pass

        try:
            number_of_reviews: str = self.driver.find_element(By.CLASS_NAME, "productReviewStars").text
            print(number_of_reviews)
        
        except:
            pass

        return {

            "name": name,
            "price": price,
            "number_of_reviews": number_of_reviews

        }

        #go to
        #scrape
        


if __name__ == "__main__":
    scraper = Scraper()
