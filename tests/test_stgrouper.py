#! /usr/bin/env python


import unittest

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import requote_names
from sqlconvert.process_tokens import StatementGrouper
from tests import main


class TestStGrouper(unittest.TestCase):
    def test_incomplete(self):
        grouper = StatementGrouper()
        grouper.process_line("select * from `T`")
        self.assertFalse(grouper.statements)
        self.assertEqual(len(grouper.statements), 0)
        self.assertRaises(ValueError, grouper.close)

    def test_statements(self):
        grouper = StatementGrouper()
        grouper.process_line("select * from `T`;")
        self.assertTrue(grouper.statements)
        self.assertEqual(len(grouper.statements), 1)
        for statement in grouper.get_statements():
            requote_names(statement)
            query = tlist2str(statement)
            self.assertEqual(query, 'SELECT * FROM "T";')
        self.assertEqual(len(grouper.statements), 0)
        self.assertEqual(grouper.close(), None)

if __name__ == "__main__":
    main()
