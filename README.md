# Project 5: Endless Explorer
Endless Explorer is an ecommerce website selling camping/survivalist gear. Users can browse a catalogue of products and make purchases. Users can make accounts, within which they can see their order history and other details.

This project is built with Django, CSS, HTML, Python, and Javascript. It uses a custom models and models adapted from the Boutique Ado examples. It has C.R.U.D. functionality, allowing users to create, read, update, and delete products. The majority of styling is done through Bootstrap, though there is a custom CSS for for more specific styling.

There are two types of users:

- A superuser that can create, delete, and edit products.
- A standard user that can browse the site and create orders.

**[Click here to visit the Endless Explorer website.](https://endless-explorer.herokuapp.com/)**

## Table of Contents

## Features

### Front Page
The front page has relevant descriptive text, to effectivly use SEO. It then has 4 products from each category for the user to browse through. Users can click on a category for more items, or click into an individual item for more details.

### Navigation Bar
The navigation bar allows users to browse products by category, search, login, logout, access their profile, and view the shopping cart. If they are a superuser, it also lets them open the "Add an Item" form. It sticks to the top of the top of the window when the user scrolls down the page.

### Messages
Messages are displayed below the navigation bar. Messages appear when the user makes any changes to their bag, logs in, logs out, completes the checkout, etc. The message div is dismissed after 3 seconds, using a small piece of JS code.

### Footer
The footer contains links to social media and other important information. Links have the rel="noopener" attribute.

### Browse by Category and Seach
Users are able to browse products by category, using links on the main page or on the navbar. This shows a subset of products. Users can also search for products by name.

### Product Cards
When browsing, products are displayed on cards. These cards contain the product image (if there is one - there is also a default "noimage" image), a brief product description, rating, category, price. They also contain a quick buy button, which will immediately add one copy of the product to the user cart. If the product has variants, which must be selected, the user will instead go to the product page when clicking this button.

### Products Variants
This uses a modified model. Each product can have up to 3 variants - ie, colours, sizes, etc. These are selected from a drop-down box on the product details page. The user can add multiple variants of the same product, which will be added as seperate line items, or multiple copies of the same variant, which will be the same line item.

### User Profile
The user profile displays information about the logged in user - primarily their address and order history.

#### User Address
The user can update their default address on their profile page. This will be reflected on the order form when they checkout.

#### User Order History
The user can see their order history and can click into each order for more details, similar to the order confirmation page.

### Bag
The user can see items in their bag, can adjust the quantities of said items, and delete items from their bag. Adjusting items is handled through some JS code.

### Checkout
In the checkout, the user gets a summary of their order and then must fill in an address form and card details. They can then confirm their order or return to the store.

### Order confirmation
Upon completing payment with Stripe, the user is brought to an order confirmation page, where order details are presented.

### Wishlist
This uses a custom model and allows a user to add products to their wishlist. All wishlist functionality has the @login_required deocrator, so if a user is not logged in, they will get a login prompt. If they are not logged in, wishlist buttons will also not display to the user. Upon navigating to their wishlist, users can view items, add them to their cart, click into them for more details, and remove items.

### AllAuth Pages
User login/logout are handled though AllAuth. These pages have had CSS styling applied to them.

### CRUD functionality
The Superuser has full CRUD functionality in respect to products in the store. They can add a new product by following a link in the navbar - this provides the same form as could be found in the admin panel. They can also edit and delete products, by clicking the links on the product page or the product card when browsing.

### Custom 404
There is a custom 404 page.

## Design
I have used a simple colour scheme, forcussing on greys and greens. This is to create a clean, more accessible and navigable site. The green in the buttons is to echo the idea of nature and adventure.

I used Bootstrap for most of this project, using guidance from Bootstrap's Getting Started Documentation.

In addition, I used my own custom CSS file, to create smaller and more specific styling effects.

### Responsive Design
The site is fully responsive. On a mobile device, the navigation menu turns into a button, product cards automatically reduce in size and evenutally stack.

### Wireframes
Wireframes were produced to help guide design.

#### Desktop Wireframe

![Screenshot of desktop wireframe](/assets/readme_images/wireframedesktop.png)

#### Mobile Wireframe

![Screenshot of mobile wireframe](/assets/readme_images/wireframemobile.png)

## Search Engine Optimisation
In order to populate the text on the site, I resarched google searches related to outdoor aventure, camping, hiking, etc. After compiling a list of recurring terms, I ensured that product text and page introductions used such terms. I tried to maintain a level of expertese, authoratativeness, and trustworthiness in order to satisfy Rater Guidelines.

Websites such as www.wordtracker.com were invaluable for this and helped specifically with choosing product names.

![Screenshot of Wordtracker](/assets/readme_images/wordtracker1.png)
![Screenshot of Wordtracker](/assets/readme_images/wordtracker2.png)

Using semantic elements such as nav, header, footer, and headers further assists with effective SEO.

On product pages, image alt fields always include product names.

Keyword meta tags have been included in the header of every page, ulilising terms found in my research.

My site includes an XML sitemap, created on https://www.xml-sitemaps.com/

My site includes a robots.txt file.

## Facebook Business Page Mockup

![Screenshot of Facebook Business Page](/assets/readme_images/EEFacebookMockup.jpg)

## Mailchimp Integration

The site includes a form for mailing list signup through mailchimp.

## Agile Development / User Stories
The site was developed using Agile Methodology (ie, MoSCoW prioritisation) to ensure that important elements were finished first and that they were approached in bite-size chunks. [User stories can be viewed here.](https://docs.google.com/spreadsheets/d/1kAf1gPciUevvqiVY8SZv4Ui5HvB0vWO3gLLJnIaMFmk/edit?usp=sharing)

![Screenshot of User Stories](/assets/readme_images/userstories.png)

## Accessibility
The site is largely text based, so works well with screen readers. The exception to this is the external links in the footer, which are given an aria-label, and product images, which are given an alt text.

The website uses high-contrast colours between background and text to maintain readability.

## Testing

### Manual Testing

| Function | Expected Outcome | Actual Outcome
| --- | --- | --- |
| **Any User** |  |  |
| User can open main page. | Display navbar, gallery of products, and footer. | As intended. |
| User can click through product cards. | Clicking through product cards shows product details. | As intended. |
| User can follow external links in footer. | External links direct to social media. | As intended. |
| User can register new account. | Clicking Register in header allows user to fill in form for a new account. | As intended. |
| Registration form is validated. | User must submit a username and a valid password. Email is optional. | As intended. |
| User recieves confirmation emails | Upon registering, confirmation email sent to the user. | As intended. |
| Every page is styled. | CSS styles working for every page, including AllAuth pages. | As intended. |
| Site functions on different browswers. | Site functions on Chrome, Firefox, and Edge. | As expected. |
| Site is responsive. | Site responds to smaller screen sizes and a variety of mobile screen sizes. | As expected. |
| User can add items to bag. | Click add to bag will add the product to the bag. Reflected on bag page. | As intended |
| User can change quantities | Click on plus/minus and update will change quantity in bag. | As intended. |
| User can select variants | Select different variants from the dropdown menu. | As intended. |
| User can make purchase | User can checkout with Stripe to pay for their order. | As intended. |
| User can see confirmation page | After finishing an order, user is presented with confirmation page. | As intended. |
| User received confirmation email | After finishing an order, user receves confirmation email. | As intended. |
| User receives pop-up messages. | For many actions, such as adding to bag, messages pop up. | As intended. |
| Messages auto-dismiss. | Messages dismiss themselves after 3 seconds. | As intended. |
| **Registered Users** |  |  |
| User can log in. | Clicking Log In allows user to sign into their account. | As intended. |
| **Logged In Users** |  |  |
| User can log out. | Clicking Log Out allows the user to sign out. | As intended. |
| User can check their profile. | Clicking profile will show the user profile. | As intended. |
| User can update default address. | Form on profile page updates user profile. | As intended. |
| User can save address when checking out. | Address can be updated from the checkout page. | As intended. |
| User can view order history. | Order history is visible on profile page. | As intended. |
| User can view individual order details. | User can click into their order to see details. | As intended. |
| **Superusers** |  |  |
| Superuser can create new product. | Form for new product adds product to the database. | As intended. |
| Superuser can edit product. | Clicking Edit allows the user to change product details. | As intended. |
| Superuser can delete product. | Clicking Delete allows the user to delete the product. | As intended. |
| Superuser can access CRUD tools | Each product card has edit/delete. Add is in the nav bar. | As intended. |

### Validator Testing

#### HTML validator

HTML Validation at https://validator.w3.org/nu/ produces some errors on the index regarding duplicate ids. I know why this is occuring and that it isn't a problem - these ids refer to quantity selector forms that are hidden from the user and cannot be adjusted by them. They only exist on the front page because that is the only place where product cards may be duplicated (they can be showcased as "On Sale" or in their default category). Subsequently, the duplicate id has no ill effect. Other than that, the site passes HTML validation. 

#### CSS validator

The site passes CSS Validation at https://jigsaw.w3.org/css-validator/.

![Screenshot of CSS Validator](/assets/readme_images/CSSvalidator.png)

#### Lighthouse

The site scores very well on Lighthouse for desktop and mobile. The slightly lower score on mobile devices is because the site used PNG images.

![Screenshot of Lighthouse Desktop](/assets/readme_images/lighthousedesktop.png)
![Screenshot of Lighthouse Mobile](/assets/readme_images/lighthousemobile.png)

#### Pep8

The Python code passes Pep8 validation.

## Project Setup
### Basics
- Use CI Template
- Open copy of template in gitpod
- Install Django:

    pip3 install Django==3.2

- Create project:

    django-admin startproject endless_explorer .

- Create gitignore file and add *.sqlite3 to this file:

    touch .gitignore

- Run server to make sure everything is going OK
- Run migrations.
- Create superuser:

    python3 manage.py createsuperuser

### AllAuth
- Install with:

    pip3 install django-allauth==0.41.0

- Add authentication backends and installed apps details, from AllAuth documentation (https://django-allauth.readthedocs.io/en/latest/installation.html)
- Create URLs in urls.py:

    path('accounts', include('allauth.urls')),

- Run migrations.
- Once done with settings, etc, freeze the requirements:

    pip3 freeze > requirements.txt

### AllAuth Templates
- These are copied so that we can modify templates with versions that take precidence. Any of these that you delete will revert those requests to default.

    cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/

### Create a home app
- Create app with:

    python3 manage.py startapp home

- Create templates directory: mkdir -p home/templates/home
- In this, create index.html and make it extend base and load static:

    {% extends "base.html" %}
    {% load static %}

- Create a view to render the template. Go to views.py
- Create a urls.py file in home app (using the file from the project directory as a template)
- Create a blank view:

    path('', views.index, name="home")

- And import views from the current directory: 

    from . import views

- Add the URLs to the project urls.py:

    path('', include('home.urls')),

- In settings.py, add "home" to installed apps.

### Install Bootsrap
- Bootstrap is installed when using the Bootstrap Starter in the base.html file.

### Create products app
- Create app:

    python3 manage.py startapp products

- Add to installed apps in settings.py
- Create model for the products in products/models.py
- Do a migrations dry run to identify potential issues.

    python3 manage.py makemigrations --dry-run

- Make migrations then migrate with plan flag to make sure there are no issues with models.

    python3 manage.py migrate --plan

- Migrate.
- Register product model in products/admin.py

    from .models import Product
    admin.site.register(Product)

## Project Deployment
### Deploying to Heroku
- Create new app, give it a name, and choose closest region.
- On Resources tab, create a Heroku Postgres add-on.

    pip3 install dj_database_url
    pip3 install psycopg2-binary

- Freeze requirements: 

    pip3 freeze > requirements.txt

- Add import dj_database_url to settings.py
- Comment out the default database configuration.
- Create a new database and pass it the DATABASE_URL from Heroku app/settings/Config Vars

    DATABASES = {
        'default': dj_database_url.parse()
    }

- Now need to run migrations again. Begin with "python3 manage.py showmigrations", then "python3 manage.py migrate".
- At this point, need to create database - importing it from a json if that was used.
- Create a new superuser with:

    python3 manage.py createsuperuser

- Revert database changes before commiting, so that Heroku database URL doesn't end up in version control.
- Install gunicorn and freeze into requirements file:

    pip3 install gunicorn

- Create a Procfile to tell Heroku to create a web dyno.

    web: gunicorn endless_explorer.wsgi:application

- Log in to heroku:

    heroku login -i

- Disable collect static:

    heroku config:set DISABLE_COLLECTSTATIC=1 --app endless-explorer

- Update allowed hosts in settings.py

    ALLOWED_HOSTS = ['endless-explorer.herokuapp.com', 'localhost']

- Commit and push, and then also push to heroku with:
    
    heroku git:remote -a endless-explorer
    git push heroku main

(if facing an error, downgrade Heroku version with: "heroku stack:set heroku-20 -a endless-explorer"
then create a runtime.txt file containing: python-3.8.14)

### Github
- Connect app to github through the deploy tab on Heroku. 
- Now enable automatic deploys so that github deploys also deploy to Heroku.

### Create a new Secret Key
- In settings/config vars, create SECRET_KEY
- In settings.py replace the existing secret key with:

    SECRET_KEY = os.environ.get('SECRET_KEY', '')

### Arrange Amazon S3 to host static files
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

### Configure Django to Access Amazon Services

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

### Configure Stripe

- Copy the Stripe API keys into the Heroku config vars.
- Create a new Endpoint for the Stripe webhook, pointing to https://endless-explorer.herokuapp.com/checkout/wh/
- Set the webhook to receive all events.
- Reveal the webhook's signing secret and add this to the Heroku config vars.

## Setting up Emails

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

## Invoke Linter

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

### Live Database
After deploying my site to Heroku, I made some more changes to models on my local version. After pushing these, I noticed that my deployed site had broken. Whenever I called a page which needed to use said models, it responded with a "ProgrammingError". I searched for answers for some time before contacting Tutor Support, where I learnt that I needed to additionally makemigrations and migrate within Heroky whenever I made changes to models. Running the following commands solved the issue:

    heroku run python3 manage.py makemigrations

    heroku run python3 manage.py migrate

### Strange Columns
On several pages, columns were displaying oddly, taking up half the page, rather than being full-width. Or not holding all of their contents. I was using the Bootstrap flex-grid to create them like this:

    <div class="container">
        <div class="row">
            <div class="column">
                <p>Column 1</p>
            </div>
            <div class="column">
                <p>Column 1</p>
            </div>
        </div>
    </div>

Upon checking the documentation, to find out why these were not displaying correctly, I realised I was using the incorrect class for each column. I should have been using the class "col". This change corrected displays across the site.

## Technologies Used

- Javascript
- Python
- CSS
- HTML
- Django
- AllAuth
- Heroku
- GitHub
- GitPod
- Firefox developer tools
- Chrome developer tools
- JSHint
- W3 HTML Validator
- W3 CSS Validator
- favicon.io
- Wordtracker
- XML-Sitemaps
- Relational database
- Stripe
- AWS

## Credits:
- Any code taken or adapted from other sources is mentioned in comments.
- Base template modified from Bootstrap starter template: https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template
- Navbar code modified from https://getbootstrap.com/docs/4.6/examples/navbar-fixed/
- Footer code modified from https://getbootstrap.com/docs/5.1/examples/footers/
- Product cards modified from https://getbootstrap.com/docs/4.6/components/card/#grid-cards
- Mailchimp signup form taken from https://www.mailchimp.com.
- Much of the project's Python code is modified from the Boutique Ado sample project. All cases of this have been commented in the code.
- Favicon modified from Freepic icon: https://www.flaticon.com/free-icons/adventure
- Placeholder image: https://www.flaticon.com/free-icons/picture
- Aluminium Teapot image: https://www.aliexpress.com/item/1005004112230217.html
- Camping Thermal image: https://www.aliexpress.com/item/1005004215204462.html
- Cutlery Set image: https://www.aliexpress.com/item/1005004112211074.html
- Foldable Cutlery image: https://www.aliexpress.com/item/1005004223338581.html
- Credit Card Multitool image: https://www.aliexpress.com/item/1005004106124768.html
- Water Purifier image: https://www.aliexpress.com/item/1005004112186122.html
- Carbiner image: https://www.aliexpress.com/item/1005004404157227.html
- Hunting Bag image: https://www.aliexpress.com/item/1005003050642045.html
- Camping Pillow image: https://www.aliexpress.com/item/1005004327692333.html
- Gas torch image: https://www.aliexpress.com/item/1005004710565250.html
- Parachute cord image: https://www.aliexpress.com/item/1005002239649577.html
- Camping stove image: https://www.aliexpress.com/item/1005004560109672.html
- Police brand torch image: https://www.aliexpress.com/item/1005003287493435.html
- Mini Lantern image: https://www.aliexpress.com/item/1005004593272493.html
- Portable torch image: https://www.aliexpress.com/item/1005004338584594.html
- Camping Lantern image: https://www.aliexpress.com/item/1005004607730450.html
- Compass image: https://www.aliexpress.com/item/4000017445414.html
- Walking stick image: https://www.aliexpress.com/item/1005004222181062.html
- Strawberries image: https://www.nutsinbulk.ie/product/freeze-strawberries-pieces
