#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlparse import parse
from sqlconvert.print_tokens import print_tokens
from sqlconvert.process_mysql import process_statement
from sqlconvert.process_tokens import find_error


def main(filename):
    with open(filename) as infile:
        for query in infile:
            for parsed in parse(query):
                print("----------")
                if find_error(parsed):
                    print("ERRORS IN QUERY")
                process_statement(parsed)
                print_tokens(parsed)
                print()
                parsed._pprint_tree()
    print("----------")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
