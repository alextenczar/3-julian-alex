# COMP805 Project: NHSEE Web App
# URL: https://nhsee-team3.herokuapp.com
## Project Team 3: Julian Quach and Alex Tenczar
This web app imports cell data from a XLSM Spreadsheet and
populate various data models within a Django database. The data is then able to be displayed and sorted by any model's attributes.

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
