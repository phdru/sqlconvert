#! /usr/bin/env python


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


if __name__ == "__main__":
    main()
