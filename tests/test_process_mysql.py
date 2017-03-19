# -*- coding: utf-8 -*-

from sqlparse import parse

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import remove_directive_tokens, \
        is_directive_statement, requote_names, unescape_strings, \
        is_insert, process_statement
from sqlconvert.process_tokens import escape_strings


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


def test_unescape_string():
    parsed = parse("insert into test values ('\"te\\'st\\\"\\n')")[0]
    unescape_strings(parsed)
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test VALUES ('\"te'st\"\n')"


def test_escape_string_postgres():
    parsed = parse("insert into test values ('\"te\\'st\\\"\\n')")[0]
    unescape_strings(parsed)
    escape_strings(parsed, 'postgres')
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test VALUES (E'\"te''st\"\\n')"


def test_escape_string_sqlite():
    parsed = parse("insert into test values ('\"te\\'st\\\"\\n')")[0]
    unescape_strings(parsed)
    escape_strings(parsed, 'sqlite')
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test VALUES ('\"te''st\"\n')"


def test_is_insert():
    parsed = parse("select /*! test */ * from /* test */ `T`")[0]
    statement = next(process_statement(parsed))
    assert not is_insert(statement)

    parsed = parse("insert into test values ('\"te\\'st\\\"\\n')")[0]
    statement = next(process_statement(parsed))
    assert is_insert(statement)


def test_split_ext_insert():
    parsed = parse("insert into test values (1, 2)")[0]
    statement = next(process_statement(parsed))
    query = tlist2str(statement)
    assert query == u"INSERT INTO test VALUES (1, 2)"

    parsed = parse("insert into test (age, salary) values (1, 2);")[0]
    statement = next(process_statement(parsed))
    query = tlist2str(statement)
    assert query == u"INSERT INTO test (age, salary) VALUES (1, 2);"

    parsed = parse("insert into test values (1, 2), (3, 4);")[0]
    stiter = process_statement(parsed)
    statement = next(stiter)
    query = tlist2str(statement)
    assert query == u"INSERT INTO test VALUES  (1, 2);\n"
    statement = next(stiter)
    query = tlist2str(statement)
    assert query == u"INSERT INTO test VALUES  (3, 4);"

    parsed = parse("insert into test (age, salary) values (1, 2), (3, 4)")[0]
    stiter = process_statement(parsed)
    statement = next(stiter)
    query = tlist2str(statement)
    assert query == u"INSERT INTO test (age, salary) VALUES  (1, 2)\n"
    statement = next(stiter)
    query = tlist2str(statement)
    assert query == u"INSERT INTO test (age, salary) VALUES  (3, 4)"


def test_process():
    parsed = parse("select /*! test */ * from /* test */ `T`")[0]
    statement = next(process_statement(parsed))
    query = tlist2str(statement)
    assert query == u'SELECT * FROM /* test */ "T"'
