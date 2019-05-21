IGRAM
===================
## Description
Igram is a web application that has pictures for users to view. It is a clone of popular photo sharing service instagram with a personal touch.

------------------------------------------------------------------------


## Features

+ [x] Photos feed with pictures recently added.
+ [x] Liking of images.
+ [x] Commenting on images.
+ [x] Following users.
+ [x] Viewing user profiles: Profile picture and bio
+ [x] User authentication system: login and sign up.
+ [x] Django admin dashboard for site management.



## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/IJaccojwang/igram.git && cd insta-clonewars
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
[Igram](https://igram.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| View Images | On sign in | All images displayed |
| View User profile | Click on User you want to view | User profile info displayed |
| Upload image | Submit new image upload form| Image uploaded, view on feed|
| Like image | Click like button | Number of likes on image increases|
| Comment on image | Submit comment | Comment recorded under image page|



## Contributing

- Git clone [https://github.com/IJaccojwang/igram.git](https://github.com/IJaccojwang/igram.git)
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Ian Jaccojwang](https://github.com/IJaccojwang)

