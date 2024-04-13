# Flask Notes App

Website with with Python, Flask framework, authentication, databases, so on.
how you create a new user's account, how you store those in a database, how to log into those user accounts, how to log out of them, and how you associate that information with a specific user.

- folder structure of the python App
  env
  website
  --static
  --templates
  --**init**.py
  --auth.py
  --views.py
  --models.py
  main.py
- Before installing flask app, make sure you have python3 or download using the command
  `sudo apt install python3`
- If you have python3, then create a virtual environment to run flask,
  - `sudo apt install python3-venv` it downloads the environment.
  - `python3 -m venv venv` it creates the environment, run this command in the flask app folder.
  - `source venv/bin/activate` this command activates the virtual environment.
- Now install the flask app `pip install Flask`
- To check the version `python -m flask --version`
- Install its dependencies

  - `pip install Flask-login`
  - `pip install Flask-sqlalchemy`

## folders

### init

It creates the flask app, configured with secret key for the development environment.

### views

It contains the roots of the pages that we have in the projects like homepage, login page, so on.
using blueprint module
