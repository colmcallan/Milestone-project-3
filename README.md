
# Cookbook | Cookbook Website
## [Demo Here](https://cookbook-recipe.herokuapp.com/)
What is 'Cookbook | Cookbook Website' - It's an app built with Flask and MongoDB. In this application I use technologies learnt on my coding journey to demonstrate how a document-based database can be utilise efficiently and effectively to create simple yet effective scalable apps on the web. The aim of this project is to showcase my tech learnt so far from the course. 
This will be my first ever project using the below languages and features and for me was a great learning experience. 

Throughout this project I will make use of [Python](https://www.python.org/) a high-end programming language along with [Flask](http://flask.pocoo.org/) a Python micro framework and [MongoDB](https://www.mongodb.com/) a document-based database and [jQuery](https://jquery.com/) a web-based language know to many.

With these tools I will be able to showcase all I have learnt from Code Institute so far; majority of my back-end logic will be written in Python running on the Flask framework using a document based database alongside jQuery to assist with some of the functions with Bootstrap

---
## UX
I wanted to create a seamless app for people to be able to easily store recipes.
The app is designed to allow for users to create, store and manage recipes. 
Lots of people may use cookbooks to refer from when cooking a meal, this app allows user to then store they're cookbook recipes into one place.
The site is fully responsive and easy to navigate throughout.

---
## Wireframes 
[Desktop View](https://github.com/colmcallan/Milestone-project-3/tree/master/static/images/wireframes/desktop)

---
### Database Schema
Before I started the core development of my project, I began working on how i wanted my database to appear. this was done by researching best practices and i found it quite interesting over all. 

---
## Cookbooks Functionality
The app's main functionality is that it is capable of communicating to a dedicated document-based database running on atlas using MongoDB.
By using Python/Flask alongside Mongo I have been able to create an application that stores recipe data inputted by anyone. 

My application is scalable and responsive meaning it will perform well on any device it's loaded on. 

Within my applications functionality I’ve created a search bar to allow users to search any recipe within my database straight from an input field. Text is entered and based on the query provided the app will filter the database's collection.

My app has a online store (not ecommerce) to ensure users have a one stop app for recipes and cooking utensils should they need any. 


---
## Technology Used
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Flask 1.0.2](http://flask.pocoo.org/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CCS3/SCSS](https://sass-lang.com/)
- [Bootsrap4](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://www.mongodb.com/)
- [Atlas](https://www.mongodb.com/cloud/atlas)
- [Fontawesome](https://fontawesome.com/)

---
## Database data

All my recipe data was source from [**Edam**](https://developer.edamam.com/edamam-recipe-api) a free recipe search site where the data was pulled into my database. 

---
### Things that could be improve if had more time
- I could add filters on browse all recipes page to be able to filter the likes of new diet labels or health labels.

- Secured user log in/registration for users and lock content in terms of who can edit and delete recipes. As i haven't had any expoosure to this functionality I wasn't capable of implementing it.

- A fully working shopping cart for items to be purchased by users. 

- Like buttons if a user (if registered) likes the recipes and add this as a filter option.

##### Why I built 'CookBook | Cookbook Website'

The main reasoning behind the project was inspired by Code Institute as the brief was to create a cookbook type project. 
---
## Testing
Most of the applications testing was done throughout development, most of which was manual tests. I will outline most of what I did below for documentation purposes.

**Testing Flask** - Within my settings I had flask's debugger set to 
```python
debug=True
```
This is so when Flask ever encounters an error the application knows to display this error in the view to give indication of what caused the app to crash.

I would work in small sprints where every step in my development I would ensure my app is still working as expected and where the app encounters any errors, I would debug the source until rectification was a success. Where needed I would document the error and the remediation taken in case of future occurrences. 

Doing this meant after a while the error codes became more familiar to me. And from this debugging each error become less time consuming. 

---

**Testing Python** - When writing Python code, I would normally write this is small chunks and do any routine testing from the CLI and where needed use the Python Interpreter to test any functions or statements. 

---

**Testing Flask Views** - In Flask each app's route uses a view template from my app structure these views were tested throughout every stage within my development process. Where needed I would test each view worked as expected when added new code or functionality to my app.

When passing any data down to the view I would firstly always ensure the data is there via using extra code within the back-end before sending down the data in the request. For example if I wanted to load my recipe collection in the back-end and send it to the view I would first ensure the data was loaded correctly by perform some back-end logic then pass this data to the view template whilst also checking the data was sent correctly to the front-end by perform the same back-end tests but on the front end before designing and displaying the mark up how I wanted it. 

---

**Testing the database** - Getting my data collections right was the trickiest part of this project. As through developing my application my database schema was constantly changing to the requirements of my app. Where multiple changes had to be made to the database in order for all my app's functionality to work properly.

To achieve this I imported my data into my database via .JSON file and ensure all routes worked as expected.

This is how I collected my recipe data to play about with at the beginning of my app development in order to get the UPDATE, DELETE and READ methods working within my app. 

---

**Testing CRUD**

**READ**
Firstly, before anything I wanted to make sure that I could display to my users the recipes I'd already collected and inserted into my db. To do this I had to create a home route and load the recipe collection within this route then pass the data to the view. As previously mentioned for the views I would constantly throughout the project development ensure there was no errors from Flask/Jinja before progressing with functionality of my app. 

In order to test that the recipe collection had successfully made it onto the app view I first assigned the data to a variable and tested within the Python interpreter that the data was loaded successful and could be printed to the terminal. After this I perform the same tests on the front-end once happy, I begin to develop the home route for users to view all my recipes in my database in one single view.

After I made a route so that  users could view a single recipe alone. I took the functionality from the task_manager project we created and transferred it over to my app. 

**UPDATE**

Testing the update recipes route was a case of trying the update.all method and applying this to a route that allowed the user to update the record based on some input by the user posting by the update recipe form. Upon a successful edit I would check in the single recipe view and by printing the entire recipe to the terminal that all user edited fields have updated.

**DELETE**
Testing the delete function in my app was a case of creating the route and then testing that route within the browser, I would grab a recipe ID and then enter the URL needed for that route to perform. After deleting a record, I would flash a message for the user to be notified and also print a message to the terminal. To ensure the recipe was delete I would check in my view all recipes page along with checking the Atlas website. 

**CREATE**
To test my create functionality of my app I would continuously fill out a recipe form and test that the route when posting create a new recipe within my recipe collection and that all the fields I needed were created successfully.

Once my CRUD functionality was in place, I tested each form multiple times and tried to break each field or manipulate each form to perform unexpected. I have had my apps functionality tested multiple times by friends, family. Where bugs were identified I made a note and fixed each issue.

From this I am confident that my CRUD functionality in my app is all working and without any bugs or errors being produced.


---

**Responsiveness** - My app is fully responsive; through the entire development and design process I continuously tested my app under Chrome Developer tools and testing various different screens sizes. By this I was able to perform periodic checks throughout the development process to ensure that my app was responsive across all device screens ranging from extra small to extra-large. Where needed I just used media queries to fix any resolution issues or responsiveness issues. I have built my app on the [Bootsrap4](https://getbootstrap.com/) a universally used grid system and using custom CSS to ensure full responsiveness. 

My app has been testing by friends and family members where needed notes were made and identified bugs were fixed. 

From doing this I have been able to confidently say that my app is fully responsiveness across all devices. 

---

**Browser compatibility** 


My app will be fully functional across all major modern browsers. I have tested my app on the following browsers.

- [Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Opera](https://www.opera.com/)
- [IE Edge](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [IE](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [Safari](https://support.apple.com/en_GB/downloads/safari)
- [Chrome Mobile](https://chrome.en.softonic.com/)

---

## Resource Sites Used
- [Edam](https://developer.edamam.com/edamam-docs-recipe-api)
- [Bootsrap4 Docs](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [Fontawesome Icons](https://fontawesome.com/)
- [Flask Docs](http://flask.pocoo.org/docs/1.0/)
- [Mongo Docs](https://docs.mongodb.com/)
- [Slack](https://slack.com/intl/en-gb/)
- [Google](https://google.com/)
- [YouTube](https://www.youtube.com/)

---

### HTML & CSS
All my HTML and CSS is valid, checked with the following validators

- [HTML Validator](https://validator.w3.org/)
-  [CSS Validator](https://jigsaw.w3.org/css-validator/)

## Deployment 
Getting my application ready for deployment consisted of the following: - 
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the heroku Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file. 
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Set Flask's debugging to False.
5. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.
6. IF using AWS cloud9, uninstall all requirements in the requirements.txt file and reinstall the following;
    1. `dnspython`
	2. `Flask`
	3. `flask-paginate`
	4. `Flask-Pagination`
	5. `Flask-PyMongo`
	6. `Flask-WTF`
	7. `heroku`
	8. `pymongo`


**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully. *

### Expanding on my project

To get set up with a copy of my project you can do these multiple ways. 

**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE. 
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few environment variables before we can run the app.
	1. `app.config["MONGO_DBNAME"] = "cookbook_creation"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 main.py`

**Via the CLI** -
1. Clone my repo via Git using the following command `https://github.com/colmcallan/Milestone-project-3`
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few environment variables before we can run the app.
	1. `app.config["MONGO_DBNAME"] = "cookbook_creation"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 app.py`

## Credits & Acknowledgments 
Credit is due to the following names. I would like to thank each and every one who has helped or contributed to my project in any way. Please see list of names below:

- Mentor **Guido Cecilio Garcia**
- Youtuber **Pretty Printed**
- Friends who helped functionality and code review **Wesley Redmond**, **Conor Fitzsimons**

