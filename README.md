# Plantbased Earthling

## Code Institute: Milestone Project 3

![Plantbased Earthling Responsive Design](https://github.com/Natte-Z/Plantbased_Earthling/blob/34fcee19518b05328adc84ef482d4e5e62b67026/static/images/responsive.png)

*Plantbased Earthling* is an app that aims to help users prepare food and get inspired by vegetarian and vegan recipes. My aim with this project was to create an app that would be inspiring, useful and enjoyable for people to use. 

I myself got inspired by online blogs and recipes to live life a little bit greener. Especially now in Covid-19 times food has become such a big deal, because you spent so much time at home and cooking food together is a great activity that can be practiced together in small groups within this pandemic. 

My idea therefore came from creating a project that would meet the needs of other users/cokking fans who would like to inspire each other with their own favourite recipes that can be easily found within one database. 

By providing tips to the recipes, people could also use exiting recipes and letting other users know their little magic to make them even better, or how to make non-vegan recipes become vegan. 

This project underlines the third of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack site with the use of HTML, CSS, JavaScript, Python + Flask and MongoDB.

[Click here to view the project live.](https://xxxherokuapp.com/)

## Table of contents

- [**UX**](#UX)
    - [Main aims](#Main-aims)
    - [User Stories](#User-Stories)
        - [Project Stakeholders](#Project-Stakeholders)
        - [New Users](#New-Users)
        - [Returning Users](#Returning-Users)
        - [Tablet User](#Tablet-User)
    - [Design Process](#Design-Process)
    - [Documenting the design process](#Documenting-the-design-process)
- [**Features**](#Features)
    - [Database structure](#Database-structure)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Features-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**](https://github.com/mkthewlis/Milestone-Project-3/blob/master/testing.md)
- [**Deployment**](#Deployment)
    - [Local deployment](#Local-Deployment)
    - [Deploying this project to Heroku](#Deploying-this-project-to-Heroku)
- [**Credits**](#Credits)
    - [Content](#Content)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## UX

### Main aims

- To create an app that has real-world value for users who are interested in changing their diet and finding new adventures within cooking. 

- To achieve the first aim, it was essential that this app would satisfy all CRUD functions, allowing users to Create, Read, Update and Delete their own recipes within their user account.

- To make the website interactive, by adding JavaScript to create a positive user experience.

- To make navigation intuitive, with prompts to guide the user in the right direction if lost and flash messages to confirm their actions.

- To create a design that would be fully responsive on all devices and screen sizes. 


### User Stories

The following User Stories helped me to create a design that would satisfy the needs of several different types of users.

#### Project stakeholders

- I am the creator of this app and want to make sure that it adds value to users to encourage them to return, by ensuring the app is intuitive to use, fully responsive and sleek in design.
- I would like to create a place for the app's user community to add and edit their recipes and leave messages for me on how the app can become more user friendly. 

#### New users

- I am a user who relies on apps for all aspects of my life, from online shopping with Klarna, measuring the number of steps that I walk and monitoring my sleeping cycles. As I am a busy person I would like to have the recipes that I like to show up quickly without commercial or any extra work. 
- I am a young user, who has never really cooked a lot before and would like something easy to get started with. 

#### Returning users

- I am user who has used this website before and added my own recipes to it. I am happy that I have a place now to store my own recipes digitally and not in an old cooking paperbook. 
- I created an account for a few weeks ago and like that I can recommend this site to my friends so that it is easier to share our secret recipes. 

#### Tablet user

- I am a user who primarily uses an iPad Pro to browse websites. I want to have a good experience on this website and view all the features in an equally aesthetic way. 

### Design Process

#### Design Process: UX Research 
Before beginning the formal design process, I began researching my favourite cooking websites. I wanted to see how they decided to structure their design, what I thought they did well and what I would like to do differently for my project. 
My research led me to the following conclusions:
- One big part that is missing on those websites is that users can edit and add their own recipes, so I created that for plantbased earthling. 
- The design would have to be sleek, simplistic and positive to capture the user's attention and encourage them to use the site as their preferred online cookbook.

##### The following websites were used in the research process:
- [ica.recept](https://www.ica.se/recept/)
- [sötasaker](https://sotasaker.com/2014/12/10/lakritskola/)
- [Zeina's Kitchen](https://zeinaskitchen.se/zeinas-green-kitchen/)

#### Design process: UX Design

1. Strategy plane: When starting the research on how to plan my online cookbook and I went through different blogs and other recipe pages the first thing that I saw that none of them have the function that users could add and edit their own recipes. I personally write down my recipes still on paper and it is annoying when at other friends places to not have the recipes. So to create an online recipe database where users could create, add, edit and delete their own recipes seemed like a need not yet solved. 

2. Scope plane: With the app idea and type of user that I wanted to create the app for, the next step would be the features. Those included account creation, managing of recipes with the CRUD functions and an easy design to navigate through. I also wanted the app to be personalised, with a user's chosen Username to feature in the design (for example, '"Welcome back 'Username!'"). Furthermore, I also wanted to allow the user to leave a message to me, the admin to give feedback and just share their ideas on how to improve the website. 

3. Strcuture plane: Once I had narrowed down what features I wanted to include, I began to consider the structure of my design. I realised that the website would have to be presentable to external users browsing through the pages with open access, whilst creating certain pages that are only accessible to users logged in with their account. To create this distinction, I decided that the menu bar would change, with standard items being 'Home', 'Categories', 'Contact', 'Login' and 'Register', whilst users who are logged in would see the same taps, but would also include 'Categories', 'Profile', 'Add Recipe' and 'Log Out' instead of the Register and Login options. This decision was made for a better user experience, as I realised that a registered user who was already logged in would not want to see the 'Sign In'/ 'Sign Up' items in their menu bar. I also made the decision that a user would be able to navigate to the 'Edit recipe' and 'delete recipe' pages through button prompts on the recipe views page, as these functions are only possible when a user is logged in.

4. Skeleton plane: With the concept and structure in place, I began to plan the navigation route through the design. After opening the website, a new user would be able to see all recipes, the contact page as well as the register and sign in function. It was important for me that users could still see all recipes without having to create an account, because I wanted a very open and welcoming website. Nowadays I believe that there are too many websites that want to create an account and that without that no function is possible, I wanted to create something different. Existing users, however, are able to see the categories option as well as are able to edit and delete their own recipes, not the ones from other users. In addition the existing users also have a profile page, which shows all of the recipes that they have created. 

5. Surface plane: 
    * As this is my third milestone project I wanted to use more colours in the beginning and created a really interesting colour scheme for this project. Moreover, I wanted the website to still show a modern design, that would keep the user interested in the website. The simplicity was shown in the fact, that all recipes are first shown in card panels with only a picture and a few small details, like category (e.g. dessert), cooking time, the name of the user that created the recipe and an extra function that shows whether a recipe is vegan. Later on in the process I realised that my colour scheme was too aggressive for this project, because the user experience gets highlighted by many recipe pictures that can be colourful, because the user itself chooses them. So that keep that in mind I changed a little bit of my colourscheme, especially for background colours to keep it more simple and sustainable in the long-term. For my first own recipes I used the website unsplash.com, which provides great pictures that can be freely used without any IP's on them. 
    * With the idea of the type and style of design that I was after, I started a wireframe on [Figma](https://www.figma.com/file/U8j2oct9s0U0jnaDaLlSSK/Milestone-Project-III?node-id=0%3A1) and began experimenting with my wireframes. As with my earlier two Milestone Projects, I found it useful to have my hero image in place, as doing so prompts me to choose the tone and theme for the rest of the design. 
    * I also used tailorbrands.com free function to include a modern logo and some images throughout the website to make it look more professional. 
    * I turned to Google Fonts to select the fonts for my project. I wanted to find two compatible fonts that were modern and would look good in a light font weight to complement the simplistic design. I found that Heebo and Poppins met these criteria and showed a difference to my earlier used fonts. 
    * I began to take note of certain features that I would add later on with JavaScript. These included an arrow button in the footer to scroll smoothly back to top and a contact page that connects with Email Js. 

> Note: Throughout the design process, I kept referring back to my original 'Main Aims', 'User Stories' and preliminary research to make sure that my project was developing as intended.

### Documenting the design process

Selected color palette:
![Color palette created with visme.co](https://visme.co/blog/website-color-schemes/)
The colours for this were:
French Laundry Blue: #3a4660
Comfortably Tan: #c9af98
Peachy Kreme: #ed8a63
Brown Bonnet: #845007

[The entire workspace can be viewed on Figma with this link.](https://www.figma.com/file/U8j2oct9s0U0jnaDaLlSSK/Milestone-Project-III?node-id=0%3A1)

## Features

### Existing Features

This project consists of nine pages, five of which can only be accessed after a user has created an account and signed in.

#### Database structure

The data for this project is stored in my MongoDB database within three collections as follows:
- *Users* - This collection stores the user's username and their enctrypted password created when they signed up to Plantbased Earthling.
- *Recipes* - When a user creates a task, it is stored within this collection with the following information: image_url, category_name, recipe_name, recipe_serves, recipe_time, recipe_difficulty, recipe_description, recipe_ingredients, recipe_instrcutions, recipe_tips extra function of “vegan” (yes or no) and created_by. 
- *Categories* - The categories of the dishes which can be starters, mains and desserts. 

#### Consistent features across all pages

- The menu at the top of the page and footer are consistent in design and responsive throughout the website. However, the contents of the menu changes depending on if a user is logged in or not.
- Each page features a 'scroll to top' button that becomes visible when the user has scrolled down on the page, this will be especially useful once more recipes are on the page.
- All buttons are designed consistently in their respective colors across the app.
- All flash messages appear under the menu bar with the same font and color throughout the app.

#### Home/Recipes 

- The user sees directly all the recipes, so that they dont need to click through more pages to get to what they are looking for on the website. 
- On larger screens the user sees three card panels of the recipes in a row and they minimize to two on medium size devices and one on a smartphone. 
- On the card panel is a button that will lead the user to the full recipe, as on the homepage they will only see short informations of the recipe
- I decided on this design feature so that the user has a better overview of all the recipes and doesnt get flashed with too much information directly

### Categories

- This page features the three categories.
- The user has the option to click on one of the categories to only see recipes that belong to that category. 

### Contact

- Here the user, whether logged in or not, has the possibility to leave a comment or question.
- I wanted this function to be open so that every user has the possbility to leave feedback also without having to have to make an account. 

#### Profile

- Once a user has either signed up or signed in, they are directed to their 'Profile' page with an overview of their own created recipes, if they have any. 
- If they have recipes they can view them through the "view" button. 

#### Add Recipe

- This page offers a form to the user with all the information that a new recipe needs. Most of the fields are required, but some like the vegan function and the tipsinput field are of free choice. 
- The form includes all the values that are within the mongo DB database.
- - A flash message is shown that the adding has been done once the user clicks the button and then the user is redirected to the home page. 

#### Recipes page

- This is the page that shows the whole recipe. 
- In the end it includes the edit and delete button, which gives the user that has created the recipe and the admin the option to use them. 

#### Edit recipe

- This site is similar to the add_recipes page, however the information that was filled out when creating a recipe is directly shown in the input fields, so that it is easier for the user to edit them. 
- A flash message is shown that the editing has been done once the user clicks the button and then the user is redirected to the home page. 

#### Register
- This is a simple page which offers the user the possibility to register for the page.
- The code has been structured in a way that it stores a secret key for the password in the database and recognizes if a username has already been used. 

#### Log In
- Here the user can login. 
- There is another link at the end which redirects the user to the register page if they haven't created an account yet. 

#### Log Out
- The logout is less a page and more a function within the navbar, that logs the user out and redirects them to the login page. 

### Features Left to Implement

- I think that there is a lot of potential to further develop this app, which is unfortunately beyond the scope and time frame of this Milestone Project with *The Code Institute*. 

- It could be useful to create a 'profile' page where users could update their information, including changing their password and adding a profile image.

- I would also consider adding a feature to report bugs found back to me, to be able to improve the app for future users as and when issues are found.

- It would be also nice to include a "favourite" button within the recipes that would save recipes to the profile page of the user. 

## Technologies Used

### Languages, libraries, databases, frameworks, editors and version control

- HTML5
    * The language used to create add structure and content to the website.
- CSS
    * The language used to style the HTML5 elements according to the design colour scheme.
- JavaScript
    * The languge used to make the app interactive, including the use of the sendEmail.js functionality. 
- [jQuery](https://jquery.com/)
    * I used the jQuery library to help write the JavaScript code used in this project.
- Python
    * The programming languaged used to create the back-end function of the app.
- PyMongo
    * PyMongo was used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The Python microframework used to help write the Python code for this project.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Jinja templating language was used with Flask in the HTML code. This allowed for template inheritance from the base.html file and to link the back-end to the front-end. 
- [MongoDB](https://www.mongodb.com/)
    * This was the selected database chosen to store data in the cloud.  
- [MaterliazeCss framework](https://materializecss.com/) 
    * I used the MaterliazeCss container system as I wanted to design my project with a good responsiveness. I also used different functions from materliaze to make the app more interactive, e.g. forms, selectors, radius as well as icons.  
- [Gitpod](https://www.gitpod.io/)
    * I relied on Gitpod's dev environment to write the code for my project.
- [Git Version Control](https://git-scm.com/)
    * I used Git for Version Control to track and record changes to my code and refer back when needed.
- [GitHub](https://github.com/)
    * I used GitHub as my remote repository, to push to and store the commited changes to my app from Git.
- [Heroku](https://www.heroku.com/)
    * I used Heroku as a hosting platform to deploy the live version of my app. 

### Additional tools used
- [Figma](https://www.figma.com/) 
    * Figma helped me design my project, by creating wireframes this project. 
- [FontAwesome](https://fontawesome.com/) 
    * I relied on free FontAwesome icons, including different icons for the social media.  
- [Google Fonts](https://fonts.google.com/)
    * I used two complementary fonts from Google for my project: Heebo and Poppins. 
- [Tailor Brands](https://www.tailorbrands.com/) 
    * I used this to create a nice logo and some more images for my app. 
- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML and CSS code (as discussed in more detail in the Testing section).
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards.

## Testing

### Testing User Stories
The following tests were conducted to test the experience of each user outlined earlier in the 'User Stories' section.

#### Project stakeholders

- As the creator of this project, I wanted to make sure that users would actually find value in using this app as that would provide an incentive for them to return to it. To achieve this goal, I have created a project that is easy to navigate and intuitive to use, allowing the user to immediately learn how to make the most of its features. Recipes are easy to add, edit, delete and view, allowing the user to focus on enjoying the process of cooking. 

## Testing

To return to the previous document, please click [here](https://github.com/mkthewlis/Milestone-Project-3/blob/master/README.md).

- [**Testing User Stories**](#Testing-User-Stories)
    - [Project Stakeholders](#Project-stakeholders)
    - [New users](#New-users)
    - [Returning users](#Returning-users)
    - [Tablet user](#Tablet-user)
- [**Validators and Lintners**](#Validators-and-lintners)
    - [HTML](#HTML)
    - [CSS](#CSS)
    - [JavaScript](#JavaScript)
    - [Python](#Python)
- [**Compatibility tests**](#Compatibility-tests)
    - [Using different browsers](#Using-different-browsers)
    - [Using different devices](#Using-different-devices)
    - [Using different screen sizes](#Using-different-screen-sizes)
- [**Manual tests**](#Manual-tests)
    - [Menu bar](#Menu-bar)
    - [Footer](#Footer)
    - [Home](#Home)
    - [Top Tips](#Top-tips)
    - [Sign-in](#Sign-in)
    - [Sign-up](#Sign-up)
    - [My tasks](#My-tasks)
    - [Add a new task](#Add-a-new-task)
    - [Edit task](#Edit-task)

### Testing User Stories

The following tests were conducted to test the experience of each user outlined earlier in the 'User Stories' section.

#### Project stakeholders

- As the creator of this project, I wanted to make sure that users would actually find value in using this app as that would provide an incentive for them to return to it. To achieve this goal, I have created a project that is easy to navigate and intuitive to use, allowing the user to immediately learn how to make the most of its features. There are prompts to sign in or sign up throughout the project, and once a user has signed in, they can navigate the internal pages from their personalised Overview page. Tasks are easy to add, edit, delete and mark as complete, allowing the user to focus on enjoying the process of getting ready to move home, which is the goal of this app.
- I also wanted to make it easy for the community of MoveOn users to share their own tips with other users. This is achieved through the 'Top Tips' page, where users can contribute to the list of tips with their own recommendations. These can only be added when a user has signed in and they can only edit and delete their own recommendations.

#### New users

- The new user who relies on technology for all aspects of their lives would find this app useful when cooking. They would find that it's easy to set up an account and begin to add, edit and delete their own recipes. They can find recipes easily through the categories which saves them time. 
- The young user who has never really cooked before would find that this helps them that cooking is actually not so hard and with the different difficulty levels have a better understanding. 

#### Returning users

- The user who had already created an account and wanted to add more recipes to their list could do so with a few simple steps: they would just directly click on "add_recipe" fill out the form and the recipe would show on their profile and on the home site. 

## Deployment

This project was developed using Gitpod as the chosen IDE and GitHub as a remote repository. 

The deployed project can be viewed on the following link: [Plantbased Earthling: Live Website](xx)

The project's GitHub repository can be viewed with the following link: [Plantbased Earthling: GitHub Repository](xx)

### Deploying this project to Heroku 
To deploy the project to Heroku, I used the following steps:

1. I created a Heroku account, signed in and created a new app with a unique name that had not already been taken (this project uses 'ms3-move-on'). I then set the region to the closest to me: 'Europe'.
2. With the app created, I went to the 'Settings' tab and clicked the 'Reveal Config Variables' button. From here, I input the following values:
```
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
IP: 0.0.0.0
PORT: 5000
```
(Note: within the MONGO_URI value, I replaced the 'username','password', 'cluster_name' and 'database_name' with my specific database values. They are kept private for security reasons.)

3. In Gitpod, I created a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
4. I then created a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: python app.py > Procfile
```
5. I then committed these new files with the following:
```
git add .
```
git commit -m ""
```
git push
6. Because I connected my Github repository to Heroku it could autp deploy the project once I pushed my code to github. 

## Credits

### Content

The content of this website is entirely fictional and written by myself.

### Images

The images are all from unsplash.com, which is an open source of illustrations. 

### Acknowledgements

Thank you to the following people who helped with support and inspiration:

- My mentor Seun Owonikoko for her attention to detail throughout the development process
- My send mentor Antonio Rodriguez for helping me in the final hours.  
- A special thanks to the talented *Code Institute* tutors Tim and Johann for their advice, guidance and support 
- All the other tutors that helped me through problems. 
- My friend Vuong, who helped me to understand JavaScript on a new level and guided me through design decisions. 
- And my roommates for helping me through the time, giving advise and feedback on the UX and just supporting me. 