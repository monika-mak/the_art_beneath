# The Art Beneath


Here is a link to the live project: [The Art Beneath](https://the-art-beneath-289b50439a5a.herokuapp.com)



![responsive](/documentation/display.png)

## Contents

- [Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
   * [User Stories](#user-stories)

- [Design](#design)
   * [Colour Scheme](#colour-scheme)
   * [Typography](#typography)
   * [Imagery](#imagery)
   * [Wireframes](#wireframes)
   * [Database Schema](#database-schema)

- [Features](#features)
   * [Home Page](#home-page)
   * [AI Tools Page](#ai-tools-page)
   * [Voting and Ranking](#voting-and-ranking)
   * [About Page](#about-page)
   * [Contact Page](#contact-page)
   * [Features to Add](#features-to-add)

- [Technologies](#technologies)
   * [Languages Used](#languages-used)
   * [Libraries & Programs Used](#libraries-and-programs-used)

- [Testing](#testing)

- [Deployment](#deployment)
   * [Deployment Process](#deployment-process)
   * [Forking](#forking)
   * [Clone](#clone)

- [Credits](#credits)
   * [Code](#code)
   * [Media](#media)

---


## Overview
The Art Beneath is a modern e-commerce platform dedicated to showcasing and selling contemporary art created by an artist, James Stanislaw. Inspired by my partner, an artist himself, this project aims to provide a seamless experience for art enthusiasts to browse, explore, and purchase unique pieces. 

The platform is designed to cater to art lovers who appreciate fine art, providing a secure and efficient way to connect with the work of James Stanislaw.

The inspiration for "The Art Beneath" comes from the idea that every artwork has layers of meaning and depth that go beyond the surface. The platform serves as a space to explore the unique and thought-provoking pieces created by James Stanislaw.

![Responsive Mockup](PLACEHOLDER_FOR_IMAGE)

---

## User Experience (UX)

AI Heroes visitors are individuals curious about AI, eager to explore its applications through straightforward examples and easy-to-understand explanations. They are looking for insights and guidance into the best AI tools available.

## User Stories

A list of user stories grouped into epics for better structure and clarity.

### EPIC | User Experience and Interface
- As a visitor, I want the website to be visually appealing and easy to navigate so that I have an enjoyable experience while exploring AI tools.
- As a visitor, I want to view the homepage so that I can learn about the website and the AI tools it features.
- As a visitor, I can navigate the website with ease so that I have an enjoyable experience exploring AI tools.
- As a user, I want to see tools in paginated format so that I don’t have to scroll through a long list of tools.
- As a visitor, I want to receive feedback (success/error messages) after completing actions so that I understand the outcome of my interaction.
- As a visitor, I want to access an error page with an option to navigate back to the homepage.
- As a visitor, I want to see social media links to follow the project and its author online. 

### EPIC | Content Management
- As an admin, I want to create, read, update, and delete posts so that I can easily manage my page content.
- As a Site Admin, I can approve or disapprove comments so that I can only display relevant topics.
- As a Site User, I can modify or delete my comment on a post so that I can be involved in the conversation.
- As a Site Admin, I can create draft posts so that I can finish writing the content later.
- As a Site Admin, I can create, update, or delete the about page content so that it is available on the site.

### EPIC | User Interaction and Engagement
- As a Site User, I am able to leave comments on a post so that I can share my opinion on the topic.
- As a user, I can view the comments so that I can be up to date with the recent engagement.
- As a Site User, I am able to click on the About link so that I can read the content of the site.
- As a user, I want to be able to send a message to the site owner so that I can address my query to the relevant people.
- As an admin, I can read the message sent by the user so that I can have a better understanding of their inquiries, needs, or feedback.

### EPIC | Voting and AI Tools Ranking
- As a visitor, I want to see the AI tools ranked by popularity based on votes so that I can easily identify the top-rated tools.
- As a user, I want to vote for an AI tool so that I can express my fascination and interest.
- As an admin, I want to monitor votes to prevent misuse and ensure fair voting.
- As a user, I want to see tools in a paginated format so that I don’t have to scroll through a long list of tools.

### EPIC | User Accounts and Authentication
- As a user, I want to log in using my email and password so that I can access personalized features.
- As a user, I want to register an account using my email and password so that I can interact more deeply with the website.

### EPIC | Deployment and Testing
- As an admin, I want to deploy the website successfully so that it is accessible to users and can be included in my portfolio.


   ![user_story_1](documentation/user_story_1.png)
   ![user_story_2](documentation/user_story_2.png)

[Back to top ⇧](#the-art-beneath)

## Design

- The look of this website was based loosely around The Code Institute's 'Codestar' wlakthorguh project as well as canva's  AI template.

    ![canva template](documentation/canva_template.png)

### Color Scheme

- **Primary Colors**:  
  The website uses a futuristic combination of deep blues, purple and  grey on a white background to create a clean and modern aesthetic. These colors reflect the technological theme while maintaining readability and simplicity.

- **Accent Colors**:  
  Bright accents like orange and purple are used to draw attention to interactive elements, such as buttons and links, enhancing the user experience and reinforcing the AI theme.

  ![Design Colors](documentation/design_colors.png)


### Typography
- The **Audiowide** font is used as the primary typeface, chosen for its retro style that complements the futuristic and technological concept of AI Heroes. It gives the site a unique personality while remaining readable and visually appealing

    ![Fonts](documentation/font.png)

### Imagery
- The **main image** features a matrix-style blue background with a superhero robot flying across, representing the fusion of futuristic ideas and AI technology.
![Main Image](documentation/main_hero_bg.png)

### Wireframes

![Home Page](/documentation/wireframes/home_wireframe.png)
![Leaderboard](/documentation/wireframes/leaderboard_wireframe.png)
![About& Contact](/documentation/wireframes/about_contact_wireframe.png)
![Post Detail](/documentation/wireframes/detail_wireframe.png)
![Login](/documentation/wireframes/login_wireframe.png)
![Register](/documentation/wireframes/register_wireframe.png)


### Database Schema 

![Database Schemas](/documentation/erd_schema.png)

[Back to top ⇧](#the-art-beneath)

## Features
This section outlines the core functionalities of the platform.

#### __Navigation Bar__
- A fully responsive navigation bar available across all pages, providing access to:
  - Home Page (via logo)
  - Gallery
  - Categories
  - Filter
  - About
  - Contact
  - Search 
  - Shopping Cart
  - Wishlist
  - User Profile (if logged in)
  - Art Managament (if superuser)
  - Login/Sign up /Logout options
- Ensures intuitive navigation for users across different devices.

#### __Footer__
![Footer ](/documentation/logged_in_lrg_home.jpeg)

- The footer rests at the bottom of each page it includes :
 - link to Facebook page .Clicking the links in the footer opens a separate browser to avoid pulling the user away from the site.
 - invitation to subscribe to a newsletter with form to enter email adress; 
 - copyright messag for clarity and purpose of the website; 

### __Home Page__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- **Hero Section**:  
  A visually striking hero section welcomes users with a title and a brief message that evokes curiosity. 
  - shop now button available for users to interact with from the get go


#### __Art Listings Page__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Displays all available art pieces with:
  - Large, spacious image (for logged users it links to detail page when clicked ) 
  - Art name
  - Price
  - Add to bag option 
  - Add to wishlist
- Users can click on an art piece to view more details, they can also add the piect into the shopping bag or their personalised wishlist.
- For admin, additional functions appear when logged in:
  - Delete art
  - Edit art 

#### __Individual Art Details Page__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Provides detailed information about each piece, including:
  - Name
  - Price
  - Description
  - Image gallery
  - Size information
  - Color meaning details
- Includes an "Add to Cart" button (visible for logged-in users only).

#### __Category-Based Browsing__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can filter art pieces by categories such as:
  - Nature
  - Female
  - Animals
  - All Categories
- Improves discoverability of relevant art.

#### __Filter-Based Browsing__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can filter art pieces by :
  - New
  - Category
  - Price
  - Orientation
  - All Art
- Improves discoverability of relevant art.

#### __Contact Us__
![Contact Us ](/documentation/logged_in_lrg_home.jpeg)
- Allows any visitor to contact site owner :
  - Contact Page. Users can contact the site owner using the contact form. If the user is logged in, their email is pre-filled in the email input field. If the query is related to particular art owrk or desired size, users can select from the list of available pieces along with dedicated space for custom size to make the context more targeted. 

- Improves communication, feedback.

#### __FAQ__
![FAQ ](/documentation/logged_in_lrg_home.jpeg)
- Displays the most frequently asked questions about the site.
  - Provides users with essential information and quells worries that they may have about the site and its products.


#### __Shopping Bag__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Allows users to:
  - View selected items
  - See total cost (including delivery fees)
  - Adjust quantity
  - Remove unwanted items
  - View a dynamic price update when changes are made

#### __Secure Checkout__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Features include:
  - Secure payment form supporting credit/debit cards, PayPal, and other methods
  - Validation of payment fields
  - Encrypted transactions using HTTPS/SSL

#### __Order Confirmation & Email Notifications__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- After successful checkout:
  - A confirmation page displays order details as well as personalised message from the artist. 
  - Users receive an email receipt with purchase details and estimated delivery date

#### __Search & Sorting__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Search for art by name or description
  - Sort listings by price (low to high/high to low)
  - Filter results based on categories

#### __Wishlist Feature__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Logged-in users can:
  - Save art pieces for future purchases
  - Access their wishlist anytime

#### __Store Management__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Administrators can:
  - Add new art pieces by James Stanislaw with detailed information
  - Edit/update existing listings
  - Delete unavailable art pieces

#### __User Account Management__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Register an account
  - Log in/out securely
  - Reset forgotten passwords
  - View order history in their profile

#### __Login Page__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Register an account

#### __Register__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Register an account

#### __Logout__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Register an account


#### __Secure Checkout Page__
![Home Page ](/documentation/logged_in_lrg_home.jpeg)
- Users can:
  - Register an account

- **Add Product Page - Admin Only**

    - Add Product Page. Admins can use this form to add new products to the site. User-friendly form inputs allow product objects to be created simply and quickly.

![screenshot](documentation/features/sitepages/add-product.png)

- **Edit Product Page - Admin Only**

    - Edit Product Page. Admins can use this form to add edit products to the site. User-friendly form inputs allow product objects to be edited simply and quickly. A message at the top of the page informs the admin which product they are editing.

![screenshot](documentation/features/sitepages/edit-product.png)

### User Features

- **User Registration**

    - Users can register for an account using a front-end form. This creates a user object in the database and automatically secures the user's sensitive information.

![screenshot](documentation/features/user/register.png)

- **User Login**

    - Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.

![screenshot](documentation/features/user/login.png)

- **User Logout**

    - Users who are logged in can easily log out in order to stop access to their account-based information and functionality.

![screenshot](documentation/features/user/logout.png)

- **User Password Recovery**

    - Users who have forgotten their password can recover their password via the forgot password link on the login page. Users will enter their email and get a password reset link sent to their account email which they can use to set a new password.

![screenshot](documentation/features/user/password-recover.png)

- **Toasts**

    - Users see helpful popup messages when performing actions on the site. These messages inform the user of the success or failure of their actions, as well as providing information about an action taken, or steps that the user must take in order to correct an action.

![screenshot](documentation/features/user/toast1.png)
![screenshot](documentation/features/user/toast2.png)
![screenshot](documentation/features/user/toast3.png)

- **Basket Updates**

    - Via toasts, users can see a summary of their basket whenever an item is added, allowing the user to quickly see the new state of their basket, without having to navigate away from the page they are currently on.

![screenshot](documentation/features/user/basket-update.png)


- **Login Dependant Navbar Links**

    - Users who are logged in see new links in the navbar. 'Register' and 'Login' links are replaced with 'My Account' links. This provides the user with visual feedback upon logging in, as well as removing links that they will not need.

![screenshot](documentation/features/user/login-navbar-links1.png)
![screenshot](documentation/features/user/login-navbar-links2.png)

- **Login Redirect**

    - Users who are not logged in who attempt to access an area of the site which requires login are redirected to the login page. After logging in, they are sent to the page they first intended to visit.

![screenshot](documentation/features/user/login-redirect.png)

- **User Profile Creation**

    - User profiles are automatically created upon user registration. This assigns each user a profile which they can use to see/update their user information.

![screenshot](documentation/features/user/profile-creation.png)

- **User Profile Update**

    - Users can update their profile information using a front-end form located on their user profile page. This allows users to update profile information or correct possible mistakes made at registration.

![screenshot](documentation/features/user/profile-update.png)

- **User Contact**

    - Users can use a front-end form to message the site owners. The form is easy to use and pre-fills the user's email address if they are logged in. Users get confirmation that their message was sent, and a message that someone from the site will be in touch as soon as possible

![screenshot](documentation/features/user/contact.png)


- **User Email Confirmations**

    - After making a purchase or subscribing to the newsletter, the site automatically sends the user a confirmation email which contains their purchase details, or in the case of newsletter subscription, a thank you message and a link to unsubscribe.

![screenshot](documentation/features/user/email-confirmation1.png)
![screenshot](documentation/features/user/email-confirmation2.png)

- **Newsletter Subscribe**

    - Users can use a button in the footer of all site pages to subscribe to the site newsletter. If the user is logged in, the email input field will pre-fill with the user's email. Users see a confirmation screen after subscribing, and receive a confirmation email to the address they provided.

![screenshot](documentation/features/user/newsletter1.png)
![screenshot](documentation/features/user/newsletter2.png)


### Admin Features

- **Create Products**

    - Administrators can use a front-end form to create new site products. The form is simple and clean and automatically formats and displays the created product in the same manner as existing products.

![screenshot](documentation/features/admin/create-product.png)

- **Edit Products**

    - Administrators can use a front-end form to update existing products. If the current logged-in user has superuser privileges, an edit button will appear under products which allows that user to edit the product's details.

![screenshot](documentation/features/admin/update-product.png)

- **Delete Products**

    - Administrators can use a front-end form to delete existing products. If the current logged-in user has superuser privileges, a delete button will appear under posts which allows that user to delete that product.

![screenshot](documentation/features/admin/delete-product.png)

- **Webhooks**

    - The site uses a secure and robust webhook system to ensure that the payment process cannot be interrupted and corrupted, either through user error or malicious intent. Webhooks are incorporated via the Stripe payment system and are handled on the Stripe website, by way of the python code in `checkout > webhook_handler.py` and `checkout > webhooks.py`

![screenshot](documentation/features/admin/webhooks.png)


- **Contact Requests**

    - Admins can see a list of all of the contact messages sent by users. Messages are displayed in an easy-to-read table, with all of the salient information presented. Messages are automatically sorted with those messages which have not been responded to at the top of the list, with the oldest (the message which has gone unanswered the longest) at the top. Admins can click on the view details links to see the full contact messages, as well as respond to the message.

![screenshot](documentation/features/admin/contact-requests.png)

- **Contact Details**

    - Admins can see details of a contact message left by the user. All of the contact message's information can be seen, including email, name, subject, message, and whether this contact message has been respond to. Contact messages can be responded to or deleted via the large buttons at the bottom of the page. A link navigates back to the contact requests page.

![screenshot](documentation/features/admin/contact-details.png)

- **Contact Message Delete**

    - Admins can delete contact messages from the database using a front end delete function inside the contact message details page.

![screenshot](documentation/features/admin/contact-delete.png)

- **Contact Respond**

    - Admins can respond to user contact messages using an email form which appears upon clicking the 'respond to message' button on the contact details page. A text area appears with the user's name and the default email signoff link pre-populated for efficiency in the typing of the response. The 'Send Email' button sends an email response to the user's given email address with the content of the text box as the body of the email.

    The contact message is then automatically marked as 'Responded' and the 'respond to message' button no longer appears on that message's details page.

![screenshot](documentation/features/admin/contact-respond1.png)
![screenshot](documentation/features/admin/contact-respond2.png)
![screenshot](documentation/features/admin/contact-respond3.png)

- **Newsletter Confirmation Emails**

    - Emails are automatically sent out to all new subscribers of the site newsletter. The email contains a 'thank you' message, as well as a link to allow users to unsubscribe from the mailing list.

![screenshot](documentation/features/admin/newsletter-confirmation-email.png)

---
### Features Left to Implement
- User reviews and ratings for art pieces
- Social media sharing options
- AI-powered art recommendations based on browsing history

---

## Responsiveness (Main Pages)

### Home 
  <details>
  <summary>Home Page Full View</summary>

  ![Home Large](/documentation/logged_in_lrg_home.jpeg)
  ![Home Medium](/documentation/logged_in_md_home.jpeg)
  ![Home Small](/documentation/logged_in_sm_home.jpeg)
  </details>

![Home Large](/documentation/home_responsive.png)


<!---- more examples here      -------------------------------------------------------->





---

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter system, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

I also played around with [Word Tracker](https://www.wordtracker.com) a bit
to check the frequency of some of my site's primary keywords (only until the free trial expired).

- ![screenshot](documentation/wordtracker.png)

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://web-piano-academy-16cd779294ab.herokuapp.com

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://web-piano-academy-16cd779294ab.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the
[Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip)
provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more. 

Users can also unsubscribe from the newsletter by following the link in their subscription confirmation email.


## Technologies Used
- **Frontend:** HTML, CSS, JavaScript, Bootstrap;
- **Backend:** Django (Python), PostgreSQL
- **Authentication:** Django Authentication System
- **Deployment:** Heroku
- **Image Hosting:** Cloudinary (for storing and managing art images)

### Libraries and Programs Used

- [Git](https://git-scm.com/)
  - Version control.
- [GitHub](https://github.com/)
  - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
  - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
  - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
  - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
  - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
  - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used to help fix problem areas and identify bugs.
- [Cloudinary](https://cloudinary.com/)
  - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
  - Used to generate the site's favicon.
- [SQlite](https://www.sqlite.org/index.html)
  - Used when performing unit tests.
- [PostgreSQL](https://www.postgresql.org/)
  - Database used through heroku.
- [Lucidchart](https://www.lucidchart.com/)
  - To draw out the database schema.
- [W3C Markup Validation Service](https://validator.w3.org/) 
  - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
  - Used to validate CSS code.
- [Pep8](http://pep8online.com/)
  - Used to validate Python code.
- [JSHint](https://jshint.com/)
  - Used to validate JS code.
- [Tinyjpg](https://tinyjpg.com/)
  - Used to compress images.
- [Heroku](https://www.heroku.com/)
  - To deploy the project.
- [Canva](https://www.canva.com/)
  - Used for robot and  background images as well as wireframes and inspiration
- [ChatGPT](https://chatgpt.com/)
  - Used for general queries and quick help.
- [Claude3.5](https://claude.ai/)
  - For insightful explanations of topic. 
- [ YouTube](https://www.youtube.com/) 
  - For tutorials and other learnigs. 

[Back to top ⇧](#ai-heroes)
---

## Testing
Comprehensive testing has been conducted to ensure a smooth user experience.

### Validator Testing
- **HTML**: Passed through W3C Validator
- **CSS**: Passed through W3C CSS Validator
- **Python**: Code checked using PEP8 linter

### Unfixed Bugs
- Some minor UI inconsistencies on mobile devices (planned for future updates).

---

## Deployment


The live deployed application can be found deployed on [Heroku](https://the-art-beneath-289b50439a5a.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: web-piano-academy).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or web-piano-academy
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/LewisMDillon/web-piano-academy) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/LewisMDillon/web-piano-academy.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/LewisMDillon/web-piano-academy)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LewisMDillon/web-piano-academy)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Credits





---

## Credits
### Content
- Product descriptions written for the fictional artist James Stanislaw.
- Color meaning interpretations sourced from art theory references.

### Media
- Images created as part of the fictional artist’s collection.
- Icons sourced from [Font Awesome](https://fontawesome.com/).

---
