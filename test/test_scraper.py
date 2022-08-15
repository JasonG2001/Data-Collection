from selenium import webdriver 
from selenium.webdriver.common.by import By
import unittest
from project.scraper import Scraper
import os


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
        self.assertEqual(product_link, 'https://www.myprotein.com/vitamins/multivitamin-gummies/12088106.html')

    def test_scraping_product(self):
        self.driver.get('https://www.myprotein.com/sports-nutrition/clear-whey-isolate/12081395.html')
        
        product_info: dict[str, str] = {}

        name: str = self.driver.find_element(By.CLASS_NAME,"productName_title").text
        product_info["Name"] = name

        self.assertEqual(product_info, {'Name': 'Clear Whey Isolate'})


        

    
if __name__ == "__main__":
    unittest.main()
