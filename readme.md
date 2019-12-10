## COMP805 Project: NHSEE Web App

### Project Team 3: Julian Quach and Alex Tenczar

### Heroku link: https://nhsee-team3.herokuapp.com/

### Description:

This web app imports cell data from a XLSM Spreadsheet and populates various data models within a Django PostGreSQL database. The web app is then able to display the models and sort them by any attribute. The web app can then calculate all scores and rank projects according to NHSEE's formulas and provided data. Our database can be locally and remotely accessed.

![](https://imgur.com/0q1ZSsn.png)

## Prerequisites:
#### Python 3.7 or newer
#### Django 2.2.5
#### The Python Packaging Tools: Pip and Pipenv
#### The GitHub Repository

## Installation:

#### 1. Create a new pipenv development environment inside the project folder and activate it with "pipenv shell".
#### 2. Within the directory containing the pipfile, enter the command "pipenv sync".
      This will install all the necessary dependencies.

## Running Locally:
#### 1. Enter pipenv environment if not activated: "$ pipenv shell"
#### 2. Start the server: "$ python manage.py runserver"  
       The web server should now be accessible at: 127.0.0.1:8000 from your web browser.
       
### Webapp Usage:
In order to import the spreadsheet: Click "Import File" in the Navbar
1. Click "Choose File" and locate the spreadsheet file. (XLSM Format)
2. Click "Import"
3. Navigate back to one of the pages used to display the models. They should now be imported and display.

Each Navbar link will display a table for each model.
Clicking the headers of each column will sort by that column's object name.

## Overall Project Status:
#### Status: 95% Functional
#### Our project is able to do all essential tasks proposed.

Import provided spreadsheet

Display Imported Data

Modify Data if necessary

Calculate all ranking and scoring values using provided data

Sort data by value according to user's choice

Display data remotely on a server (accessible to anyone with URL)

Display top 5 projects by score and category

### Additional Feature Statuses:

### 1. Scoring page:
#### Status: Incomplete
Able to create the scoring page using ModelForm, having problems with saving objects.

## Special Thanks to:

#### The Python Software Foundation:
https://www.python.org

#### The Django Software Foundation:
https://www.djangoproject.com

#### Eric Gazoni and Charlie Clark for OpenPyxl:
https://openpyxl.readthedocs.io/en/stable/

#### Stuart Langridge for Sorttable:
https://kryogenix.org/code/browser/sorttable/

#### Kenneth Reitz for Pipenv:
https://pipenv.kennethreitz.org/en/latest/

#### PostgreSQL Global Development Group:
https://www.postgresql.org

#### NHSEE for giving us a chance to work on a real life project:
https://nhsee.org

#### Lastly, thank you to all COMP705/805 Teams and Professor Mihaela Sabin!


