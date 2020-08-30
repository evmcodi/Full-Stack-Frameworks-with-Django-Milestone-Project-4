# Definitions App
Definitions is a website that allows users to purchase access to a software as a service (SaaS) app that allows the user to store and access terms and definitions that they learn. It can be used for students keeping a *personal dictionary* of terms that they learn through an education course or for professionals to support learning and retention of job-specific terms. People could also use this in their free time to keep a log of new phrases and terms related to any hobbies that they enjoy. It can be accessed on desktop, tablet and mobile devices, and because the terms are stored on a cloud database the users own terms can be accessed from any browser by using their login username and password.

This website is built using Django 3, Python 3, SQLite, Postgres, Heroku, AWS, Stripe, Javascript, HTML and CSS for the Code Institute Full Stack Frameworks milestone project. 

Email verification is required to register as a user of the site. 

Payment with a test credit card with code `4242 4242 4242 4242`, CVC of `424` and Zip code of `24242` is required to access the Definitions software application.

Live demo is hosted here: https://definitions-web-app.herokuapp.com/.

![Desktop Demo](/assets/readme-main.png "Desktop Demo")



## UX

### Strategy

In any area of study there are many new terms and definitions to learn and retain for future use. Students, professionals and hobbyists could be more capable and confident in their learning of their subjects of interest with a tool that helps them keep track of these new terms and their definitions. The definitions website provides access to a cloud-based personal dictionary for a yearly charge of €20. 


### Scope

The goal for this site is to provide a service to make it easy and intuitive for users to store and access terms and definitions that they learn. For the owner of the website the goal is to sell subscriptions to the product and to provide a good experience to the customers so that more customers will purchase access to the product, cover the costs of hosting, and provide a profit to the company.

Initially the website owner is selling to consumers directly (B2C) due to project scope constraints, but in future Enterprise licences could be sold to organisations (B2B) to provide a space for collaborative term dictionaries for employee on-boarding and training. 

#### User Stories

**Website Owners Goals**

As a website owner, I want to:
- Create a site that attracts customers to purchase yearly subscriptions.
- Allow marketing employees to publish regular blog posts on the site without them having administrative superuser access to the site database.
- Prevent users who have not logged in or have not paid the subscription fee from accessing the Definitions software.
- Prevent users who do not have 'Publisher' permission from creating new blog posts on the site.
 
**End-users goals**

As a student, I want to:
- Enjoy using a tool to help store and retrieve terms and definitions so they can be remembered and studied again.
- Not have to click a 'Save' button in order to store my new terms. I don't want to lose terms that I have added if I exit the browser tab by mistake.
- Interact with a simple user interface where the navigation bar doesn't show irrelevant links when I'm logged in.
- Keep up to date with any new features of the site or articles on learning that are available to read on a News page for the website.
- Use the app on mobile, tablet and desktop devices.




### Structure

The site's content structure contains the following main views.

- Home: An introduction to the site with a dynamic counter of items in the mongodb collection.

- Blog: A page on the website where both logged-in and anonymous visitors to the site can check on what the latest updates on the software are. Users with the 'Publisher' permission can also use this page to publish new blog posts without needing superuser access to the Django administration panel.
- New blog post: A page that allows publisher users to add new blog posts to the site for marketing purposes and user engagement.

- Definitions App: A page that shows you all your terms and their definitions in a list. Includes buttons to add, update and delete terms.
- Add Term/Definition modal: A modal allowing you to add a new term & definition.
- Edit Term/Definition modal: A modal allowing you to edit one of your terms/definitions.
- Delete Term/Definition modal: A modal asking for confirmation before you delete a term/definition from the database.

- Register & Login pages: Pages that allow new users to register, verify their emails and log in to the site.

- Payment: A page that allows logged-in users to pay for a yearly subscription to the service.
- Payment-Success: A page that confirms a successful payment by the user and directs them to the Definitions App software page.

#### Information Architecture





### Skeleton - Wireframes

Wireframes were created in two mockup tools. quickMockup for the initial mockups. Webflow for more advanced mockups.

The wireframes are available to view in the [wireframes folder in this Git repository](https://github.com/evmcodi/Full-Stack-Frameworks-with-Django-Milestone-Project-4/tree/master/assets/wireframes).



### Surface - Colours, fonts etc.

#### Colour scheme
I chose a simple white and light grey, black and slate blue colour scheme. This was based on the familiarity to a regular physical English dictionary book.

#### Fonts

Fonts were hosted by Google Fonts.

Headings: Poppins
Other text: DM Sans

#### Layout


#### Images



## Features



### Features to Implement




## Testing

### Process of testing User Stories

The user stories were tested manually.


**Website Owners Goals**

As a website owner, I want to:
- Create a site that attracts customers to purchase yearly subscriptions.
> Home page is working as a landing page. Log in, payment are working.
- Allow marketing employees to publish regular blog posts on the site without them having administrative superuser access to the site database.
> 
- Prevent users who have not logged in or have not paid the subscription fee from accessing the Definitions software.
> 
- Prevent users who do not have 'Publisher' permission from creating new blog posts on the site.
>


**End-users goals**

As a student, I want to:
- Enjoy using a tool to help store and retrieve terms and definitions so they can be remembered and studied again.
>
- Not have to click a 'Save' button in order to store my new terms. I don't want to lose terms that I have added if I exit the browser tab by mistake.
>
- Interact with a simple user interface where the navigation bar doesn't show irrelevant links when I'm logged in.
>
- Keep up to date with any new features of the site or articles on learning that are available to read on a News page for the website.
>
- Use the app on mobile, tablet and desktop devices.
>


## Deployment

### Local deployment
On a local desktop this app can be run by cloning this repo, making sure Python3 is installed, creating a new virtual environment with the bash command `python3 -m venv my_env`, installing the python modules in requirements.txt.

Then in your local environment set the following environment variables.

On linux this can be done with bash in the terminal with the command `nano .bashrc`

```bash
export SECRET_KEY=<>
export DEVELOPMENT="True"

###  using these for Stripe
export STRIPE_PUBLIC_KEY=<>
export STRIPE_SECRET_KEY=<>

```

## Credits

### Technologies Used

Languages:
- HTML
- CSS
- Javascript
- Python

Libraries:
- JQuery
- Bootstrap 4
- Django

Services:
- Heroku
- Postgres
- AWS S3 bucket
- Stripe

### Devlopment tools used

#### VSCode

- Free IDE developed by Microsoft.

#### Live server extension for VSCode 
- Auto-reloads the site preview in the browser after a file is edited and saved. 
- Also allows viewing and testing your site on other devices connected to the same local network.
- https://github.com/ritwickdey/vscode-live-server

#### Beautify css/sass/scss/less
- Extension for VSCode that allows instant formatting of CSS files with Ctrl-Shift-I shortcut.

#### Firefox & Developer Tools
- Browser with developer tools for previewing UI.

#### Git & Github
- Git is used for version control of code is preinstalled on most Linux distributions. 
- Github.com is used for storing version-controlled code online and as a cloud backup.

#### Heroku
- Heroku is used for deployment of the code online.

#### quickMockup
- https://jdittrich.github.io/quickMockup/

- Free open sourece tool for wireframing websites. Allows export to html.


#### Webflow
- A realistic mockup creator that uses the CSS box model.


<br><br>
*This site is not intended for commercial use*
