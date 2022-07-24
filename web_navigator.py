from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

class WebNavigator:

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
        creatine_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[5]')
        creatine_button.click()