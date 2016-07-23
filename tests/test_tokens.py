#! /usr/bin/env python


import unittest
from sqlparse import parse

from mysql2sql.process_tokens import requote_names
from mysql2sql.print_tokens import get_tokens_str
from tests import main


class TestTokens(unittest.TestCase):
    def test_requote(self):
        parsed = parse("select * from `T`")[0]
        requote_names(parsed)
        query = get_tokens_str(parsed)
        self.assertEqual(query, 'SELECT * FROM "T";\n')


if __name__ == "__main__":
    main()
