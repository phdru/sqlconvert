#! /usr/bin/env python

import sys
from sqlparse import parse
from mysql2sql.process_tokens import requote_names
from mysql2sql.print_tokens import print_tokens, print_subtree


def test():
    for query in (
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one')",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one')"
    ):
        print "----------"
        for parsed in parse(query):
            requote_names(parsed)
            print_tokens(parsed)
            print_subtree(parsed)
    print "----------"


def main(query):
    parsed = parse(query)[0]
    requote_names(parsed)
    print_tokens(parsed)
    print_subtree(parsed)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: %s [-t | sql_query_string]" % sys.argv[0])
    if sys.argv[1] == '-t':
        test()
    else:
        query = sys.argv[1]
        main(query)
