#! /usr/bin/env python
from __future__ import print_function

import argparse
import sys

from mysql2sql.print_tokens import print_tokens
from mysql2sql.process_tokens import requote_names, StatementGrouper


def main(infile, outfile):
    grouper = StatementGrouper()
    for line in infile:
        grouper.process_line(line)
        if grouper.statements:
            for statement in grouper.get_statements():
                requote_names(statement)
                print_tokens(statement, outfile=outfile)
    tokens = grouper.close()
    if tokens:
        for token in tokens:
            print_tokens(token, outfile=outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MySQL to SQL')
    parser.add_argument('-i', '--infile', help='input file name')
    parser.add_argument('-o', '--outfile', help='output file name')
    args = parser.parse_args()

    if args.infile:
        infile = open(args.infile, 'rt')
    else:
        infile = sys.stdin
        if infile.isatty():
            print("Error: cannot input from console", file=sys.stderr)
            parser.print_help()
            sys.exit()

    if args.outfile:
        try:
            outfile = open(args.outfile, 'wt')
        except:
            if infile is not sys.stdin:
                infile.close()
            raise
    else:
        outfile = sys.stdout

    main(infile, outfile)
