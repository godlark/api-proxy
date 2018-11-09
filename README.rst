proxy-api
=========

The proxy for every API

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Development and Testing
------------------------

* Install docker and docker-compose
* Run:
    $ docker-compose up
* Run migrations:
    $ python manage.py migrate
* Create a superuser account:
    $ docker-compose run django sh
    $ python manage.py createsuperuser
* Setup proxies and callbacks:
    * go to localhost:8000/admin
    * login
    * play

A little more help:

If you setup proxy http://google.pl with `google` slug, in order to receive
response via proxy, you have to go to http://0.0.0.0:8000/google/~~params~~
Proxies are available only for logged users.

If you setup callback endpoint http://192.168.1.25:80 with slug `intranet`
slug, in order to receive callbacks, you have to pass an address
http://public-address-to-you-proxy:8000/callbacks/forward/intranet/~~params~~
If you want to replay callbacks requests, check `id` of your favourite
callback request, than call http://0.0.0.0:8000/callbacks/replay/`id`


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy proxy_api

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



