mysql2sql
=========

This is mysql2sql, a mysql to sql converter. It is primary intended to
convert mysqldump (especially with extended INSERT syntax) to standard SQL
to load at least to PostgreSQL or SQLite.

The program removes /\*! directives \*/, unquotes names quoted with
backticks, quote non-lowercase names with double quotes, unescapes strings
and escapes them to a different quoting style, and splits extended INSERTs
into a series of plain INSERTs separated by newlines. Everything else is
passed unmodified.


.. highlight:: none

Command line
------------

mysql2sql
~~~~~~~~~

Usage::

    mysql2sql [-e encoding] [-E output_encoding] [-m/-p/-s] [infile] [[-o] outfile]

Options::

    -e ENCODING, --encoding ENCODING
                           input/output encoding, default is utf-8
    -E OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                           separate output encoding, default is the same as
                           `-e` except for console; for console output charset
                           from the current locale is used
    -m, --mysql            MySQL/MariaDB quoting style
    -p, --pg, --postgres   PostgreSQL quoting style
    -s, --sqlite           Generic SQL/SQLite quoting style (default)
    -P, --no-pbar          Inhibit progress bar
    infile                 Input file, stdin if absent or '-'
    -o, --outfile outfile  Output file, stdout if absent or '-'

Options `-m/-p/-s` change quoting style. `-m` sets MySQL quoting style;
it's added to use the program in the following scenario: convert MySQL
dumps with extended INSERTs to SQL with plain INSERTS suitable to be fed
back to MySQL. `-p` sets PostgreSQL quoting style; it's like MySQL with
additional `E''-style quoting
<https://www.postgresql.org/docs/9.1/static/sql-syntax-lexical.html#SQL-SYNTAX-STRINGS-ESCAPE>`_.
`-s` sets generic SQL/SQLite quoting style; this is the default.

If stderr is connected to the console the program displays a text mode
progress bar. Option `-P/--no-pbar` inhibits it.

Option `-o` is useful when infile is absent (input is redirected), for
example::

    mysql2sql -o outfile.sql < infile.sql
    cat infile.sql | mysql2sql -o outfile.sql

But of course it simply can be::

    mysql2sql - outfile.sql < infile.sql
    cat infile.sql | mysql2sql - outfile.sql
