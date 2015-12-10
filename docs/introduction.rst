.. _introduction:

.. include:: global.txt

Introduction
============

The Drone plugin system
-----------------------

One of Drone's most interesting features is its
`plugin system <Drone plugin documentation_>`_. Unlike most CI systems that
force you to write plugins in a certain language using a plugin API, Drone's
"plugin API" is the Docker container.

Our plugin containers can mount the build root as a volume, and variables
are passed by piping JSON strings as arguments to the ``docker run``
statements. As a consequence, Drone neither knows or cares what language
each plugin is written in.

Purpose
-------

While the official Drone plugins tend to mostly be written in Go_, some
teams have existing Python experience or substantial amounts of software
that is already written in Python. drone-python aims to be everything
needed to write plugins in Python.

Additionally, drone-python will eventually provide an HTTP API client for
the Drone HTTP API.

MIT License
-----------

The `MIT License`_ was selected for its permissiveness. We aim to maximize
the usability of the software.

drone-python License
--------------------

The MIT License (MIT)

Copyright (c) 2015 drone.io
Copyright (c) 2015 Gregory Taylor

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

