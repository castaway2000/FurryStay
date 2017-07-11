# OpenStay Example
 Furrystay uses OpenStay an OpenSource platform written by me and in conjunction with the hackathon starter kit.
 OpenStay partially uses the hackathon boilerplate
 https://github.com/DrkSephy/django-hackathon-starter


## Table of Contents

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Features

* User Registration
* Host registration
* Search engine with filters
* Inteligent Profiles
* Internal Direct Messaging System
* User Review system
* User Settings
* dashboard with upcoming info
* front page with notification system

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



### Hackathon contribution


| Name                               | Description                                                 |
| ---------------------------------- |:-----------------------------------------------------------:|
| **hackathon_starter**/settings.py | Django settings module containing database and API keys/tokens|
| **hackathon/static/**             | Front-end JavaScript / CSS files|
