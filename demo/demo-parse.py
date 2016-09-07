#! /usr/bin/env python
from __future__ import print_function

import argparse
from sqlparse import parse
from sqlconvert.print_tokens import print_tokens
from sqlconvert.process_tokens import find_error


def parse_queries(*queries):
    for query in queries:
        for parsed in parse(query, encoding='utf-8'):
            print("----- -----")
            if find_error(parsed):
                print("ERRORS IN QUERY")
            print_tokens(parsed, encoding='utf-8')
            print()
            parsed._pprint_tree()
        print("-----/-----")


def parse_test(_args):
    parse_queries(
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one')",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one')"
    )


def parse_sql(args):
    parse_queries(*args.lines)


def parse_file(args):
    infile = open(args.filename, 'rt')
    lines = infile.readlines()
    infile.close()
    parse_queries(*lines)


if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(description='Parse')
    subparsers = main_parser.add_subparsers(help='Commands')

    parser = subparsers.add_parser('sql', help='SQL from command line')
    parser.add_argument('lines', nargs='+', help='SQL lines')
    parser.set_defaults(func=parse_sql)

    parser = subparsers.add_parser('test', help='SQL from test data')
    parser.set_defaults(func=parse_test)

    parser = subparsers.add_parser('file', help='SQL from a file')
    parser.add_argument('filename', help='SQL file')
    parser.set_defaults(func=parse_file)

    args = main_parser.parse_args()
    args.func(args)
