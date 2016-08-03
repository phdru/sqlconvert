#! /usr/bin/env python
from __future__ import print_function

import sys
from sqlparse import parse
from mysql2sql.process_tokens import requote_names
from mysql2sql.print_tokens import print_tokens


def test():
    for query in (
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one')",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one')"
    ):
        for parsed in parse(query):
            print("----------")
            requote_names(parsed)
            print_tokens(parsed)
            print()
            parsed._pprint_tree()
    print("----------")


def main(query):
    for parsed in parse(query):
        print("----------")
        requote_names(parsed)
        print_tokens(parsed)
        print()
        parsed._pprint_tree()
    print("----------")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s [-t | sql_query_string [; sql_query_string ...]]" %
                 sys.argv[0])
    if sys.argv[1] == '-t':
        test()
    else:
        query = ';'.join(sys.argv[1:])
        main(query)
