#! /usr/bin/env python
from __future__ import print_function

import argparse
from sqlconvert.print_tokens import print_tokens
from sqlconvert.process_tokens import find_error, StatementGrouper


def group_lines(*lines):
    grouper = StatementGrouper(encoding='utf-8')
    for line in lines:
        grouper.process_line(line)
        for statement in grouper.get_statements():
            print("----- -----")
            if find_error(statement):
                print("ERRORS IN QUERY")
            print_tokens(statement, encoding='utf-8')
            print()
            statement._pprint_tree()
            print("-----/-----")
    tokens = grouper.close()
    if tokens:
        for token in tokens:
            print_tokens(token, encoding='utf-8')
            print(repr(token))


def group_test(_args):
    group_lines(
        "SELECT * FROM `mytable`; -- line-comment",
        "INSERT into /* inline comment */ mytable VALUES (1, 'one');",
        "/*! directive*/ INSERT INTO `MyTable` (`Id`, `Name`) "
        "VALUES (1, 'one');"
    )


def group_sql(args):
    group_lines(*args.lines)


def group_file(args):
    infile = open(args.filename, 'rt')
    lines = infile.readlines()
    infile.close()
    group_lines(*lines)


if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(description='Group')
    subparsers = main_parser.add_subparsers(help='Commands')

    parser = subparsers.add_parser('sql', help='SQL from command line')
    parser.add_argument('lines', nargs='+', help='SQL lines')
    parser.set_defaults(func=group_sql)

    parser = subparsers.add_parser('test', help='SQL from test data')
    parser.set_defaults(func=group_test)

    parser = subparsers.add_parser('file', help='SQL from a file')
    parser.add_argument('filename', help='SQL file')
    parser.set_defaults(func=group_file)

    args = main_parser.parse_args()
    args.func(args)
