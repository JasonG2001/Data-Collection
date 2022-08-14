from xmlrpc.client import Boolean
from selenium import webdriver 
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid
import os
import json
import boto3
import psycopg2

class Scraper:

    """Scrapes the information off every page in the website and stores this information locally
    """

    def __init__(self):

        self.driver: webdriver = webdriver.Chrome()
        self.driver.get("https://www.myprotein.com/")
        self.accept_cookies_and_exit_signup()

        '''
        all_product_info = self.scrape_all_product_links()
        
        self.store_all_files_locally(all_product_info)
        self.store_all_to_aws()
        '''

    def accept_cookies_and_exit_signup(self) -> None:

        """Clicks 'accept cookies' button and exits the sign up button
        """
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[3]/div/div[2]/button'))).click()
        except:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[4]/div/div[2]/button'))).click()
        
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="home"]/div[1]/div/div/div[2]/button'))).click()


    def get_button_links(self) -> list[str]:

        """Finds all buttons on the front page as a link
        
        Returns
        -------
        list
            list of strings of the button links on the front page
        """
    
        button_links: list[str] = []
        button_container = self.driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div[2]')
        buttons = button_container.find_elements(by=By.TAG_NAME, value='a')

        for button in buttons:

            button_link: str = button.get_attribute('href')

            button_links.append(button_link)

        return button_links
    '''
    def get_next_pages(self):
        
        pages_links = []

        while disabled != "disabled":
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,'responsivePaginationNavigationButton paginationNavigationButtonNext'))).click()
            link = 
            pages_links.append(link)

        return pages_links
    '''

    def get_all_product_links(self) -> list[str]:

        """Gets the links of all the products on the whole website
        
        Returns
        -------
        list
            list of strings of all the product links from all the buttons, combined onto 1 list
        """

        all_product_links: list[str] = []
        
        for button_link in self.get_button_links():
            product_links: list[str] = self.get_product_links(button_link)
            all_product_links.extend(product_links)
        
        return list(set(all_product_links)) # set() removes any duplicate links

    def get_product_links(self, button_link: str) -> list[str]:
        
        """Goes to a button link and gets the product links present in the button
        
        Parameters
        ----------
        button_link: str
            The link of the button with the product links
            
        Returns
        -------
        list
            list of strings of all the products inside 1 button
        """

        self.driver.get(button_link)

        product_links: list[str] = [] 

        try: 
            products = self.driver.find_elements(By.CLASS_NAME, 'productListProducts_product ') 

            for product in products:

                name: str = product.find_element(By.CLASS_NAME, 'athenaProductBlock_productName').text 
                
                if self.check_if_product_has_been_scraped(product) == True:

                    product_link: str = product.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                
                    product_links.append(product_link)

                else: 
                    print(f"{name} has already been scraped")
            
            if product_links[0] == 0: # The products on the nutritions page is identified by a different Class name. This exception allows the products to be scraped in the except block
                raise Exception
            
            return product_links

    
        except: # For vitamins and vegan page
            
            products = self.driver.find_elements(By.CLASS_NAME, 'sectionPeek_item')

            for product in products:

                name: str = product.find_element(By.CLASS_NAME, 'athenaProductBlock_productName').text 

                if self.check_if_product_has_been_scraped(product) == True:

                    product_link = product.find_element(by=By.TAG_NAME, value='a').get_attribute('href')

                    product_links.append(product_link)

                else:
                    print(f"{name} has already been scraped")
            
            return product_links 
        
    def check_if_product_has_been_scraped(self, product) -> bool:

        name: str = product.find_element(By.CLASS_NAME, 'athenaProductBlock_productName').text 
        modified_name: str = name.replace("/", " - ")
        
        PATH = r"C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data"

        if modified_name not in os.listdir(PATH):
            return True

        else:
            return False


    def scrape_all_product_links(self) -> list[dict[str,str]]:

        """Gets information of all the products on the website
        
        Returns
        -------
        list
            list of dictionaries of strings which hold the information of all the products
            the dictionary holds the following information:
                product link
                uuid
                name
                description
                price
                number of stars
                number of reviews
                source link for any image available
        """

        list_of_product_info: list[dict[str,str]] = []

        for product_link in self.get_all_product_links():
            product_info: dict[str,str] = self.scrape_product_links(product_link)
            list_of_product_info.append(product_info)

        return list_of_product_info
            


    def scrape_product_links(self, product_link: str) -> dict[str,str]:

        """Goes to a product link and scrapes the information of that product
        
        Parameters
        ----------
        product_link: str
            link of the individual product that we want to scrape
            
        Returns
        -------
        dictionary
            dictionary of strings which corresponds to the information of a product
            the dictionary holds the following information on the product:
                product link
                uuid
                name
                description
                price
                number of stars
                number of reviews
                source link for any image available
        """
        
        self.driver.get(product_link)
       
        product_info: dict[str, str] = {}

        friendly_id: str = product_link
        product_info["Friendly ID"] = friendly_id

        product_info["UUID"] = str(uuid.uuid4())
            

        try:
            name: str = self.driver.find_element(By.CLASS_NAME,"productName_title").text
            product_info["Name"] = name

        except:
            product_info["Name"] = "None"

        try: 
            description: str = self.driver.find_element(By.CLASS_NAME, "productDescription_synopsisContent").text
            product_info["Description"] = description

        except:
            product_info["Description"] = "None"
        
        try:
            price: str = self.driver.find_element(By.CLASS_NAME, "productPrice_price  ").text

            product_info["Price"] = price

        except:
            product_info["Price"] = "None"

        try:
            number_of_stars: str = self.driver.find_element(By.CLASS_NAME, "athenaProductReviews_aggregateRatingValue").text
            product_info["Number of stars"] = number_of_stars

        except:
            product_info["Number of stars"] = "None"

        try:
            number_of_reviews: str = self.driver.find_element(By.CLASS_NAME, "productReviewStars_numberOfReviews").text
            product_info["Number_of_reviews"] = number_of_reviews
        
        except:
            product_info["Number_of_reviews"] = "None"

        try:
            src: str = self.driver.find_element(by=By.XPATH, value='//img[@class="athenaProductImageCarousel_image"]').get_attribute('src')
            product_info["Source of image"] = src

        except:
            product_info["Source of image"] = "None"
        
        return product_info

    
    def store_file_locally(self, directory_name: str, json_name: str, data: dict[str,str], image_source: str) -> None:

        """Makes a directory named as the id of the product inside 'raw_data' and craeates a json in this directory
        the dictionary of information of a product is converted to this json file
        images are also downloaded into this directory
        
        Parameters
        ----------
        directory_name: str
            name given to the directory created inside 'raw_data'
        json_name: str
            name given to the json file being created inside the created directory
        data: dict[str,str]
            the data in the form of a dictionary that is converted to a json file
        image_source: str
            link of the image source
        """
        
        try: 

            PATH_FOR_DIRECTORY: str = r"C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data"
            os.chdir(PATH_FOR_DIRECTORY)

            modified_directory_name = directory_name.replace("/", " - ") # Directory name cannot contain a '/'
            os.makedirs(modified_directory_name)

        except FileExistsError:

            print(f"File named {modified_directory_name} already exists.")

        os.chdir(modified_directory_name)

        
        with open(json_name, "w") as json_file:
            json.dump(data, json_file, indent=4)

        try: # download images
            full_path: str = modified_directory_name + ".jpg"
            urllib.request.urlretrieve(image_source, full_path)

        except:

            print(f"No image available for {modified_directory_name}")
    

    def store_all_files_locally(self, all_product_info: list[dict[str,str]]) -> None:

        """Stores the information in the form of a json file for every single product in their own directory

        Parameters
        ----------
        all_product_info: list
            list of dictionary of product information abtained from the scrape all product method
        """
        for product_info in all_product_info:
            self.store_file_locally(product_info["Name"], "data.json", product_info, product_info["Source of image"])

    def store_all_to_aws(self) -> None:

        """Stores all the json and image files in the local directory onto the aws cloud
        """

        BUCKET = "scraper-information"
        PATH = r"C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data"

        for product_directory in os.listdir(PATH):
            
            self.store_to_aws(product_directory, BUCKET)

    def store_to_aws(self, directory_name: str, bucket_name: str) -> None:

        """Looks for one directory stored in the local files and uploads the data file with the image file onto the aws cloud
            
        Parameters
        ----------
        directory_name: string
            give a name of the directory to enter so that the data inside that directory is accessible
        bucket_name: string
            give the name of the bucket on the aws server for which the local files will be stored to"""
        
        s3 = boto3.resource('s3')

        s3.meta.client.upload_file(fr'C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data\{directory_name}\data.json', bucket_name, f'data file - {directory_name}')
        s3.meta.client.upload_file(fr'C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data\{directory_name}\{directory_name}.jpg', bucket_name, f'image file - {directory_name}')

    def quit_browser(self) -> None:

        """Closes the web browser"""
        
        self.driver.quit()
    
    def upload_to_postgres(self, host, user, password, dbname, port) -> None: # run once for table creation, run again to insert record

        """Uploads to the postgres application linked to the amazon rds

        Parameters
        ----------
        host: string
            host name of the rds database
        user: string
            user name for the rds database
        password: string
            password made for the database
        dbname: string
            master name of the database
        port: int
            port number for the rds database
        """
        
        with psycopg2.connect(host = host, user = user, password = password, dbname = dbname, port = port) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("CREATE TABLE product_info (name VARCHAR UNIQUE, link VARCHAR UNIQUE, price FLOAT, number_of_stars FLOAT);")
                
                except:
                    path = r"C:\Users\xiaoh\OneDrive\Documents\AICore\Data-Collection\raw_data"
                    os.chdir(path)

                    for product_directory in os.listdir(path):

                        os.chdir(product_directory)

                        with open("data.json") as f:
                            data = json.load(f)

                        with psycopg2.connect(host = host, user = user, password = password, dbname = dbname, port = port) as conn:
                            with conn.cursor() as cur:
                                
                                modified_name: str = data["Name"].replace("'","/")
                                link: str = data["Friendly ID"]
                                
                                try:
                                    price = float(data["Price"][1:])
                                except ValueError:
                                    price = 0
                                
                                try:
                                    average_stars = float(data["Number of stars"])
                                except ValueError:
                                    average_stars = 0

                                cur.execute(f"INSERT INTO product_info VALUES ('{modified_name}', '{link}', '{price}', {average_stars})")
                
                        os.chdir(path)




if __name__ == "__main__":

    HOST = "database-1.cqav9sfxcwg5.eu-west-2.rds.amazonaws.com"
    USER = "postgres"
    PASSWORD = "Jguan2001"
    DATABASE = "postgres"
    PORT = 5432

    scraper = Scraper()
    
    all_product_info = scraper.scrape_all_product_links()
    scraper.store_all_files_locally(all_product_info)
    # scraper.upload_to_postgres(HOST, USER, PASSWORD, DATABASE, PORT)

    scraper.quit_browser()

    print(f"Scraping has taken {time.time()} s")