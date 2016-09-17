# -*- coding: utf-8 -*-

from sqlparse import parse

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import remove_directive_tokens, \
        is_directive_statement, requote_names, unescape_strings, \
        process_statement


def test_encoding():
    parsed = parse("insert into test (1, 'тест')", 'utf-8')[0]
    query = tlist2str(parsed).encode('utf-8')
    assert query == \
        u"INSERT INTO test (1, 'тест')".encode('utf-8')


def test_unicode():
    parsed = parse(u"insert into test (1, 'тест')")[0]
    query = tlist2str(parsed)
    assert query, u"INSERT INTO test (1 == 'тест')"


def test_directive():
    parsed = parse("select /*! test */ * from /* test */ `T`")[0]
    remove_directive_tokens(parsed)
    query = tlist2str(parsed)
    assert query == u'SELECT * FROM /* test */ `T`'


def test_directive_statement():
    parsed = parse("/*! test */ test ;")[0]
    assert not is_directive_statement(parsed)
    parsed = parse("/*! test */ ;")[0]
    assert is_directive_statement(parsed)


def test_requote():
    parsed = parse("select * from `T`")[0]
    requote_names(parsed)
    query = tlist2str(parsed)
    assert query == u'SELECT * FROM "T"'


def test_string():
    parsed = parse("insert into test values ('\"test\\\"')")[0]
    unescape_strings(parsed)
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test VALUES ('\"test\"')"


def test_process():
    parsed = parse("select /*! test */ * from /* test */ `T`")[0]
    process_statement(parsed)
    query = tlist2str(parsed)
    assert query == u'SELECT * FROM /* test */ "T"'
