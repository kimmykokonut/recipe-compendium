WIP

## Recipe Roundup

an exploration in Flask and Python while saving my favorite recipes to share

### Setup

1. clone project
2. navigate to directory
   $ cd recipes
3. make virtual environment
   $ python3 -m venv .venv
4. activate environment
   $ . .venv/bin/activate
5. install packages & dependencies
   $ pip install -r requirements.txt
6. initialize database file
   $ flask --app recipes init-db
7. run app on local server
   $ flask --app recipes run --debug
