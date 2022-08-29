# Data-Collection


# Milestone 1

Github was used to create a new repository called 'Data-Collection' where changes will be tracked. Different feature branches will be created for each independant feature added and this will be merged into the main branch using 'git merge <new branch>' whilst on the main branch. Therefore, no new feature should be added on the main branch, rather on the newly created branches, merged before deleting the new branch.
  
  
# Milestone 2
  
Before moving into the coding for a scraper, I had to select a website where I would gather information from. I chose a website that would be associated with items which I show interest in. For such a website, I selected the 'MyProtein' site as the layout is simple and clear.
  
![image](https://user-images.githubusercontent.com/109103538/187242134-cc0437aa-31c1-465c-a959-2887c53a5ee0.png)

The items sold on the website is also an interest of mine
  
  
# Milestone 3
  
This milestone was the beginning of the coding for the scraper. To allow python access to the chromedriver to control chrome, the Selenium library must be imported. The first step is to get onto the website using driver.get() <img width="276" alt="image" src="https://user-images.githubusercontent.com/109103538/187243456-fe6443be-3878-4070-9d59-108c33ac31c7.png">

This is added as part of the initialiser in the Scraper class so that it is initialised everytime an instance of the class is created.
  
When first arriving on the website, the first obstacle is to bypass the cookies and sign up page. This is done using a click feature inside the Selenium library and waiting for the 'x' button and 'accept cookes' button to show on the html before clicking.
  
<img width="805" alt="image" src="https://user-images.githubusercontent.com/109103538/187244666-5ccd666e-5f90-40ad-bf8b-48f724faa8cc.png">

  
By observing the html of the website, I identified that the buttons on the page are part of a container with a specific xpath so a for loop can be used to access each individual button:
  
<img width="590" alt="image" src="https://user-images.githubusercontent.com/109103538/187244144-21dd171f-339b-4c54-a707-45ac123aacb8.png">
  
Using the driver.get() method again, my code allows access to each of the button links and the same method (used to get the button links) is repeated to get the links of all products in each button.
  
<img width="550" alt="image" src="https://user-images.githubusercontent.com/109103538/187245065-70d0a5c5-a390-4bf6-8576-43d8bd978d4e.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/109103538/187245190-6ad66a7f-642e-4a03-8c7b-1c152d4df995.png">
<img width="370" alt="image" src="https://user-images.githubusercontent.com/109103538/187245256-d95548ee-016a-4c16-b4db-21c0e62087e0.png">
  
These are used to get the product links in each button, whilst

<img width="533" alt="image" src="https://user-images.githubusercontent.com/109103538/187245435-4db08135-8706-4b73-b33a-cba4512090c3.png">

This repeats the process for all the buttons on the site.


# Milestone 4
  
This milestone involves the gathering of specific information and identification for each product which I plan to scrape.
  
<img width="508" alt="image" src="https://user-images.githubusercontent.com/109103538/187246934-022b3c9a-7848-413a-85c6-51134205a2cb.png">
<img width="658" alt="image" src="https://user-images.githubusercontent.com/109103538/187246989-be9ab94f-0912-47a0-a2c1-2321a88c1d02.png">
<img width="772" alt="image" src="https://user-images.githubusercontent.com/109103538/187247045-eb959586-e355-4780-a574-5f5331158672.png">

This method scrapes each product link obtained before the scrape_all_products() method repeats this process for all the product links
  
<img width="497" alt="image" src="https://user-images.githubusercontent.com/109103538/187247414-5b215931-56fc-442a-b211-2f28f5bce364.png">

Therefore, my code gathers the links of all items first and then scrapes each link rather than scraping as the links are gathered.
  
As part of the milestone, image data had to ge gathered and this was done by scraping each product for their image source. The source is the link for the image.
  
<img width="774" alt="image" src="https://user-images.githubusercontent.com/109103538/187248325-a851b406-b240-4885-845c-c82def398849.png">

I decided to use the product link as the friendly id for each item because this is unique and deterministic given the website. Unfortunately, the website didn't contain its own product id for each item which would make a better friendly id. Using the uuid module, I was able to generate a uuid for each of the items which I scrape.
  
All the data scraped is stored inside a dictionary and stored locally onto a .json file on my local drive using the os module in python. The script should create a directory named with each of the item names and these are created inside the 'raw_data' directory.
  
<img width="608" alt="image" src="https://user-images.githubusercontent.com/109103538/187250805-2fa9fe9a-c906-43a4-8e2d-f5f2e5e3323e.png">
  
json.dump() method from the json module converts the python dictionary into the .json file stored inside each item directory.
  
Within the same method of storing json files, the urllib.request module is imported and used to download the image data and stores this as a .jpg inside the same directory as the .json file.
  
<img width="392" alt="image" src="https://user-images.githubusercontent.com/109103538/187251333-e77bdb35-4222-4f8a-a1a3-d1736d8530fe.png">


# Milestone 5
  
This milestone taught me the importance of refactoring code to make it run more efficiently and have less demand on computer resources. To do so, I ran through the code and checked for features such as nested loops which are more demanding to run and unneccessary try/except blocks.
  
I also improved the structure of my working directory by creating two separate directories 'project' for my scraper.py and 'test' for unit testing. A setup.py file is also added to the main directory and using the setuptools module, I wrote the setup requirements which allows the scraper.py and test_scraper.py to run each other without having to be in the same directory.
  
The test_scraper.py uses the unittest module to test the different methods inside my scraper.py to ensure the methods give the expected outcome and in other cases, would help identify if any exceptions are being ignored.
  
An example is testing whether a method returns the expected type.
  
<img width="411" alt="image" src="https://user-images.githubusercontent.com/109103538/187253260-ed5f5fce-3473-4d1d-a281-b110a2c112cd.png">
  
The setUp() method runs before every unit test and the follow up method ensures that the method being tested returns my expected type of a list.


# Milestone 6

This milestone walked me through the storing of infomration onto a cloud service. In this case, Amazon RDS and the S3 bucket.
Using the boto3 library, I stored the .json dictionaries for each item and their .jpg image onto the aws S3 bucket in their own folders and this would happen as I ran the method.

<img width="449" alt="image" src="https://user-images.githubusercontent.com/109103538/187254483-5a868062-e3cd-4381-b0cb-d171049d6765.png">
<img width="673" alt="image" src="https://user-images.githubusercontent.com/109103538/187259085-8b24840c-b980-4528-a3bc-d5a8af6d1fb0.png">


Another method was also added and this used postgres and the library of psychopg to upload my scraped data into a postgres table where I can then query using SQL.

<img width="781" alt="image" src="https://user-images.githubusercontent.com/109103538/187259692-45159fb6-77f7-4af2-bb2a-63d2e0f240c4.png">

This creates a postgres table names 'product_info.

The script then goes into my local files and converts the .json data back into a dictionary.

<img width="788" alt="image" src="https://user-images.githubusercontent.com/109103538/187260233-d12117fe-d772-4170-aa66-dcf3494b26e9.png">

<img width="759" alt="image" src="https://user-images.githubusercontent.com/109103538/187260527-8c04a749-b424-4645-b6ef-dceda559edd9.png">

This block of code then uploads the data as a record to postgres in the form of a table.


# Milestone 7
  
This milestone required me to do a final refactoring of my code before containerisation in the next milestone.
The other major part of the milestone involves the prevention of my code from rescraping. The way I've done this is by creating methods to prevent rescraping and uploading the exact same records to postgres.
  
<img width="767" alt="image" src="https://user-images.githubusercontent.com/109103538/187263865-985dc3b3-935c-4c09-a339-0a6c67e0302a.png">
<img width="790" alt="image" src="https://user-images.githubusercontent.com/109103538/187263955-0f2a050e-44be-444e-986e-431f2744057a.png">
  
Checking for rescraping checks against my local directory to see if the product is already present.
Whilst checking if record exists checks against the postgres database and compares to see if the records are exactly identical. If they are exactly identical then no action is taken, if the product id is different to all the pre-existing records, then the new record is added. However, if the product id already exists but the record is not an exact copy, then it replaces the old record with the updated.

  

