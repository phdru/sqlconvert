
.PHONY: all
all: nodb postgres clean

.PHONY: nodb
nodb:
	PYTHONPATH=.. python -m  pytest

.PHONY: postgres
postgres:
	createdb test
	PYTHONPATH=.. python -m  pytest -D postgres:///test
	dropdb test

.PHONY: clean
clean:
	rm -f *.tmp
