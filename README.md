# Funakoshi club
## About

## Table of Contents
  - [How to use](#how-to-use)
  - [Project idea](#project-idea)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Acknowledgement](#acknowledgement)
## How to use

## Project idea

## Features

### Existing Features

## Technologies Used
 - For the account registration used Django-allauth library
 - For the feature images and CSS support used the Cloudinary library
 - For the comments used Crispy forms library
 - For the login/logout templates used default account templates from Allauth library

## Testing

 ### Validator Testing

## Deployment

  - ### Create the Heroku app
    On the Heroku, dashboard click on the "Create new app" button then give the app a name, choose a region and click on the "Create app" button.

  - ### Attach the PostgreSQL database
    On the Heroku, menu clicks on the "Resources" tab then in "Add-ons" search for "Postgres" to add Heroku Postgres to the project.

  - ### Prepare our environment and [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) files
    In the project's [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) add the app name in "INSTALET_APP".
    Create the [env.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/env_sample.py) file to store the URL from DATABASE, CLAUDINARY and SECRET_KEY then add them in the Heroku "Config Vars".

  - ### Get our static and media files stored on Cloudinary
    In the project's [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) by adding followings lines (STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage') we telling Django to store my static and media files in Cloudinare.

 - ### Deployment to Heroku
    Add Heroku's app name followed by herokuapp.com to ALLOWED_HOST from [setings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py).
    Add a file named "Procfile" for Heroku to know how to run my project.
    In the Heroku, dashboard click on the "Deploy" tab then click on GitHub to connect GitHub account after that searching for a repo to connect it to the Heroku.


### Cloning

## Acknowledgement

