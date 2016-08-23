#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlparse import parse
from mysql2sql.print_tokens import print_tokens
from mysql2sql.process_tokens import requote_names, find_error, \
    StatementGrouper


def main(filename):
    grouper = StatementGrouper()
    with open(filename) as infile:
        for line in infile:
            grouper.process(parse(line)[0])
            if grouper.statements:
                for statement in grouper.get_statements():
                    print("----------")
                    if find_error(statement):
                        print("ERRORS IN QUERY")
                    requote_names(statement)
                    print_tokens(statement)
                    print()
                    statement._pprint_tree()
                print("----------")
    tokens = grouper.close()
    for token in tokens:
        print_tokens(token)
        print(repr(token))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
