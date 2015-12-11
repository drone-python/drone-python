.. _writing_a_plugin:

.. include:: global.txt

How to write a Drone plugin
===========================

As the `Drone plugin documentation`_ says, all Drone plugins are ran in
Docker containers. A JSON string is passed in as the container's arguments,
and Drone assumes that that container will do something interesting with it.

Making things even more interesting, the Drone build root is mounted at
``/drone`` within the plugin container. This means that you can interact with
the files created during your initial *build* step.

By chaining plugins, we can achieve all sorts of neat things during our
Drone builds. Best of all, writing plugins is easy and relatively pain-less!

Start with our template
-----------------------

Assuming that you have already installed drone-python, get started by
using the :command:`create-drone-py-plugin` command. Pass in your desired
plugin name as the argument. We recommend all lowercase letters with dashes
used for separators. For example::

    $ create-drone-py-plugin my-plugin

Running this will fetch the latest Python Drone plugin template from GitHub,
then fill in some variables based on your responses to some questions. The
end result is a fully-functioning example plugin with much of the
foundation work already done.

Write your logic
----------------

Open up the ``plugin/main.py`` and take a look at the example provided (a
very crude webhook). You'll want to replace this module with your own logic,
but it serves as a helpful starting point.

The most important variable to notice is ``payload``. This is a parsed
JSON dict containing a mixture of values from the Drone build and the
``.drone.yml`` file.

Notice that the payload's ``vargs`` key contains the key/value pairs passed in
via ``.drone.yml``. These allow your user to provide input or configure your
plugin. You'll want to make sure to document these in ``DOCS.md`` (more
on that later).

Other interesting keys include ``repo`` (repo info for the build),
``system`` (mostly about your Drone install), and ``build`` (details on the
build itself).

As you work on your logic, make sure to add any dependencies to
``requirements.txt`` to make sure that the Docker image ends up with
everything it needs to run your plugin.

Testing as you go
-----------------

See the ``README.rst`` for examples on how to run the script. You can either
run it directly or build a Docker image and run a container.

If you want to run the script directly, you'll need to install the necessary
requirements (in ``requirements.txt``).

Pre-release checklist
---------------------

* Thoroughly edit your ``DOCS.md`` file to include information on what the
  plugin is for, the possible inputs, the behaviors, and anything else that
  may be helpful for your users. This document is used in the Drone
  add-on marketplace (if you are going to publish it there).
* Spend some time picking out the higher level details and replicating them
  to ``README.rst``.
* Make sure your ``requirements.txt`` contains everything necessary to
  run your plugin. Pin to specific package versions where possible.
* If you will be submitting your plugin for inclusion into the Drone
  add-on marketplace, replace ``logo.svg`` with your own.

Publishing
----------

Once you are ready to make your plugin available to Drone, you'll need
to publish the image somewhere. If you are working on a public image,
create a `Docker Hub`_ repository and build/push there.

If you are pushing to a private repository, the process is much the same.
You'll need to provide credentials to pull the image in your ``.drone.yml``.

In either case, your plugin sections in ``.drone.yml`` will need to use the
``image:`` key to point at your published Docker image. You'll want to
tag your images as well.

Troubleshooting and error tracking
----------------------------------

If you want to be able to track unexpected errors with your plugin, it may
be worth integration Sentry_. This can make diagnosing issues in production
much easier, since a full stacktrace and each frames' ``locals()`` will
be included.

Getting help
------------

See :doc:`support` if you get stuck while working on your plugin.

.. _Docker Hub: https://hub.docker.com/
.. _Sentry: https://getsentry.com
