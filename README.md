# Project 5: Endless Explorer
Endless Explorer is an ecommerce website selling camping gear. Users can browse a catalogue of products and make purchases. Users can also view a blog and leave comments/reviews on posts/products. Users can make accounts, within which they can see their order history and other details.

https://endless-explorer.herokuapp.com/

## Features

### Front Page

### Browse by Category

### Product Preview
This uses a modified model. In the product model, each product may have a product preview. This text appears while browsing through products. It is limited to 254 characters.

### Wishlist Items
This uses a custom model.

### User Profile
#### User Address
#### User Order History
#### User Wishlist

## Project Setup
### Basics
- Use CI Template
- Open copy of template in gitpod
- Install Django: "pip3 install Django==3.2"
- Create projecT: "django-admin startproject endless_explorer ." (the . creates in current directory)
- Create gitignore file: "touch .gitignore" (and add *.sqlite3 to this file)
- Run server to make sure everything is going OK
- Run migrations: "python3 manage.py migrate"
- Create superuser: "python3 manage.py createsuperuser"

### AllAuth
- install with: "pip3 install django-allauth==0.41.0"
- Add authentication backends and installed apps details, from AllAuth documentation (https://django-allauth.readthedocs.io/en/latest/installation.html)
- Create URLs in urls.py: path('accounts', include('allauth.urls')),
- Run migrations
- Once done with settings, etc, "pip3 freeze > requirements.txt"

### AllAuth Templates
- These are copied so that we can modify templates with versions that take precidence. Any of these that you delete will revert those requests to default.

    cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/

### Create a home app
- python3 manage.py startapp home
- create templates directory: mkdir -p home/templates/home
- in this, create index.html and make it extend base and load static:

    {% extends "base.html" %}
    {% load static %}

- create a view to render the template. Go to views.py
- create a urls.py file in home app (using the file from the project directory as a template)
- create a blank view: path('', views.index, name="home")
- and import views from the current directory: from . import views
- add the URLs to the project urls.py: path('', include('home.urls')),
- In settings.py, add "home" to installed apps.

### Install Bootsrap
- Bootstrap is installed when using the Bootstrap Starter in the base.html file.
- Base template modified from Bootstrap starter template: https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template

### Create products app
- python3 manage.py startapp products
- add to installed apps in settings.py
- create model for the products in products/models.py
- do a migrations dry run to identify potential issues.
- python3 manage.py makemigrations --dry-run
- make migrations then migrate with plan flag to make sure there are no issues with models
- python3 manage.py migrate --plan
- migrate.
- register product model in products/admin.py
- from .models import Product
- admin.site.register(Product)

### Deployment
#### Deploying to Heroku
- Create new app, give it a name, and choose closest region.
- On Resources tab, create a Heroku Postgres add-on.
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- Freeze requirements: pip3 freeze > requirements.txt
- Add import dj_database_url to settings.py
- Comment out the default database configuration.
- Create a new database and pass it the DATABASE_URL from Heroku app/settings/Config Vars

DATABASES = {
    'default': dj_database_url.parse()
}

- Now need to run migrations again. Begin with python3 manage.py showmigrations, then python3 manage.py migrate.
- At this point, need to create database - importing it from a json if that was used.
- Create a new superuser with python3 manage.py createsuperuser
- Revert database changes before commiting, so that Heroku database URL doesn't end up in version control.
- Install gunicorn and freeze into requirements file: pip3 install gunicorn
- Create a Procfile to tell Heroku to create a web dyno.

    web: gunicorn endless_explorer.wsgi:application

- Log in to heroku: heroku login -i
- Disable collect static: heroku config:set DISABLE_COLLECTSTATIC=1 --app endless-explorer
- Update allowed hosts in settings.py

    ALLOWED_HOSTS = ['endless-explorer.herokuapp.com', 'localhost']

- Commit and push, and then also push to heroku with:
    
    heroku git:remote -a endless-explorer
    git push heroku main

(if facing an error, downgrade Heroku version with: heroku stack:set heroku-20 -a endless-explorer
then create a runtime.txt file containing: python-3.8.14)

#### Github
- Connect app to github through the deploy tab on Heroku. 
- Now enable automatic deploys so that github deploys also deploy to Heroku.

#### Create a new Secret Key
- In settings/config vars, create SECRET_KEY
- In settings.py replace the existing secret key with: SECRET_KEY = os.environ.get('SECRET_KEY', '')

#### Arrange Amazon S3 to host static files
- Sign up for Amazon Web Services
- Create an S3 bucket
- Ensure bucket is public and ACLs enabled.
- Under the bucket properties, enable Static Website Hosting.
- Under the bucket permissions, paste in the following CORS configuration.

    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]

- In permissions/policies, use the policy generator.
    - Policy type is S3 bucket policy.
    - Allow all principals with *
    - Set action to 'GetObject'
    - Copy in ARN
    - Click 'add statement' and 'generate policy'.
    - Copy this policy into the bucket policy editor.
    - Add /* to the end of the resource key before saving.
- In the ACS (Access Control List), enable List for Everyone.
- Back in the services menu, open IAM. Go to 'User Groups' and 'Create Group'.
- Give the group a name and click, 'Create Group'.
- Go to 'Policies' and 'Create Policy'.
- Select the JSON tab and click 'Import Managed Policy'. Import the S3 Full Access policy.
- Update the policy with the S3 ARN, like this:

    "Resource": [
        "arn:aws:s3:::endless-explorer",
        "arn:aws:s3:::endless-explorer/*"
    ]

- Click through 'Tags' and 'Review'. Give the policy a name and a description and click 'Create Policy'.
- Head back to the group, 'Permissions', 'Add Permissions', 'Attach Policies'. Select and attach the correct policy.
- Create a user to add to the group on the 'Users' page. Click, 'Add User'.
- Give the user a name and grant them programatic access.
- Add the user to the correct group and click through 'Tags', 'Review', and 'Create User'.
- Download the CSV file, which contains the User's access keys.

#### Configure Django to Access Amazon Services

- Install boto3 and django-storages:

    pip3 install boto3
    pip3 install django-storages

- And then freeze the requirements file so these are installed on Heroku.

    pip3 freeze > requirements.txt

- Add Storages to installed apps. And add the following settings to settings.py:

    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'endless-explorer'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

- Add the ACCESS_KEY and SECRET_ACCESS_KEY config vars to Heroku. (they come from the downloaded CSV file)
- Also add USE_AWS, set to 'True', and remove the DISABLE_COLLECTSTATIC variable.
- Create a file in the base directory called custom_storages.py - and fill this in to tell Django to send static files to S3.
- Update the settings file to indicate these instructions:

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

#### Configure Stripe

- Copy the Stripe API keys into the Heroku config vars.
- Create a new Endpoint for the Stripe webhook, pointing to https://endless-explorer.herokuapp.com/checkout/wh/
- Set the webhook to receive all events.
- Reveal the webhook's signing secret and add this to the Heroku config vars.

### Setting up Emails

- Go to gmail settings, and seach for App Passwords.
- Select "mail" and for the app, select "other" and type in a name for the app.
- This grants a password that can be used as a config var in Heroku:

    EMAIL_HOST_PASS as the password
    EMAIL_HOST_USER as the gmail account

- In settings.py, delete the EMAIL_BACKEND variable, the existing DEFAULT_FROM_EMAIL and paste in the following:

    if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'endlessexplorer@example.com'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

### Invoke Linter

To check for issues across the entire project:

python3 -m flake8

## Bugs
### Views Error
In my index view, I had made the error where I was rendering a tuple rather than calling a function:

    return(render, 'home/index.html')

Luckily, this error was caught very early in the project. Changing the line to call the render function solved the error.

    return render(request, 'home/index.html')

### Sorting Error
When sorting by price, the products view does not consider that some products may be on sale. In order to fix this, I changed the product model so that "price" always represents the current price. Historical prices are then stored as "old_price", so that the original price can be referred to the on the site. If a product has an old_price, then it will be displayed as if it is on sale.

## Credits:
- Base template modified from Bootstrap starter template: https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template
- Much of the project is modified from the Boutique Ado sample project.
- Placeholder image: https://www.flaticon.com/free-icons/picture
- Aluminium Teapot image: https://www.aliexpress.com/item/1005004112230217.html
- Camping Thermal image: https://www.aliexpress.com/item/1005004215204462.html
- Cutlery Set image: https://www.aliexpress.com/item/1005004112211074.html
- Foldable Cutlery image: https://www.aliexpress.com/item/1005004223338581.html
- Credit Card Multitool image: https://www.aliexpress.com/item/1005004106124768.html
- Water Purifier image: https://www.aliexpress.com/item/1005004112186122.html
- Carbiner image: https://www.aliexpress.com/item/1005004404157227.html
- Hunting Bag image: https://www.aliexpress.com/item/1005003050642045.html
