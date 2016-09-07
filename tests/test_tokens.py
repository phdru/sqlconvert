#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sqlparse import parse

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import remove_directives, requote_names, \
        is_directive_statement, process_statement
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

    def test_requote(self):
        parsed = parse("select * from `T`")[0]
        requote_names(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, 'SELECT * FROM "T"')

    def test_directive(self):
        parsed = parse("select /*! test */ * from /* test */ `T`")[0]
        remove_directives(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, 'SELECT * FROM /* test */ `T`')

    def test_directive_statement(self):
        parsed = parse("/*! test */ test ;")[0]
        self.assertFalse(is_directive_statement(parsed))
        parsed = parse("/*! test */ ;")[0]
        self.assertTrue(is_directive_statement(parsed))

    def test_process(self):
        parsed = parse("select /*! test */ * from /* test */ `T`")[0]
        process_statement(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, 'SELECT * FROM /* test */ "T"')


if __name__ == "__main__":
    main()
