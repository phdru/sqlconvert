Broytman mysql to sql converter, Copyright (C) 2016 PhiloSoft Design
Author: Oleg Broytman <phd@phdru.name>
License: GPL

This is mysql2sql, a mysql to sql converter. Intended primarily to
convert mysqldump (especially with extended INSERT syntax) to standard
SQL to load at least to PostgreSQL or SQLite.

Uses sqlparse to parse SQL.

The program is in its initial phase and currently cannot do much.
