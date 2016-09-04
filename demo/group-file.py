#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlconvert.print_tokens import print_tokens
from sqlconvert.process_mysql import process_statement
from sqlconvert.process_tokens import find_error, StatementGrouper


def main(filename):
    grouper = StatementGrouper()
    with open(filename) as infile:
        for line in infile:
            grouper.process_line(line)
            if grouper.statements:
                for statement in grouper.get_statements():
                    print("----------")
                    if find_error(statement):
                        print("ERRORS IN QUERY")
                    process_statement(statement)
                    print_tokens(statement)
                    print()
                    statement._pprint_tree()
                print("----------")
    tokens = grouper.close()
    if tokens:
        for token in tokens:
            print_tokens(token)
            print(repr(token))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
