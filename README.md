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

1. Strategy plane: While researching other to-do apps available to users, I realised that there wasn't one specifically aimed at users moving home. This confirmed to me that there were users who's needs had not yet been met; specifically, the need to have an app targeting users who are moving homes. In order to meet their needs, I realised that I would have to keep this particular type of user in mind throughout the design and planning process in order to create a successful app.

2. Scope plane: With the app idea and type of user in place, I began to consider what features would be required to create a successful and useable app. I knew that a user had to be able to create their own account, manage their tasks with the help of the four CRUD functions and find the design easy to navigate as they worked their way through their list of tasks. I also wanted the app to be personalised, with a user's chosen Username to feature in the design (for example, '"Welcome back 'Username!'"). Furthermore, I also wanted to include a feature to allow users to share their ideas with others, and delete and update the tips that they've added on the community board.

3. Strcuture plane: Once I had narrowed down what features I wanted to include, I began to consider the structure of my design. I realised that the website would have to be presentable to external users browsing through the pages with open access, whilst creating certain pages that are only accessible to users logged in with their account. To create this distinction, I decided that the menu bar would change, with standard items being 'Home', 'Top Tips', 'Sign In' and 'Sign Up', whilst users who are logged in would see see same basic items, but would notice 'My Tasks' (instead of 'Sign In') and 'Sign Out' (instead of 'Sign Up'). This decision was made for a better user experience, as I realised that a registered user who was already logged in would not want to see the 'Sign In'/ 'Sign Up' items in their menu bar. I also made the decision that a user would be able to navigate to the 'Edit task' and 'Add new task' pages through button prompts on their 'My Tasks' page, as these functions are only possible when a user is logged in.

4. Skeleton plane: With the concept and structure in place, I began to plan the navigation route through the design. After opening the website, a new user would immediately be able to access the 'Sign Up' page by noticing a button with the same name in the menu bar (and this standard button design would reappear throughout the design to continue to prompt a new user to sign up). Conversely, existing users could either choose to sign in from the menu, or scroll down to the bottom of this page to find a 'sign in' button prompt. If, however, the user does neither of those steps and chooses to click on the next item in the menu - 'Top Tips' - they would see a list of recommended tasks to consider before moving home. This page then contains a prompt for users to add their own tips to the community board - if they are signed in, the form to do so is visible. Otherwise, they are directed to the sign in/ sign up page respectively and the 'submit' form is hidden. From this page, regardless of whether the user chooses to navigate to the 'Sign Up' or the 'Sign In' page, they will see the same basic page structure: a form to either sign up or sign in (depending on the page they clicked on), a prompt to direct them to the other (if they choose the wrong link) and a feature image.
Regardless of which form they complete and submit, they are navigated to a personalized 'My Tasks' page for their account, which either shows their existing tasks if they are a returning user, or a prompt to add tasks if their list is empty. Clicking on the 'Add new task' button takes them to a page to create a new task which is then visible in their list. By clicking on this task, they can either mark it as complete, delete it or edit it (by being redirected to a 'Edit task' page). Once satisfied with their use of the app, they can click on the 'Sign Out' button and return to the external design and the 'Sign In' page.

5. Surface plane: 
    * The main stylistic decision I made early on was to keep the design as sleek, modern and simplistic as possible, to prevent the design from distracting the user from their use of the app. However, I did not want this decision to compromise the user experience, so I chose to rely on illustrations and graphics instead of photos to bring color and life to the app. My search for graphics led me to find [unDraw](https://undraw.co/), which is a great resource of open source illustrations that can be personalised after your chosen HEX color value.
    * With the idea of the type and style of design that I was after, I started a workspace on [Figma](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=170%3A2) and began experimenting with my wireframes for desktop, tablet and mobile devices. As with my earlier two Milestone Projects, I found it useful to have my hero image in place, as doing so prompts me to choose the tone and theme for the rest of the design. I selected one of the images I had chosen from unDraw and personalised it with a color palette I had created with [coolors](https://coolors.co/), as shown below. I chose this palette as the colors were modern yet toned down to offer a calm and welcoming feeling to users looking for help when planning their move.
    * I turned to Google Fonts to select the fonts for my project. I wanted to find two compatible fonts that were modern and would look good in a light font weight to complement the simplistic design. I found that Roboto and Quicksand met these criteria. 
    * I began to take note of certain features that I would add later on with JavaScript. These included an arrow button in the footer to scroll smoothly back to top, a menu bar that would fill the background color on scroll down and 'copy url' icon to encourage useres to share the app with others.

> Note: Throughout the design process, I kept referring back to my original 'Main Aims', 'User Stories' and preliminary research to make sure that my project was developing as intended.