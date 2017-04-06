.. Rocket Python documentation master file, created by
   sphinx-quickstart on Thu Jan 19 18:32:35 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

Rocket Python is a Python 2 and 3 library to access the `REST API <https://rocket.chat/docs/developer-guides/rest-api/>`__ in RocketChat instances.  The goal
is to implement the entire REST API provided by `RocketChat <https://rocket.chat>`__.

Installation
------------

First step is to install via pip::

   pip install rocket-python

You'll need to create an instance of the Rocket API by logging in::

   from rocketchat.api import RocketChatAPI

    api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
    'domain': 'https://myrockethchatdomain.com'})


Main API Documentation
----------------------

.. toctree::
   :maxdepth: 1

   rocketchat

Detailed Module Docs
--------------------


.. toctree::
   :maxdepth: 1


   rocketchat.calls.auth
   rocketchat.calls.channels
   rocketchat.calls.groups
   rocketchat.calls.chat
   rocketchat.calls
   license
