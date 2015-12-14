.. _installation:

.. include:: global.txt

Installation
============

This document covers the installation of drone-python. You'll want to do
this in your development environment, as well as in your plugins'
``Dockerfile`` (if you are writing a plugin).

Distribute & Pip
----------------

Installing drone-python is simple with pip_, just run this in your terminal::

    $ pip install drone

.. _pip: https://pip.pypa.io/

GitHub
------

drone-python is developed on `GitHub <GitHub project_>`_, where you can
always retrieve the latest version of the code.

You can either clone the public repository::

    $ git clone git://github.com/drone/drone.git

Download the tarball::

    $ curl -OL https://github.com/drone/drone/tarball/master

Or, download the zipball::

    $ curl -OL https://github.com/drone/drone/zipball/master

Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install

