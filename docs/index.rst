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

    mysql-to-sql.py [-e encoding] [-E output_encoding] [infile] [[-o] outfile]

Options::

   -e ENCODING, --encoding ENCODING
                           input/output encoding, default is utf-8
   -E OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                           separate output encoding, default is the same as
                           `-e` except for console; for console output charset
                           from the current locale is used
    infile                 Input file, stdin if absent or '-'
    -o, --outfile outfile  Output file, stdout if absent or '-'

Option `-o` is useful when infile is absent (input is redirected), for
example::

    mysql-to-sql.py -o outfile.sql < infile.sql
    cat infile.sql | mysql-to-sql.py -o outfile.sql

But of course it simply can be::

    mysql-to-sql.py - outfile.sql < infile.sql
    cat infile.sql | mysql-to-sql.py - outfile.sql


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
