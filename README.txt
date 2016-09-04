Broytman SQL converter, Copyright (C) 2016 PhiloSoft Design
Author: Oleg Broytman <phd@phdru.name>
License: GPL

This is sqlconvert, a a library to perform SQL convertions. It uses
sqlparse to parse SQL.

The library is in its initial phase and currently cannot do much.

The first goal is to implemet mysq2sql, a script intended primarily to
convert mysqldump output (especially with extended INSERT syntax) to
standard SQL to load at least to PostgreSQL or SQLite.
