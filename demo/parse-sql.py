#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlparse import parse
from sqlconvert.print_tokens import print_tokens
from sqlconvert.process_tokens import find_error


def main(*queries):
    for query in queries:
        for parsed in parse(query, encoding='utf-8'):
            print("----------")
            if find_error(parsed):
                print("ERRORS IN QUERY")
            print_tokens(parsed, encoding='utf-8')
            print()
            parsed._pprint_tree()
        print("----------")


def test():
    main(
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one')",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one')"
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
