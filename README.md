# Setup Project
## Clone this repository

Create Virutual enviornment using `requirements.txt` file.

Start project using `python manage.py runserver`

Open link `http://127.0.0.1:8000/admin` in browser.

Use credentials `username : admin , password : admin` for login
Note: I have added default user admin, you can use admin/admin credentials for that admin user. For implement authenticatin in API i have used this.

After login into the admin panel, goto Token model and copy token for API calls.

## APIs list will be below.
- http://127.0.0.1:8000/api/v1/cars/car/
- http://127.0.0.1:8000/api/v1/cars/car/{id}/
- http://127.0.0.1:8000/api/v1/cars/rate/
- http://127.0.0.1:8000/api/v1/cars/popular/

## For test case use below command
`python manage.py test apps.car.tests`

