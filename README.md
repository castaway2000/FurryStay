# OpenStay
 OpenStay uses the hackathon boilerplate
 https://github.com/DrkSephy/django-hackathon-starter


## Table of Contents

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Obtaining API Keys](#getting-api-keys)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

* User Registration
* Sphinx Documentation
* Django Nosetests
* Integration with Django Rest Framework
* Basic Authentication with username and password
* **OAuth 2.0 Authentication**
    * Facebook
    * Google+
* **OAuth 1.0a Authentication** 
    * Twitter
* **API Examples**
    * Twitter API
    * Facebook API
    * Google+ API

## Pre-requisites

This project relies on `bower` for front-end dependencies, which in turn requires [npm](https://www.npmjs.com/). `npm` is now bundled with `NodeJS`, which you can download and install [here](https://nodejs.org/download/).

For Python-specific libraries, this project relies on [pip](https://pypi.python.org/pypi/pip). The easiest way to install `pip` can be [found here](https://pip.pypa.io/en/latest/installing.html).

## Getting Started

To get up and running, simply do the following:

    $ git clone https://github.com/castaway2000/OpenStay.git
    $ cd django-hackathon-starter

    # Install the requirements
    $ pip install -r requirements.txt

    # Install bower
    $ npm install -g bower
    $ bower install

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    $ manage.py runserver localhost:8080

**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).

<hr>

### Getting API Keys



<img src="https://g.twimg.com/Twitter_logo_blue.png" width="100">

1. Register an account on [Twitter.com](http://www.twitter.com/)
2. Visit [Twitter application management page](https://apps.twitter.com/)
3. Click on **Create New App**
    * Enter `Application name`, `Description`, and `Website` field
    * For `Callback URL` field, enter: `http://127.0.0.1:8000/hackathon/`
4. Click **Create your Twitter application**
5. Go to the **Permissions** tab
6. Under *Access*, select **Read and Write** type
7. Go to **Keys and Access Tokens** tab
8. Under *Your Access Token*, click on **Create my access token** to generate access tokens
9. Within `settings.py`, add the following:
    * `TWITTER_CONSUMER_KEY` = `Twitter-consumer-key`
    * `TWITTER_CONSUMER_SECRET` = `Twitter-consumer-secret`
    * `TWITTER_ACCESS_TOKEN` = `Twitter-access-token`
    * `TWITTER_ACCESS_TOKEN_SECRET` = `Twitter-access-token-secret`


<hr>

<img src="http://www.freelargeimages.com/wp-content/uploads/2014/11/Facebook_logo-6.jpg" width="200">

1. Register an account on [Facebook.com](http://www.facebook.com.com/)
2. Visit [Facebook Developers page](https://developers.facebook.com/)
3. After logging in, Click on **My Apps** and then on **Add a New App**
    * Choose W**ebsite** as the platform and add the **name** for your project
    * Give your app a name.
    * Choose the category your app falls into.
    * Click **Create App ID**
    * Skip the quickstart process and you will be redirected to the app dashboard.
4. Copy the **app ID** and the **app secret**.
5. From the left menu choose the **Settings** option.
6. Click on **Add Platform** and choose **Website** once again.
7. Under **site URL**, specift the URL to be redirected after authentication is complete.
8. Click save.
9. In ```settings.py``` change the following values:
    * ```FACEBOOK_APP_ID = your_app_id```
    * ```FACEBOOK_APP_SECRET = your_app_secret```


<hr>

<img src="http://icons.iconarchive.com/icons/marcus-roberto/google-play/512/Google-plus-icon.png" width="200" />

1. Register an account on [Google.com](https://accounts.google.com/signup).
2. Navigate to [Google Developer Console](https://console.developers.google.com/project).
3. Click on **Create Project**, give your app a name and click **Create** (this might take a few sceonds).
4. You will be redirected to the project dashboard. From the left menu choose **APIs & auth** and then choose **APIs**.
5. Choose the API you would like to use (the built in example uses **Google+ API**).
6. Click on **Enable API**.
7. From the side menu, under **APIs & auth** select **consent screen**.
    * Fill your app name under **Product Name**.
    * Hit **save** button on the bottom.
8. From the side menu, under **APIs & auth** select credentials:
    * Click on **Create new Client ID**.
    * Under **Authorized JavaScript origins** specify you app base address (e.g ```http://localhost:8000```).
    * Under **Authorized redirect URIs** specify the URL to be redirected after authentication is complete.
    * Hit **Create Client ID** button (this might also take a few seconds).
9. Copy your new generated ```client_id``` and ```client_secret```:
10. Under ```settings.py``` change the following values:
    * ```GOOGLE_PLUS_APP_ID = your_client_id```
    * ```GOOGLE_PLUS_APP_SECRET = your_client_secret```

<hr>



### Project Structure


| Name                               | Description                                                 |
| ---------------------------------- |:-----------------------------------------------------------:|
| **hackathon_starter**/settings.py | Django settings module containing database and API keys/tokens|
| **hackathon**/admin.py            | Registered models for Django's admin page|
| **hackathon**/models.py           | Django models and profiles for user login|
| **hackathon**/tests.py            | Integration tests|
| **hackathon**/urls.py             | Django Hackathon Starter URL dispatcher|
| **hackathon**/views.py            | Django views file|
| **hackathon**/serializers.py      | Allows JSON representation for Django Model fields|
| **hackathon**/forms.py            | Basic form fields|
| **hackathon/static/**             | Front-end JavaScript / CSS files|
| **hackathon/unittests**           | Unit tests|
| **hackathon/scripts/**            | API Example scripts|
| **hackathon/scripts/**facebook.py | Script for interacting with Facebook API |
| **hackathon/scripts/**googlePlus.py | Script for interacting with Google+ API |
| **hackathon/scripts/**twitter.py                    | Script for interacting with Twitter API |
| **hackathon/templates/**hackathon/                  | Templates for API examples |
| **hackathon/templates/**hackathon/base.html         | Base template, contains navbar |

## Contributing


We welcome contributions of all kinds. If you would like to know what work is needed to be done, check the [issue tracker](https://github.com/castaway2000/open_stay/issues). Before sending a pull request, please open an issue. This project follows the [pep-0008](https://www.python.org/dev/peps/pep-0008/) style guide.


### LICENSE

**Where applicable to hackathon code contribution the MIT license is applied otherwise OpenStay is housed under the Mozilla Public License Version 2.0**

The MIT License (MIT)
Copyright (c) 2015 David Leonard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
