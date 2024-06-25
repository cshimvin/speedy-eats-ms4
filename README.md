# Milestone Project 4: Speedy Eats Food Ordering Website

![Website shown on various devices](/documentation/images/speedy-eats-layouts.png)

## Live Project

[View the live project](https://cshimvin-speedy-eats-9486f6bced13.herokuapp.com/)

## Table of Contents
1. [Project Goals](#project-goals)
- Business Goals
- User Goals
- Administrator Goals
2. [User Experience](#user-experience)
- User Stories
- Design and Structure
- Wireframes
3. [Features](#features)
- Must Have (current features)
- Could Have
- Won't Have (for now)
4. [Technologies Used](#technologies-used)
5. [Database Structure](#database-structure)
6. [Testing](#testing)
- User stories tests
- Functionality
- HTML Validation
- CSS Validation
- JS Validation
- Python Validation
- Accessibility and Performance
- Browser Compatibility
- Device Compatibility
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Project Goals

### Business Goals

As a business, I would like the website to:

- showcase the food and service we offer
- offer delivery of food to customers
- allow customers to buy food for delivery
- accept card payments online
- administer delivery drivers

### User Goals

As a user, I would like the website to

- offer a wide range of food online
- be easy to navigate and find the food I want
- offer payment online
- offer delivery of food to my home
- provide decent descriptions of food items so I know what I'm ordering
- allow me to write reviews on my experience

### Administrator Goals

As a website administrator I would like the website to:

- be easy to understand and navigate
- let me administer food items on the site
- let me check customer's orders
- create superusers in order for them to add and update food items
- view and update the minimum order value and current delivery time
- create, update and remove delivery drivers

## User Experience

### User Stories

First time visitor goals:

- As a first time visitor, I would like to easily find out about what food is on offer.
- As a first time visitor, I would like to easily order food online for delivery to my home.
- As a first time visitor, I would like to be able to pay for my order online.
- As a first time visitor, I would like to search for food to order.
- As a first time visitor, I would like to browse what food as available in each category.
- As a first time visitor, I would like to see how much I have spent so far and if I have met the minimum order requirements.
- As a first time visitor, I would like a smooth ordering and checkout process.
- As a first time visitor, I would like to receive confirmation of my order to ensure it has been processed correctly.
- As a first time visitor, I would like to view reviews so I know what to expect.

Returning visitor goals

- As a returning visitor, I would like to navigate the site and find other food to order.
- As a returning visitor, I would like to check on my previous orders.
- As a returning visitor, I would like to be able to save my details for further orders so I don't have to complete it every time.
- As a returning visitor, I would like a smooth ordering and checkout process.
- As a returning visitor, I would like to receive confirmation of my order to ensure it has been processed correctly.
- As a returning visitor, I would like to write a review on my previous experience.

Frequent visitor goals:

- As a frequent visitor, I would like to keep up to date with any new food items or special offers.
- As a frequent visitor, I would like to create a profile so I can save my delivery information for the future and to see all my previous orders.
- As a frequent visitor, I would like a consistent a familiar view of the site so I know what I need to do to order items.

As a website administrator:

- As a website administrator, I would like the website to be easy to understand and navigate.
- As a website administrator, I would like the website to let me administer food items on the site.
- As a website administrator, I would like the website to let me check customer's orders.
- As a website administrator, I would like the website to create superusers in order for them to add and update food items.
- As a website administrator, I would like the website to view and update the minimum order value and current delivery time.
- As a website administrator, I would like to create, update and remove delivery drivers.

### Design and Structure

The website consists of a number of pages which have a consistent structure and design. The background image was designed to convey the fact it is a food ordering site.

The main goal of the site is to allow users to browse, order and pay for food for delivery. They can also see how long the order is going to take to be delivered.

The website allows users to search for food items without logging in which should encourage users to register an account. This is why the log in and register links are consistently shown on the top navigation bar.

Once logged in, users can see their previous orders if they have any and save their information to their profile to save time and effort on future orders.

#### Colour Palette

I used brown for the main brand colour as this conveys earthiness which relates a lot to Indian food.

#### Typography

I chose the following typography:

- Roboto for the main body text font
- Reddit Mono for the page titles font

### Wireframes

Wireframes of the initial design can be found in the following wireframes:

- [Mobile wireframes](/documentation/pdf/speedy-eats-wireframes-mobile.pdf)
- [Desktop wireframes](/documentation/pdf/speedy-eats-wireframes-desktop.pdf)

## Features

### Must Have (current features)

These are the features that have already been implemented on the website.

#### Navigation

This is the main navigation on the site and is displayed on all site pages. It changes depending on whether a user is logged in or if the user is a superuser so that users only see the options they are authorised to see. It changes in appearance on smaller screens to prevent clutter.

On larger screens:

![Main navigation on larger screens](/documentation/images/main-nav-large.png)

On smaller screens:

![Main navigation on smaller screens](/documentation/images/main-nav-small.png)

My account menus:

![My account menu on navigation bar](/documentation/images/account-menus.png)

#### Footer

This is displayed on every page and contains links to the social media networks and details of the site itself.

![Footer](/documentation/images/footer.png)

#### Home page

This is the shop front which showcases which has 4 main features:

The header of the page to show what the website is about

![Header of the page](/documentation/images/header.png)

A link to the food menu

![Food menu link](/documentation/images/food-link.png)

The opening hours

![Opening hours](/documentation/images/opening-hours.png)

Any special offers

![Special offers](/documentation/images/special-offers.png)

#### Registration page

This allows a user to register an account which checks if the username doesn't already exist and then the data gets written to the database. It also validates the username and password to ensure it meets the requirements and returns a message if it doesn't. The password is saved as a hash to the database. It also logs the user in and adds a user session cookie.

![Registration form](/documentation/images/registration.png)

#### Log in page

his allows a user to log in so that they can see their past orders or carry out administration tasks if they are marked as a superuser in their user account on the database. It checks the username and password is valid when compared to the database entry then sets a "user" cookie to ensure the user stays logged in.

![Log in page](/documentation/images/log-in.png)

#### Product details page

This shows the details of the food item including it's price and the option to add a quantity of the item to their bag. If the user is logged in as a superuser then buttons are displayed to allow the food item listing to be edited or deleted.

![Product details](/documentation/images/product-detail.png)

#### Add a product page

This is available to logged in superusers only. It allows a product to be added to the database with details including the name, description, price, image and type of dish.

It contains validation so a negative price cannot be entered.

![Add product form](/documentation/images/add-product.png)

#### Shopping bag page

Once a user adds products to the shopping bag they can see what they have ordered so far and if there order has met the minimum order value.

![Shopping bag](/documentation/images/shopping-bag.png)

#### Checkout page

This shows the order summary and a form to input delivery details. The payment is handled by [Stripe](https://www.stripe.com) and by use of webhooks.

If delivery details previously saved by a registered user, the form will be pre-populated with these details. This is also an option to save delivery details for future purchases.

![Checkout page](/documentation/images/checkout.png)

#### Order confirmation page

This confirms that the order was processed successfully and that payment has been successfully handled. It shows a summary of the order number, contact information and delivery information. It also shows details of the order itself.

On checkout the user is sent a confirmation email with details about their order.

![Checkout success page](/documentation/images/checkout-success.png)

#### Profile page

This allows a logged in user to amend their personal details to ensure future purchases are made for quickly and efficiently by having details on orders made completed automatically. It also shows a user's previous orders which can be clicked on for further details.

![Profile page](/documentation/images/profile.png)

#### Add a Review Page

This allows a logged in user to write a review on their previous experience of the website and food.

This includes: Review Title, Review Body, Rating and Name

![Add a review page](/documentation/images/add-a-review.png)

#### Reviews page

This shows all users reviews left by other users of the site including a rating and date the review was left.

![Reviews page](/documentation/images/reviews.png)

#### Delivery Drivers Management page

This allows logged in administrators to view a list of delivery drivers and enables them to view the driver and edit driver details and remove drivers from the database. It also allows new drivers to be added.

![Delivery Drivers page](/documentation/images/delivery-drivers.png)

#### Add a Driver page

This allows logged in administrators to add a delivery driver to the database.

![Add a Driver page](/documentation/images/add-driver.png)

#### View a Driver page

This allows logged in administrators to view details of a specific delivery driver including staff number, name, phone number, vehicle type and registration.

![View a Driver page](/documentation/images/driver-details.png)

#### Edit a Driver page

This allows logged in administrators to edit details of a specific delivery driver including staff number, name, phone number, vehicle type and registration.

![Edit a Driver page](/documentation/images/edit-driver.png)

### Could Have

If there was more time available in this phase, the following features could be implemented:

- __More user friendly order numbers:__ At present the order numbers are quite complex. Displaying a more user friendly number means if a customer has to contact the retailer by phone, it is easier to give them the order number.
- __A postcode check__ to ensure the customer is in the delivery area.
- __A contact page__ for users to contact the retailer in case of any issues.
- When looking at the complete menu, the items could be divided into categories.

### Won't Have (for now)

- __Dynamic order tracking and delivery time estimate:__ Real time tracking of a users food order so they know how long it is going to be.
- __Autocomplete address from postcode:__ Allow users to have their address autocompleted from their postcode.

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5) to create the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS3) to style the website.
- [Bootstrap 4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) was used for the layout of the site.
- [FontAwesome](https://fontawesome.com/) was used to create some of the icons on the site.
- [Google Fonts](https://fonts.google.com/) was used to display the typography of the site.
- [Git](https://git-scm.com/) was used for version control of the code.
- [GitHub](https://github.com/) was used as a repository for the code.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [JQuery 3.3.1](https://jquery.com/) to create the functionality of the site
- [Python](https://www.python.org/) was used as the back-end programming language.
- [Gitpod](https://gitpod.io/) and [CodeAnywhere](https://codeanywhere.com/) were used as a cloud-based IDEs for development.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site together with the Jinja template.
- [ElephantSQL](https://elephantsql.com/) was used as the non-relational database management with Django.
- [Amazon AWS](https://aws.amazon.com/) was used for storing static and media files.
- [Heroku](https://www.heroku.com/) was used for hosting the deployed back-end site.
- [Balsamiq](https://balsamiq.com/) was used to create the project wireframes.
- [DBDiagram](https://dbdiagram.io/) was used to create the database schema diagram

## Database Structure

I used a relational database for this project as there were relationships between the Django models. I used SQLite during development and ElephantSQL when it went into production.

![Database schema](/documentation/images/db-schema.png)

## Testing

### User stories tests

The user stories have been tested and the results are:

|As a…                     |I want to…                                                                                                              |Result|
|--------------------------|------------------------------------------------------------------------------------------------------------------------|------|
|New customer              |Know what the purpose of the site is                                                                                    |PASS  |
|                          |I would like to easily order food online for delivery to my home                                                        |PASS  |
|                          |I would like to be able to pay for my order online.                                                                     |PASS  |
|                          |I would like to search for food to order.                                                                               |PASS  |
|                          |I would like to browse what food as available in each category.                                                         |PASS  |
|                          |I would like to see how much I have spent so far and if I have met the minimum order requirements.                     |PASS  |
|                          |I would like a smooth ordering and checkout process.                                                                    |PASS  |
|                          |I would like to receive confirmation of my order to ensure it has been processed correctly.                             |PASS  |
| | I would like to read reviews on the website | PASS |
|Returning customer        |I would like to navigate the site and find other food to order.                                                         |PASS  |
|                          |I would like to check on my previous orders.                                                                            |PASS  |
|                          |I would like to be able to save my details for further orders so I don't have to complete it every time.                |PASS  |
|                          |I would like a smooth ordering and checkout process.                                                                    |PASS  |
|                          |I would like to receive confirmation of my order to ensure it has been processed correctly.                             |PASS  |
| | I would like to leave and read reviews on the website | PASS |
|Frequent visitor          |I would like to keep up to date with any new food items or special offers.                                              |PASS  |
|                          |I would like to create a profile so I can save my delivery information for the future and to see all my previous orders.|PASS  |
|                          |I would like a consistent a familiar view of the site so I know what I need to do to order items.                       |PASS  |
| | I would like to leave and read reviews on the website | PASS | 
|As a website administrator|I would like the website to be easy to understand and navigate.                                                         |PASS  |
|                          |I would like the website to let me administer food items on the site.                                                   |PASS  |
|                          |I would like the website to let me check customer's orders.                                                             |PASS  |
|                          |I would like the website to create superusers in order for them to add and update food items.                           |PASS  |
|                          |I would like the website to view and update the minimum order value and current delivery time.                          |PASS  |
| | I would like to view, update, delete and create delivery driver staff members | PASS |


### Functionality

The functionality for various aspects of the site was tested and the results are:

|Feature                 |Expected Outcome                                                                                                                                                                                                                                                               |Action                                                                                                                                                                                                                                                                                                                                                                           |Result|
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|Navbar                  |When clicked it goes to the relevant page.                                                                                                                                                                                                                                     |When clicked it goes to the relevant page.                                                                                                                                                                                                                                                                                                                                       |PASS  |
|Navbar                  |When the navigation menu is displayed on a small screen it changes to a hamburger menu.                                                                                                                                                                                        |Resized the screen to show the hamburger menu.                                                                                                                                                                                                                                                                                                                                   |PASS  |
|Navbar                  |When logged in, the navbar hides the register and log in links and displays profile and log out links.                                                                                                                                                                         |Logged in as a user and confirmed it shows the profile and log out links and hides the log in and register links.                                                                                                                                                                                                                                                                |PASS  |
|Navbar                  |When logged in, the navbar displays the admin menu.                                                                                                                                                                                                                            |Logged in as an administrator and the navbar shows the Add a Product link.                                                                                                                                                                                                                                                                                                       |PASS  |
|Search bar              |When a search term is entered and the search button is clicked, the relevant results are displayed.                                                                                                                                                                            |Searched for “korma” and clicked the search button and a chicken korma dish was displayed.                                                                                                                                                                                                                                                                                       |PASS  |
|Log in form validation  |When a user submits their username and password in the log in page, the user gets logged in or an error message is displayed if there is no match to the username and password.                                                                                                |Tried the log in page with both valid and invalid details. When valid details were entered, I was logged in and a success message was displayed. When I entered incorrect details, an error message was displayed.                                                                                                                                                               |PASS  |
|Register form validation|When a user submits a new username, password and password confirmation in the registration page, the user details get added to the database and the user is logged in or an error message is displayed if there is the username already exists or the 2 passwords do not match.|Attempted to complete the registration form with an existing username and received a “username already exists” error message. Attempted to complete the registration form where the passwords didn’t match and received a “passwords don’t match” error message. Completed the registration form with a new username and passwords that match and it registered and logged me in.|PASS  |
|Add a product           |When an administrator completes and submits the form, the details are added to the database and a success message is displayed.                                                                                                                                                |Added the product details to the form and submitted the form. I received a success message and I checked the database and the details had been added.                                                                                                                                                                                                                            |PASS  |
|Edit a product          |The existing product details are displayed in the relevant form fields and when an administrator edits and submits the form, the details are updated in the database and a success message is displayed.                                                                       |Edited the product details on the form and submitted the form. I received a success message and I checked the database and the details had been updated.                                                                                                                                                                                                                         |PASS  |
|Delete a product        |When an administrator clicks on the delete link on a product in the product details page, the product is deleted.                                                                                                                                                              |Clicked on a delete link on a product page. I received a success message and I checked the database and the details had been updated.                                                                                                                                                                                                                                            |PASS  |
|Page not found          |When the incorrect web page address is entered, is produces a 404 page.                                                                                                                                                                                                        |Visited a page that doesn't exist in the site.                                                                                                                                                                                                                                                                                                                                   |PASS  |
|Shopping bag            |When a user goes to the shopping bag, the list of contents are displayed with a check out link. If the minimum order value hasn't been sent, a message is displayed and the checkout button is unavailable.                                                                    |Add products to the bag and visited the bag. The Contents were displayed correctly. With orders above the minimum value it let me click the checkout button but below the below this was disabled and a message displayed.                                                                                                                                                       |PASS  |
|Checkout                |When a user goes to the checkout they can complete their delivery and card details and pay for their order.                                                                                                                                                                    |Went to the checkout page and completed the delivery and payment details.                                                                                                                                                                                                                                                                                                        |PASS  |
|Checkout                |When a registered user goes to the checkout they can tick the box to save their delivery details.                                                                                                                                                                              |Went to the checkout page as a registered user and completed the delivery details and ticked the save details box. Went back into the bag and the details were saved.                                                                                                                                                                                                            |PASS  |
|Checkout success        |When a user submits their order at the checkout they received a success page with the order details.                                                                                                                                                                           |Submitted my order and a success page was displayed with order details.                                                                                                                                                                                                                                                                                                          |PASS  |
|Profile                 |When a registered user goes to the profile page, they are presented with a form to amend their details and information about their recent orders. If they are not logged in they are redirected to a log in page.                                                              |Went to the profile page as a logged in user and saw the form and order history. Went to the profile when not logged in and was presented with a log in page.                                                                                                                                                                                                                    |PASS  |
|Register                |When a new user goes to the register page, they are presented with a form to complete their details including a username and password to user in future.                                                                                                                       |Went to the registration page and was able to register successfully.                                                                                                                                                                                                                                                                                                             |PASS  |
|Home Page               |when a customer clicks on the food menu button, they are presented with a list of food items they can buy.                                                                                                                                                                     |Clicked on the "Browse our menu" button on the home page and was presented with the menu items available.                                                                                                                                                                                                                                                                        |PASS  |
| Write a Review page | When a logged in user visits the page, a form is presented where a user can write a review of their experience | Went to Add Review page and submitted a review successfully | PASS |
| View Reviews page | When a user visits the page, the reviews submitted are displayed on the page | Went to the Reviews page and saw a list of reviews | PASS |
| Delivery Driver Management | When a superuser visits the page, they see a list of delivery drivers with options to edit, delete, view and add drivers | Visited the Drivers page and was able to see a list of drivers and was able to click on the various links which took me to the correct locations | PASS |
| Add a delivery driver | When a superuser clicks on the add driver link on the driver list page, they are presented with a form to complete the various delivery driver details | Submitted the form on the page and form submitted correctly | PASS |
| Edit a delivery driver | When a superuser clicks on the edit driver link on the driver list page, they are presented with a form with existing information and can edit the various delivery driver details | Changed information on the form on the page and submitted it and form submitted correctly | PASS |
| Delete a delivery driver | When an administrator clicks on the delete link on a driver in the driver details page or driver list page, the driver is deleted. | Clicked on a delete link on a driver details page and on the driver list page. I received a success message and I checked the database and the details had been updated. | PASS |

When in development, each app was tested after creation by creating a basic view showing the text "It works".

### HTML Validation

All pages were tested using the [W3C HTML validator](https://validator.w3.org/nu/) and no errors were found. The results are in the [attached PDF document](/documentation/pdf/HTML-Validation.pdf).

### CSS Validation

The CSS stylesheet `base.css` was checked using the [W3C CSS validator](https://jigsaw.w3.org/css-validator/validator) and no errors were found:

![W3C CSS Validation results](/documentation/images/css-validation.jpg)

## JS Validation

There were only a few lines of in page javascript and a js file for Stripe. All javascript worked as expected and no console errors were displayed.

## Python Validation

The code was validated using Python's own Flake8 utility using the command `python3 -m flake8`

The results were:

![Flake8 results](/documentation/images/flake8-errors.png)

I generally resolved formatting errors as I went along using Gitpod's own Problems tab. The remaining errors are:
- A majority of the errors above are from automatically produced files (migrations. build-assets) so I left these alone.
- In `settings.py` I could not get the lines any shorter as they contained API keys which could not be broken up.
- In `checkout/webhooks.py` local variable 'e' is used for error handling so cannot be removed.
- `env.py` is not part of the deployed project since these variables are in the Heroku itself. This also impacts 'env' imported but unused error in `settings.py`
 - In `checkout/apps.py` checkout.signals is used for Stripe.

### Accessibility and Performance

Accessibility was checked to ensure that Aria labels and image alt text was added to all images and visual elements on the site.

A [Lighthouse report](/documentation/pdf/lighthouse-report.pdf) was also created which passed accessibility. There were also a few performance suggestions which could be implemented in future iterations.

### Browser Compatibility

The website has been tested on the following browsers:

- Google Chrome Version 121.0.6167.185 (Official Build) (64-bit)
- Microsoft Edge Version 123.0.2420.81 (Official build) (64-bit)
- Mozilla Firefox 122.0 (64-bit)

The layout, functionality and website works on all the above browsers.

### Device Compatibility

The responsiveness and layout of the site has been tested on a number of devices including tablets, desktops and mobile phones from iPhone 5 to 5K screens and the website displays correctly.

Chrome developer tools were used at various points during the development including when changes were made to the layout.

### Check links work

All links were tested manually and by using the [Broken Link Checker](https://chrome.google.com/webstore/detail/broken-link-checker/nibppfobembgfmejpjaaeocbogeonhch?utm_source=ext_sidebar&hl=en-US) extension on Google Chrome.

## Bugs

Bugs fixed:
- Plural of Category in admin was Categorys - added a Meta class to the Category model: verbose_name_plural = "Categories"
- Plural of Category names in page headers incorrect in some cases (e.g. Side Dishes was Side Dishs) - added a field to the Category model of category_name_plural
- JQuery did not work correctly to update and remove items from the bag. Found out I was using the slim version of JavaScript. Changed base template to load the main version of JavaScript
- Update link wasn't working in the bag as it was in the incorrect place on the page. Moved it outside the form and it worked.

## Deployment

### How the site was deployed

The site was deployed using GitHub and is hosted on Heroku and was deployed as follows:

### How to clone this repository

- Go to the repository at https://github.com/cshimvin/speedy-eats-ms4.git on GitHub
- Click on the Code button and copy the https URL under Clone
- Open a terminal on GitBash
- Navigate to the folder you want to store the cloned repository
- In the terminal type git clone and paste the URL of the cloned repository after it then press Enter
- The site will then be cloned to that directory

### Deploying locally

If you are going to deploy the application locally, you will need to create an `env.py` file. An example can be found in the [sample_env.py](/sample_env.py) file attached.

**DO NOT commit your `env.py` file to GitHub as it contains unique credentials to your database.** Make sure you add `env.py` to your .gitignore file.

### Deploying to Heroku

Ensure you have signed up to [Heroku](https://www.heroku.com/) then carry out the following:

1. Select "New" > "Create New App"
2. Create a unique app name and select the server region closest to you.
3. Select "Create App"
4. In the new app, select "Settings"
5. Select "Reveal Config Vars"
6. Complete your environment variables:

![Heroku Config Vars](/documentation/images/heroku-config-vars.png)

7. Create the Procfile in the terminal: `echo web: python app.py > Procfile`
8. Create the requirements.txt file in the terminal: `pip3 install -r requirements.txt`

To connect the GitHub repository to the Heroku App:

- Go to the app in Heroku
- Go to the "Deploy" tab
- Under "Connect to GitHub" search for your repository and click "Connect"
- To update the app every time you commit to GitHub, select "Automatic Deployment"

### Set up AWS for static files and images

<details>

<summary>Create the Bucket</summary>

1. Create an [Amazon AWS](https://aws.amazon.com) account
2. Search for S3 on the interface and create a new general purpose bucket with the same name as your Heroku app, select the region nearest to you and untick the block all public access box.
3. Tick the acknowledgement and select create bucket.
4. Go back into your bucket.
5. Under the Properties tab, enable static web hosting. Use `index.html` for the Index document and `error.html` for the Error document and select save changes.
6. Under the permissions tab, edit the CORS box with the following:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
7. Edit the Bucket policy and click on Policy generator.
8. Select S3 bucket policy and enter `*` in the Principal box and `GetObject` in the actions box.
9. Copy the ARN name from the Properties tab into the ARN box and click Add Statement.
10. Click Generate Policy.
11. Copy the box from the box and paste it into the Policy section of the Bucket Policy.
12. Add `/*` to the end of the ARN under the Resource field and click Save.
13. Edit the Access Control List under the Permissions tab and tick "List" under the "Everyone" group.
</details>
<details>
<summary>Create the Identity and Access Management for the bucket</summary>

1. Search for IAM on the interface bar.
2. Click on User Groups under Access Management.
3. Click on Create group.
4. Give the group a meaningful name.
5. Click on Create Group
6. Click on Policies under Access Management
7. Click Create Policy
8. Select JSON then Actions > Import Policy
9. Search for AmazonS3FullAccess and select it.
10. Click Import.
11. Get the ARN from the bucket created earlier.
12. Paste the ARN in the `Resource` field instead of `*` so it looks like the following:
```
"Resource": [
    "pasted-arn-name",
    "pasted-arn-name/*"
]
```
13. Give the policy a meaningful name and click on Create Policy.
14. Attach the policy to a Group by going to Access Management > User Groups.
15. Click on the group name created above.
16. Under the Permissions tab click on Add Permissions > Attach Policy
17. Search for the policy created above, select the policy and click Attach Policies.
18. Select Access Management > Users.
19. Click Create user.
20. Enter a meaningful name - e.g. `speedy-eats-staticfiles-user`
21. Click Next.
22. Select the group you created above and click Next.
23. Click Create User.
</details>
<details>
<summary>Retrieve the access keys</summary>

1. Go to IAM and select 'Users'
2. Select the user to create the CSV file.
3. Select the 'Security Credentials' tab
4. Go to 'Access Keys' and click 'Create access key'
5. Select 'Application running outside AWS' and click Next
6. Click 'Create Access Key'
7. Click the 'Download .csv file' button
You can then use this to complete the access keys in the Config Vars created above.
</details>

<details>

<summary>Connect Django to S3</summary>

1. Install boto3 and django-storages
```
pipenv install boto3
pipenv install django-storages
pip freeze > requirements.txt
```
2. In settings.py:
    1. Add `storages` to `INSTALLED_APPS`
    2. Set the AWS bucket config:
    ```
    if "USE_AWS" in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "speedy-eats"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    ```
    3. Set the static and media files storage and location and override static and media URLs:
    ```
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
    ```
3. Delete `DISABLE_COLLECTSTATIC` variable from the Heroku Config Vars and deploy the app.
4. Go to the bucket in AWS and create a `media` folder under Objects:
![Media folder](/documentation/images/bucket-media-folder.png)
</details>

### Set up the Database

1. Sign up for [ElephantSQL](https://customer.elephantsql.com/) and create a new instance.
2. Give the database a meaningful name (e.g. speedy-eats).
3. Use the Tiny Turtle plan.
4. Select your nearest region and click Review.
5. Select Create Instance.
6. Go into your database instance, copy the URL of the database and add it to the DATABASE_URL Config variable in Heroku.
7. In your terminal, enter the following to install apps to connect to your database:
```
 pip3 install dj_database_url==0.5.0 psycopg2
 pip freeze > requirements.txt
```
8. In the `settings.py` file, add the following:
```
 import os
 import dj_database_url
```
9. __Temporarily__ add the following to `settings.py` with your DATABASE URL copied above:
```
DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
 ```
10. In the terminal enter the following:
```
python3 manage.py showmigrations
python3 manage.py migrate
python3 manage.py loaddata categories
python3 manage.py loaddata products
```
11. Create a superuser in the terminal by adding a username and password after entering `python3 manage.py createsuperuser`
12. Replace the code entered in step 9 above to:
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
 ```
 __You must ensure you do this before committing any changes otherwise you'll expose your DATABASE URL__

## Credits

Images for the site have been taken from [Pexels.com](https://www.pexels.com) and are royalty free.

Attribution for code is included as comments and docstrings in the code itself.