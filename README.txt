Broytman SQL converter, Copyright (C) 2016-2017 PhiloSoft Design.
Author: Oleg Broytman <phd@phdru.name>.
License: GPL.

sqlconvert is a library to perform SQL conversions. It uses sqlparse to
parse SQL and SQLObject to escape SQL strings and handle connections to DB
backends.

The library is in the early stage of development and currently cannot do
much.

The first goal is to implement mysql2sql, a script intended primarily to
convert mysqldump output (especially with extended INSERT syntax) to
standard SQL to load at least to PostgreSQL or SQLite.
