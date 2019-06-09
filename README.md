# CBA Server -- Server-side Application for the Cost Benefit Analysis Subsystem

## 1. Initial setup
This project requires:
* Python >= 3.6
* PostgreSQL >= 9.6
* `pipenv` for Python virtual environment management

### 1.1. Setup the database
Before setting the Django codebase, please make sure that you have the access to a PostgreSQL instance (either on our local machine or some remote server).

* Create a database `cba_wb`
* Make sure you have in your hands the details of username, password, host, and port of this database.

### 1.2. Setup the repo
* Clone this repository: `git clone https://github.com/orma/cba-server.git`

* At the project directory root (i.e., `cba-server`), create an `.env` file and follow [environment variables guide](docs/environment_variables.md) to set the values for all the variables.

* After that, run `pipenv shell` to activate the Python virtual environment for this project

* Then run `pipenv install --dev` to install all required dependencies for this project. You would need to occasionally run this command as you fetch new updates from this repository

* Then run `python cba/manage.py migrate` to run all latest database migrations

* Then run `python cba/manage.py runserver` to start the development server

* And voila! You've completed the neccessary steps to set up a local development environment for this project.