
.PHONY: all
all:
	@echo "Nothing to be done for 'all'"

.PHONY: release
release: tests docs distr

.PHONY: distr
distr:
	./mk-distr

.PHONY: docs
docs:
	cd docs && exec ./rebuild

.PHONY: test
test:
	tox

.PHONY: tests
tests: test

.PHONY: clean
clean:
	find . -name '*.py[co]' -type f -delete
