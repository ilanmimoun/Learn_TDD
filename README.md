# SuperLists
That's a test from the book `Test-Driven Development with Python` by H.J.W. Percival. The goal of this project is to learn TDD.

## Requirements
  - Install __Virtualenv 15.1.0__ ([Tutorial](https://virtualenv.pypa.io/en/stable/installation/)).
  - Install __Python 3.6.3__ ([Tutorial](https://docs.python.org/fr/3.6/installing/index.html)).
  - Install __Django 2.0__ ([Tutorial](https://www.djangoproject.com/download/)).

## Initialization
### Get the code
    mkdir -p ~/projects/Learn_TDD
    cd ~/projects/Learn_TDD
    git clone https://github.com/ilanmimoun/Learn_TDD.git

### Install requirements
    cd ~/projects/Learn_TDD
    # Install requirements for django:
    pip install -r requirements.txt

### Run the Django server
    cd ~/projects/Learn_TDD/superlists
    python manage.py runserver

### Run the tests
    cd ~/projects/Learn_TDD/superlists
    python functional_tests.py
    python manage.py tests

### Run the website
Go to http://localhost:8000/

## Urls of the project
### Main page
http://localhost:8000/

### Admin page
http://localhost:8000/admin/
