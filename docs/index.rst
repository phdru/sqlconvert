.. mysql2sql documentation master file, created by
   sphinx-quickstart on Fri Jul 22 19:32:24 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mysql2sql's documentation!
=====================================

This is mysql2sql, a mysql to sql converter. It is primary intended to
convert mysqldump (especially with extended INSERT syntax) to standard
SQL to load at least to PostgreSQL or SQLite.

It uses `sqlparse <https://github.com/andialbrecht/sqlparse>`_ to parse
SQL.

The program is in its initial phase and currently cannot do much.

.. highlight:: none

Command line
------------

mysql-to-sql.py
~~~~~~~~~~~~~~~

Usage::

    mysql-to-sql.py [-i infile] [-o outfile]

Options::

    -i, --infile infile    Input file, stdin if absent
    -o, --outfile outfile  Output file, stdout if absent


Indices and tables
==================

* :ref:`genindex`
* `<api/modules.html>`_
* :ref:`search`


Credits
=======

Created by Oleg Broytman <phd@phdru.name>.

Copyright (C) 2016 PhiloSoft Design.


License
=======

GPL.
