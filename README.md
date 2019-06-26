# Django Todo-List
## Introduction
This project is a todo-list application created using the Django framework for python. The todo-list supports multiple users, and allows new users to register with a username and password. Pages for each user are inaccessible without that user being signed in, so the to-do list data for each user is private.

The project uses a MySQL database with Django for the backend, then Django's template engine for the frontend:

## File Structure
```

├── todo_list
│   ├── settings.py
│   ├── urls.py  
│   └── *.py
│
├── todo_app
│   ├── migrations
│   ├──static
│   │   └── todo_app
│   │       └──style.css
│   ├── templates
│   │   └── todo_app
│   │       └── *.html
│   ├── models.py  
│   ├── urls.py  
│   ├── views.py  
│   └── *.py
│
├── accounts
│   ├── migrations
│   ├── templates
│   │   └── accounts
│   │       └── *.html
│   ├── models.py  
│   ├── urls.py  
│   ├── views.py  
│   └── *.py
│
├── manage.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

The file structure of a Django project is pretty bulky. Many files exist just from creating the project and creating apps though, and several were never modified. The main areas that were modified within the program were the **urls.py** files (some of which were created by me), the **views.py** files, and on occasion, the **models.py** files and **settings.py** file. The files I created were pretty much only front-end files like .html and .css files, along with the files for Docker.

## Instructions

docker and docker-compose must be installed to run this application.

Start the project with:

```
> docker-compose up -d
```