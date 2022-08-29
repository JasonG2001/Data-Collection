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

This repeates the process for all the buttons on the site.


