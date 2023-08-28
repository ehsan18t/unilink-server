# Setup Guide
 - [ ] Clone this repository: 
    ```
    git clone https://github.com/ehsan18t/unilink-server.git
    ```
 - [ ] Install [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
 - [ ] Open project folder in terminal
 - [ ] Create `venv` by running 
    ```
    python -m venv venv
    ```
 - [ ] Activate `venv` by running 
    ```
    venv\Scripts\activate.bat
    ```
 - [ ] Install required packages: 
    ```
    pip install -r requirements.txt
    ```
 - [ ] Migrate database: 
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
 - [ ] Create admin account: 
    ```
    python manage.py createsuperuser
    ```
 - [ ] Run the server: 
    ```
    python manage.py runserver
    ```
 - [ ] Open [http://localhost:8000](http://localhost:8000) in your browser


# Full Documentations
 - [Documentations](https://github.com/ehsan18t/unilink-docs)

# API Documentation
 - [Frontend Repo](https://github.com/ehsan18t/unilink)
 - [API Tests (PostMan)](https://elements.getpostman.com/redirect?entityId=28446015-f0c7ad26-98e7-47f2-8120-82692c8865e5&entityType=collection)
 

# Resources
 - [Youtube Tutorial](https://www.youtube.com/watch?v=2pZmxh8Tf78)
 - [Blog](https://docs.digitalocean.com/tutorials/app-deploy-django-app/)
 - [Django Rest API](https://www.django-rest-framework.org/)
 - [Djoser Docs](https://djoser.readthedocs.io/en/latest/getting_started.html)
 - [JWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
 - [Django Docs](https://docs.djangoproject.com/en/)

