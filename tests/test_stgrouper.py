#! /usr/bin/env python


import unittest
from sqlparse import parse

from mysql2sql.print_tokens import tlist2str
from mysql2sql.process_tokens import requote_names, StatementGrouper
from tests import main


class TestStGrouper(unittest.TestCase):
    def test_incomplete(self):
        grouper = StatementGrouper()
        parsed = parse("select * from `T`")[0]
        grouper.process(parsed)
        self.assertFalse(grouper.statements)
        self.assertEqual(len(grouper.statements), 0)
        self.assertRaises(ValueError, grouper.close)

    def test_statements(self):
        grouper = StatementGrouper()
        parsed = parse("select * from `T`;")[0]
        grouper.process(parsed)
        self.assertTrue(grouper.statements)
        self.assertEqual(len(grouper.statements), 1)
        g = grouper.get_statements()
        statement = next(g)
        requote_names(statement)
        query = tlist2str(parsed)
        self.assertEqual(query, 'SELECT * FROM "T";')
        self.assertRaises(StopIteration, next, g)
        self.assertEqual(len(grouper.statements), 0)
        self.assertEqual(grouper.close(), [])

if __name__ == "__main__":
    main()
