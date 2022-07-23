from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

class Scraper:
    pass

driver = webdriver.Chrome()
driver.get("https://www.myprotein.com/")

def accept_cookies_and_exit_signup():

    exit_signup_button = driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[4]/div/div[2]/button')
    exit_signup_button.click()
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="home"]/div[1]/div/div/div[2]/button')
    accept_cookies_button.click()

def open_protein_page():
        
    protein_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[1]')
    protein_button.click()

def open_bars_and_snacks_page():
    
    bars_and_snacks_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[2]')
    bars_and_snacks_button.click()

def open_clothing_page():
    
    clothing_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[3]')
    clothing_button.click()

def open_vitamins_page():
    
    vitamins_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[4]')
    vitamins_button.click()

def open_vegans_page():
    
    vegans_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[5]')
    vegans_button.click()

def open_creatine_page():
    creatine_button = driver.find_element(by=By.XPATH, value= '//*[@id="mainContent"]/div[2]/a[5]')
    creatine_button.click()

def scrape_price():
    pass

def scrape_review():
    pass

def scrape_description():
    pass

driver.quit()