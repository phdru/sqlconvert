# -*- coding: utf-8 -*-

try:
    from io import StringIO, BytesIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
    BytesIO = StringIO

from sqlparse import parse
from sqlconvert.print_tokens import print_tokens


def test_print_tokens():
    sio = StringIO()
    parsed = parse("select * from T")[0]
    print_tokens(parsed, outfile=sio)
    assert sio.getvalue() == u"SELECT * FROM T"


def test_print_tokens_encoded():
    sio = BytesIO()
    parsed = parse("select * from T")[0]
    print_tokens(parsed, outfile=sio, encoding='ascii')
    assert sio.getvalue() == b"SELECT * FROM T"
