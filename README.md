# SuperLists
That's a test from the book `Test-Driven Development with Python` by H.J.W. Percival. The goal of this project is to learn TDD.

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
    cd ~/projects/Learn_TDD
    python functional_tests.py
    cd ~/projects/Learn_TDD/superlists
    python manage.py tests

### Run the website
Go to http://localhost:8000/

## Urls of the project
### Main page
http://localhost:8000/
