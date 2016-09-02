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
    parser.add_argument('-o', '--outfile', help='output file name')
    parser.add_argument('infile', help='input file name')
    parser.add_argument('output_file', nargs='?', help='output file name')
    args = parser.parse_args()

    if args.infile:
        if args.infile == '-':
            infile = sys.stdin
        else:
            infile = open(args.infile, 'rt')
    else:
        infile = sys.stdin

    if infile.isatty():
        print("Error: cannot read from console", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    if args.outfile:
        if args.output_file:
            print("Error: too many output files", file=sys.stderr)
            parser.print_help()
            sys.exit(1)

        outfile = args.outfile

    elif args.output_file:
        outfile = args.output_file

    else:
        outfile = '-'

    if outfile == '-':
        outfile = sys.stdout
    else:
        try:
            outfile = open(outfile, 'wt')
        except:
            if infile is not sys.stdin:
                infile.close()
            raise

    main(infile, outfile)
