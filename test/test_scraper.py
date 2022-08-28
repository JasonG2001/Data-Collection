from project.scraper import Scraper
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import unittest

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.driver: webdriver = webdriver.Chrome()

    def test_get_button_links_returns_list(self):
        self.scraper = Scraper()
        self.assertIsInstance(self.scraper.get_button_links(), list)
    
    def test_get_button_link(self):
        self.driver.get("https://www.myprotein.com/")
        buttons = self.driver.find_element(By.CLASS_NAME, 'brandLogos_link')
        button_link = buttons.get_attribute('href')
        self.assertEqual(button_link, 'https://www.myprotein.com/nutrition/protein.list')

    def test_get_product_links_returns_list(self):
        self.scraper = Scraper()
        self.assertIsInstance(self.scraper.get_product_links("https://www.myprotein.com/nutrition/healthy-food-drinks.list"), list)

    def test_get_product_link(self):
        self.driver.get("https://www.myprotein.com/nutrition/protein.list")
        product = self.driver.find_element(By.CLASS_NAME, 'productListProducts_product ')
        product_link = product.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        self.assertEqual(product_link, 'https://www.myprotein.com/sports-nutrition/impact-whey-protein/10530943.html')

        self.driver.get('https://www.myprotein.com/nutrition/vitamins.list')
        product = self.driver.find_element(By.CLASS_NAME, 'sectionPeek_item')
        product_link = product.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        self.assertEqual(product_link, 'https://www.myprotein.com/sports-nutrition/alpha-men-multivitamin-tablets/10530421.html')

    def test_scraping_product(self):
        self.driver.get('https://www.myprotein.com/sports-nutrition/clear-whey-isolate/12081395.html')
        
        product_info: dict[str, str] = {}

        name: str = self.driver.find_element(By.CLASS_NAME,"productName_title").text
        product_info["Name"] = name

        self.assertEqual(product_info, {'Name': 'Clear Whey Isolate'})

    def test_storing_file_locally(self):
        self.scraper = Scraper()

        test_dict: dict[str:str] = {"test 1": "test 2"}
        self.scraper.store_file_locally("test_file", "test.json", test_dict, "None")

        PATH: str = r"C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data"
        list_of_directories: list[str] = os.listdir(PATH)
        
        self.assertIn("test_file", list_of_directories)


        

    
if __name__ == "__main__":
    unittest.main()
