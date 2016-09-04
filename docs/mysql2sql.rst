mysql2sql
=========

This is mysql2sql, a mysql to sql converter. It is primary intended to
convert mysqldump (especially with extended INSERT syntax) to standard
SQL to load at least to PostgreSQL or SQLite.

The program is in its initial phase and currently cannot do much. It only
removes /\*! directives \*/ and passes everything else unmodified.


.. highlight:: none

Command line
------------

mysql2sql
~~~~~~~~~

Usage::

    mysql2sql [-e encoding] [-E output_encoding] [infile] [[-o] outfile]

Options::

    -e ENCODING, --encoding ENCODING
                           input/output encoding, default is utf-8
    -E OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                           separate output encoding, default is the same as
                           `-e` except for console; for console output charset
                           from the current locale is used
    -P, --no-pbar          Inhibit progress bar
    infile                 Input file, stdin if absent or '-'
    -o, --outfile outfile  Output file, stdout if absent or '-'

If stderr is connected to the console the program displays a text mode progress
bar. Option `-P/--no-pbar` inhibits it.

Option `-o` is useful when infile is absent (input is redirected), for
example::

    mysql2sql -o outfile.sql < infile.sql
    cat infile.sql | mysql2sql -o outfile.sql

But of course it simply can be::

    mysql2sql - outfile.sql < infile.sql
    cat infile.sql | mysql2sql - outfile.sql
