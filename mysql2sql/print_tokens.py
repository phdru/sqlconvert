
import sys
from sqlparse.sql import TokenList


def print_subtree(token_list, ident=0):
    for token in token_list:
        print " "*ident, repr(token)
        if isinstance(token, TokenList):
            print_subtree(token, ident+4)


def print_tokens(token_list, level=0):
    for token in token_list:
        if not isinstance(token, TokenList):
            sys.stdout.write(token.normalized)
        if isinstance(token, TokenList):
            print_tokens(token, level+1)
    if level == 0:
        print ';'
