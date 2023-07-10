# Initial Setup
## Install necessary Packages in Django
```
pip install djangorestframework djoser django-cors-headers python-dotenv
```
 - `djangorestframework` - for managing rest-api framework in django, and it automatically installs `django`.
 - `djoser` - for managing auth
 - `django-cors-headers` - for allowing cross-origin requests
 - `python-dotenv` - for `.env` support

## Create Requirements.txt
```
pip freeze > requirements.txt
```

## Settings
In  `settings.py`,
- import necessary package
    ```
    from django.core.management.utils import get_random_secret_key
    from os import getenv, path
    import dotenv
    ```
- load `.env` file
    ```
    # This is not going to run in production server
    env_file = BASE_DIR / '.env.local'
    if path.isfile(env_file):
        dotenv.load_dotenv(env_file)
    ```
- Update some settings
  ```
  # generates a random key if .env doesn't have the secret key (NOT RECOMMENDED)
  SECRET_KEY = getenv("DJANGO_SECRET_KEY", get_random_secret_key())
  ```
  ```
  DEBUG = getenv("DEBUG", "False") == "True"
  ```
  ```
  ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
  ```
  ```
  INSTALLED_APPS = [
    ...
    'rest_framework',
    'djoser',
  ]
  ```
  ```
  STATIC_URL = 'static/'
  STATIC_ROOT = BASE_DIR / 'static'
  MEDIA_URL = 'media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```  

- Rest Framework settings
  ```
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ],
      # requests are only allowed for authenticated users
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated'
      ]
  }
  ```
- Djoser settings
  ```
  # Full Docs: https://djoser.readthedocs.io/en/latest/settings.html
  DJOSER = {
      'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
      'SEND_ACTIVATION_EMAIL': True,
      'ACTIVATION_URL': 'activation/{uid}/{token}',
      'USER_CREATE_PASSWORD_RETYPE': True,
      'SET_PASSWORD_RETYPE': True,
      'PASSWORD_RESET_CONFIRM_RETYPE': True,
      'TOKEN_MODEL': None,
  }
  ```


# Resources
 - [Youtube Tutorial](https://www.youtube.com/watch?v=2pZmxh8Tf78)
 - [Blog](https://docs.digitalocean.com/tutorials/app-deploy-django-app/)
 - [Django Rest API](https://www.django-rest-framework.org/)
 - [Djoser Docs](https://djoser.readthedocs.io/en/latest/getting_started.html)
 - [JWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
 - [Django Docs](https://docs.djangoproject.com/en/)
