
import sys
try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO


def print_tokens(token_list, outfile=sys.stdout):
    for token in token_list.flatten():
        outfile.write(token.normalized)


def get_tokens_str(token_list):
    sio = StringIO()
    print_tokens(token_list, outfile=sio)
    return sio.getvalue()
