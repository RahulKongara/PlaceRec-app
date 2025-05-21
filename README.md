# To run Backend

Make sure to setup your virtual environment before installing the dependencies.
The requirements.txt file contains all the dependencies required to be installed before running the backend.


`cd backend`
## Activate virtual env.
`py -m pipenv shell`

## If you are running the app for the first time or made changes since the last migration

`python manage.py makemigrations`
`python manage.py migrate`

## If you are running the app without making any changes since the last migration directly run cmd:

`python manage.py runserver`

The backend will run on http://127.0.0.1:8000/api/landmarks/

# To run Frontend

Run on localhost using:
`npm run dev`

# Note: This is not yet delpoyed to production and is still under development.
