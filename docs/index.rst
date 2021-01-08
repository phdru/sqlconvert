.. sqlconvert documentation master file, created by
   sphinx-quickstart on Fri Jul 22 19:32:24 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sqlconvert's documentation
==========================

sqlconvert is a library to implement SQL converters. It uses `sqlparse
<https://github.com/andialbrecht/sqlparse>`_ to parse SQL and `SQLObject
<http://sqlobject.org/>`_ to escape SQL strings and handle connections to
DB backends.

The library is in the early stage of development and currently cannot do
much.

The library is accompanied with `mysql2sql <mysql2sql.html>`_, a script
intended primarily to convert mysqldump (especially with extended INSERT
syntax) to standard SQL to load at least to PostgreSQL or SQLite.

Contents:

.. toctree::
   :maxdepth: 1

   install
   mysql2sql
   news


Indices and tables
==================

* :ref:`genindex`
* `<api/modules.html>`_
* :ref:`search`


Credits
=======

Created by Oleg Broytman <phd@phdru.name>.

Copyright (C) 2016-2021 PhiloSoft Design.


License
=======

GPL.
