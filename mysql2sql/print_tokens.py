
import sys
try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
from sqlparse.sql import TokenList


def print_tokens(token_list, outfile=sys.stdout, level=0):
    for token in token_list:
        if not isinstance(token, TokenList):
            outfile.write(token.normalized)
        if isinstance(token, TokenList):
            print_tokens(token, outfile, level+1)
    if level == 0:
        outfile.write(';\n')


def get_tokens_str(token_list):
    sio = StringIO()
    print_tokens(token_list, outfile=sio)
    return sio.getvalue()
