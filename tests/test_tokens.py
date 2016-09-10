#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sqlparse import parse

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import remove_directive_tokens, \
        is_directive_statement, requote_names, unescape_strings, \
        process_statement
from tests import main


class TestTokens(unittest.TestCase):
    def test_encoding(self):
        parsed = parse("insert into test (1, 'тест')", 'utf-8')[0]
        query = tlist2str(parsed).encode('utf-8')
        self.assertEqual(query,
                         u"INSERT INTO test (1, 'тест')".encode('utf-8'))

    def test_unicode(self):
        parsed = parse(u"insert into test (1, 'тест')")[0]
        query = tlist2str(parsed)
        self.assertEqual(query, u"INSERT INTO test (1, 'тест')")

    def test_directive(self):
        parsed = parse("select /*! test */ * from /* test */ `T`")[0]
        remove_directive_tokens(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, u'SELECT * FROM /* test */ `T`')

    def test_directive_statement(self):
        parsed = parse("/*! test */ test ;")[0]
        self.assertFalse(is_directive_statement(parsed))
        parsed = parse("/*! test */ ;")[0]
        self.assertTrue(is_directive_statement(parsed))

    def test_requote(self):
        parsed = parse("select * from `T`")[0]
        requote_names(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, u'SELECT * FROM "T"')

    def test_string(self):
        parsed = parse("insert into test values ('\"test\\\"')")[0]
        unescape_strings(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, u"INSERT INTO test VALUES ('\"test\"')")

    def test_process(self):
        parsed = parse("select /*! test */ * from /* test */ `T`")[0]
        process_statement(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, u'SELECT * FROM /* test */ "T"')


if __name__ == "__main__":
    main()
