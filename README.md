# Milestone Project 4: Speedy Eats Food Ordering Website

Website shown on various devices

## Live Project

View the live project

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


### User Goals

As a user, I would like the website to


### Administrator Goals

As a website administrator I would like the website to:


## User Experience

### User Stories

First time visitor goals:


Returning visitor goals


Frequent visitor goals:


### Design and Structure

The website consists of a number of pages which have a consistent structure and design.

#### Colour Palette

#### Typography

I chose the following typography:


### Wireframes

Wireframes of the initial design can be found in the following wireframes:

- Mobile wireframes
- Desktop wireframes

## Features

### Must Have (current features)

These are the features that have already been implemented on the website.

#### Navigation

#### Home page

### Could Have

- User friendly order numbers
- Check postcode to ensure the customer is in the delivery area

### Won't Have (for now)

- Dynamic order tracking
- Autocomplete address from postcode

## Technologies Used

## Database Structure

## Testing

### User stories tests

The user stories have been tested and the results are:

### Functionality

The functionality for various aspects of the site was tested and the results are:

- each app tested after creation by creating a basic view showing the text "It works"

### HTML Validation

### CSS Validation

## JS Validation

## Python Validation

### Accessibility and Performance

### Browser Compatibility

The website has been tested on the following browsers:

### Device Compatibility

### Check links work

## Bugs

Bugs fixed:
- Plural of Cateogry in admin was Categorys - added a Meta class to the Category model: verbose_name_plural = "Categories"
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

### Set up the Database

### Deploying locally

If you are going to deploy the application locally, you will need to create an `env.py` file. An example can be found in the [sample_env.py](/sample_env.py) file attached.

**DO NOT commit your `env.py` file to GitHub as it contains unique credentials to your database.** Make sure you add `env.py` to your .gitignore file.

### Deploying to Heroku

Ensure you have signed up to [Heroku](https://www.heroku.com/) then carry out the following:

- Select "New" > "Create New App"
- Create a unique app name and select the server region closest to you.
- Select "Create App"
- In the new app, select "Settings"
- Select "Review Config Vars"
- Complete your environment variables:
- Create the Procfile in the terminal: `echo web: python app.py > Procfile`
- Create the requirements.txt file in the terminal: `pip3 install -r requirements.txt`

To connect the GitHub repository to the Heroku App:

- Go to the app in Heroku
- Go to the "Deploy" tab
- Under "Connect to GitHub" search for your repository and click "Connect"
- To update the app every time you commit to GitHub, select "Automatic Deployment"

## Credits

Any images not referenced are owned by the developer. 

Attribution for code is included as comments and docstrings in the code itself.