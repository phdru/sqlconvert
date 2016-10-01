# -*- coding: utf-8 -*-

from pytest import raises
from sqlparse import parse

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_tokens import is_newline_statement, StatementGrouper


def test_newline_statement():
    parsed = parse("\n")[0]
    assert is_newline_statement(parsed)


def test_encoding():
    parsed = parse("insert into test (1, 'тест')", 'utf-8')[0]
    query = tlist2str(parsed).encode('utf-8')
    assert query == \
        u"INSERT INTO test (1, 'тест')".encode('utf-8')


def test_unicode():
    parsed = parse(u"insert into test (1, 'тест')")[0]
    query = tlist2str(parsed)
    assert query, u"INSERT INTO test (1 == 'тест')"


def test_incomplete():
    grouper = StatementGrouper()
    grouper.process_line("select * from `T`")
    assert not grouper.statements
    assert len(grouper.statements) == 0
    raises(ValueError, grouper.close)


def test_statements():
    grouper = StatementGrouper()
    grouper.process_line("select * from T;")
    assert grouper.statements
    assert len(grouper.statements) == 1
    for statement in grouper.get_statements():
        query = tlist2str(statement)
        assert query == 'SELECT * FROM T;'
    assert len(grouper.statements) == 0
    assert grouper.close() is None
