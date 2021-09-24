News
====

Version 0.3.0 (2021-09-24)
--------------------------

* Python 3.8, Python 3.9.

* GitHub Actions.

* Stop testing at Travis CI.

* Stop testing at AppVeyor.

Version 0.2.3 (2019-02-01)
--------------------------

* Python 3.7.

* Use remove-old-files.py from ppu to cleanup pip cache
  at Travis and AppVeyor.

* Install psycopg2 from `psycopg2-binary`_ package.

.. _`psycopg2-binary`: https://pypi.org/project/psycopg2-binary/

Version 0.2.2 (2017-06-10)
--------------------------

* Use tox instead of tests/Makefile.

* Test at Travis and AppVeyor with Postgres.

Version 0.2.1 (2017-05-01)
--------------------------

* Convert README to reST.

Version 0.2.0 (2017-04-30)
--------------------------

* Python 3.5, 3.6.

* Test at Travis and AppVeyor.

* Use Portable Python Utilities.

Version 0.1.2 (2017-04-27)
--------------------------

* Fix dependencies.

Version 0.1.1 (2017-04-26)
--------------------------

* Install m_lib.defenc and m_lib from PyPI.

Version 0.1.0 (2017-03-19)
--------------------------

* Split extended INSERTs (mysql2sql script).

* Extend tests.

Version 0.0.8 (2017-03-18)
--------------------------

* Split extended INSERTs (library and tests, scripts will be extended later).

* Extend tests, increase test coverage.

Version 0.0.7 (2016-09-27)
--------------------------

* Change quoting style to MySQL, PostgreSQL or SQLite.

* Add a test for print_tokens().

Version 0.0.6 (2016-09-25)
--------------------------

* Condense a sequence of newlines after a /\*! directive \*/;

* Rename remove_directives -> remove_directive_tokens.

* Unescape strings. Add a test for Postgres.

* Use SQLObject for string quoting and connection handling for tests.

* Use pytest, coverage and tox for testing.

* Add tests for Postgres and SQLite.

Version 0.0.5 (2016-09-07)
--------------------------

* Remove /\*! directives \*/; and newlines after them.

* Join group-{file,sql}.py into demo-group.py
* parse-{file,sql}.py into demo-parse.py.

* Add demo-process.py.

* Fix: flush buffer and outfile.

Version 0.0.4 (2016-09-04)
--------------------------

* Add MySQL-specific remove_directives() and process_statement().

Version 0.0.3 (2016-09-04)
--------------------------

* Rename the project: mysql2py -> sqlconvert.

Version 0.0.2 (2016-09-04)
--------------------------

* Rename mysql-to-sql.py -> mysql2py.

* Display progress bar.

Version 0.0.1 (2016-09-03)
--------------------------

* First release. Setup, tests and docs infrastructure.
