#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sqlparse import parse

from mysql2sql.process_tokens import requote_names
from mysql2sql.print_tokens import tlist2str
from tests import main


class TestTokens(unittest.TestCase):
    def test_requote(self):
        parsed = parse("select * from `T`")[0]
        requote_names(parsed)
        query = tlist2str(parsed)
        self.assertEqual(query, 'SELECT * FROM "T"')

    def test_encoding(self):
        parsed = parse("insert into test (1, 'тест')", 'utf-8')[0]
        query = tlist2str(parsed).encode('utf-8')
        self.assertEqual(query, u"INSERT INTO test (1, 'тест')".encode('utf-8'))

    def test_unicode(self):
        parsed = parse(u"insert into test (1, 'тест')")[0]
        query = tlist2str(parsed)
        self.assertEqual(query, u"INSERT INTO test (1, 'тест')")


if __name__ == "__main__":
    main()
