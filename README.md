# Project 5: Endless Explorer
Endless Explorer is an ecommerce website selling camping gear. Users can browse a catalogue of products and make purchases. Users can also view a blog and leave comments/reviews on posts/products. Users can make accounts, within which they can see their order history and other details.

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
- Aluminium Teapot image: https://www.aliexpress.com/item/1005004112230217.html
- Camping Thermal image: https://www.aliexpress.com/item/1005004215204462.html
- Cutlery Set image: https://www.aliexpress.com/item/1005004112211074.html
- Foldable Cutlery image: https://www.aliexpress.com/item/1005004223338581.html
- Credit Card Multitool image: https://www.aliexpress.com/item/1005004106124768.html
- Water Purifier image: https://www.aliexpress.com/item/1005004112186122.html
- Carbiner image: https://www.aliexpress.com/item/1005004404157227.html
- Hunting Bag image: https://www.aliexpress.com/item/1005003050642045.html

# Things from CI Readme
## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
