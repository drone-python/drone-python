.. _faq:

.. include:: global.txt

Frequently Asked Questions
==========================

This document attempts to answer some of the questions we field most
frequently.

Why use drone-python over the more common drone-go?
---------------------------------------------------

Since Drone plugins are language-agnostic, the selection of language for
plugin authoring is largely prefernce-based. Common reasons for using
drone-python over the more commonly used drone-go include:

* Teams that have a wealth of Python experience and less familiarity with
  Go may prefer to stick with what they know.
* Some developers subjectively prefer Python over Go for this sort of work.
* Your plugins will have access to the rich and mature ecosystem of
  existing Python packages.

What Python versions do you support?
------------------------------------

Python 2.7.x and >= 3.2. While you may be able to use drone-python on
earlier versions, we don't officially support them.
