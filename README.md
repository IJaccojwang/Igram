Picshare
===================
## Description
Picshare is anweb application that has pictures for users o view. One can add pictures through the admin section and search for pictures as well.

------------------------------------------------------------------------


## Features

+ [x] Photos gallery with most recent additions featured.
+ [x] Copying image links to share with friends.
+ [x] search functionality for users.
+ [x] Django admin dashboard for adding & managing posts.



## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/IJaccojwang/picshare.git && cd insta-clonewars
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.


## Running the tests
```bash
python manage.py test
```

## Live Demo

The web app can be accessed from the following link:
[Picshare](https://ijpicshare.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| View Images | On site load | All images displayed |
| View Categories | Click on category | List of categories is displayed |
| Add new image | Submit in admin page| View image on home page|
| Search for image | Submit search form | View images that meet search criteria|



## Contributing

- Git clone [https://github.com/IJaccojwang/picshare.git](https://github.com/IJaccojwang/picshare.git)
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Ian Jaccojwang](https://github.com/IJaccojwang)

