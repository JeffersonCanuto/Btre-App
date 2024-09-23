# Btre-App
BT Real Estate is a business app designed to connect customers with realtors who have properties available to purchase all across the United States.

# Software

## Update packages

```
# sudo apt update
# sudo apt upgrade
```

## Install Python 3, Postgres & NGINX

```
# sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

# Postgres Database & User Setup

```
# sudo -u postgres psql
```

You should now be logged into the pg shell

### Create a database

```
CREATE DATABASE btre_prod;
```

### Create user

```
CREATE USER dbadmin WITH PASSWORD 'abc123!';
```

### Set default encoding, tansaction isolation scheme (Recommended from Django)

```
ALTER ROLE dbadmin SET client_encoding TO 'utf8';
ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbadmin SET timezone TO 'UTC';
```

### Give User access to database

```
GRANT ALL PRIVILEGES ON DATABASE btre_prod TO dbadmin;
```

### Quit out of Postgres

```
\q
```

# Vitrual Environment

You need to install the python3-venv package

```
# sudo apt install python3-venv
```

### Create project directory

```
# mkdir pyapps
# cd pyapps
```

### Create venv

```
# python3 -m venv ./venv
```

### Activate the environment

```
# source venv/bin/activate
```

# Git & Upload

### Pip dependencies

From your local machine, create a requirements.txt with your app dependencies. Make sure you push this to your repo

```
$ pip freeze > requirements.txt
```

Create a new repo and push to it (you guys know how to do that)

### Clone the project into the app folder on your server (Either HTTPS or setup SSH keys)

```
# git clone https://github.com/yourgithubname/btre_project.git
```

## Install pip modules from requirements

You could manually install each one as well

```
# pip install -r requirements.txt
```

# Local Settings Setup

Add code to your settings.py file and push to server

```
try:
    from .local_settings import *
except ImportError:
    pass
```

Create a file called **local_settings.py** on your server along side of settings.py and add the following

- SECRET_KEY
- ALLOWED_HOSTS
- DATABASES
- DEBUG
- EMAIL\_\*

## Run Migrations
```
# python manage.py makemigrations
# python manage.py migrate
```

## Create super user

```
# python manage.py createsuperuser
```

## Create static files
```
python manage.py collectstatic
```

### Create exception for port 8000

```
# sudo ufw allow 8000
```

## Run Server

```
# python manage.py runserver 0.0.0.0:8000
```

### Test the site at YOUR_SERVER_IP:8000

Add some data in the admin area