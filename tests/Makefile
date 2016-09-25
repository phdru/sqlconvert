
.PHONY: all
all: nodb postgres sqlite clean

.PHONY: nodb
nodb:
	PYTHONPATH=.. python -m  pytest

.PHONY: postgres
postgres:
	createdb test
	PYTHONPATH=.. python -m  pytest -D postgres:///test
	dropdb test

.PHONY: sqlite
sqlite:
	PYTHONPATH=.. python -m  pytest -D sqlite:///tmp/test.sqdb
	rm -f /tmp/test.sqdb

.PHONY: clean
clean:
	rm -f *.tmp
