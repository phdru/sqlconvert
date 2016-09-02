
import sys


def print_tokens(token_list, outfile=sys.stdout, encoding=None):
    if encoding:
        outfile = getattr(outfile, 'buffer', outfile)
    for token in token_list.flatten():
        normalized = token.normalized
        if encoding:
            normalized = normalized.encode(encoding)
        outfile.write(normalized)


def tlist2str(token_list):
    return u''.join(token.normalized for token in token_list.flatten())
