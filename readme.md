# COMP805 Project: NHSEE Web App
## Project Team 3: Julian Quach and Alex Tenczar
This web app imports cell data from a XLSM Spreadsheet and
populate various data models within a Django database. The data is then able to be displayed and sorted by any model's attributes.

## Prerequisites:
### Python 3.7 or newer.
### Django 2.2.5
Installation:
$ pip install django Django==2.2.7

### import_export: https://django-import-export.readthedocs.io/en/latest/
Installation:
$ pip install django-import-export

### OpenPyxl: https://openpyxl.readthedocs.io/en/stable/#
Installation:
$ pip install openpyxl

## Usage:
### Local Setup:
1.Open your pip environment: "$ pipenv shell"
2.Start the server: "$ python manage.py runserver"

### Webapp Usage:
In order to import the spreadsheet: Click "Import File" in the Navbar
    1. Click "Choose File" and locate the spreadsheet file. (XLSM Format)
    2. Click "Import"
    3. Navigate back to one of the pages used to display the models. They should now be imported and display.

Each Navbar link will display a table for each model.
Clicking the headers of each column will sort by that column's object name.