
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
        if isinstance(token, TokenList):
            print_tokens(token, outfile, level+1)
        else:
            outfile.write(token.normalized)


def get_tokens_str(token_list):
    sio = StringIO()
    print_tokens(token_list, outfile=sio)
    return sio.getvalue()
