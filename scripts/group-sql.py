#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlparse import parse
from mysql2sql.print_tokens import print_tokens
from mysql2sql.process_tokens import requote_names, find_error, \
    StatementGrouper


def main(*queries):
    grouper = StatementGrouper()
    for query in queries:
        grouper.process(parse(query)[0])
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
    grouper.close()


def test():
    main(
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one');",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one');"
    )


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s [-t | sql_query_string [; sql_query_string ...]]" %
                 sys.argv[0])
    if sys.argv[1] == '-t':
        test()
    else:
        queries = sys.argv[1:]
        main(*queries)
