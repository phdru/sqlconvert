
import sys


def print_tokens(token_list, outfile=sys.stdout):
    for token in token_list.flatten():
        outfile.write(token.normalized)


def tlist2str(token_list):
    return ''.join(token.normalized for token in token_list.flatten())
