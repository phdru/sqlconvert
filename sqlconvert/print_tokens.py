
import sys


def print_tokens(token_list, outfile=sys.stdout, encoding=None):
    if encoding:
        buffer = getattr(outfile, 'buffer', outfile)
    else:
        buffer = outfile
    for token in token_list.flatten():
        normalized = token.normalized
        if encoding:
            normalized = normalized.encode(encoding)
        buffer.write(normalized)
    if buffer is not outfile:
        buffer.flush()
    outfile.flush()


def tlist2str(token_list):
    return u''.join(token.normalized for token in token_list.flatten())
