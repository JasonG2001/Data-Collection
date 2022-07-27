from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class WebNavigator:
    
    def __init__(self) -> None:

        self.driver: webdriver = webdriver.Chrome()
        self.driver.get("https://www.myprotein.com/")
        self.accept_cookies_and_exit_signup()

    def accept_cookies_and_exit_signup(self) -> None:

        WAIT_TIME: int = 10
        self.driver.implicitly_wait(WAIT_TIME)

        exit_signup_button: None = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[4]/div/div[2]/button')
        exit_signup_button.click()

        accept_cookies_button: None = self.driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[1]/div/div/div[2]/button')
        accept_cookies_button.click()

    def get_driver(self):
        return self.driver

    def visit_link(self, link_list): #
        scraper = self.Scraper()
        link_list = scraper.scrape_links()

        for link in link_list:
            self.driver.get(link)


        pass

    def scroll_down_page(self, scroll_amount):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")

    def open_protein_page(self):
        
        protein_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[1]')
        protein_button.click()

    def open_bars_and_snacks_page(self):
        
        bars_and_snacks_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[2]')
        bars_and_snacks_button.click()

    def open_clothing_page(self):
        
        clothing_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[3]')
        clothing_button.click()

    def open_vitamins_page(self):
        
        vitamins_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[4]')
        vitamins_button.click()

    def open_vegans_page(self):
        
        vegans_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[5]')
        vegans_button.click()

    def open_creatine_page(self):
        creatine_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[6]')
        creatine_button.click()

    def go_to_product_link(self, product_link):
        # a_tag = product.find_element(by=By.TAG_NAME, value='a')
        # link = a_tag.get_attribute('href')
        self.driver.get(product_link)



if __name__ == "__main__":
    wn = WebNavigator()
    wn.open_protein_page()
    time.sleep(3)
    wn.driver.quit()
    

