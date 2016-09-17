
from pytest import raises
from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_tokens import StatementGrouper


class TestStGrouper(object):
    def test_incomplete(self):
        grouper = StatementGrouper()
        grouper.process_line("select * from `T`")
        assert not grouper.statements
        assert len(grouper.statements) == 0
        raises(ValueError, grouper.close)

    def test_statements(self):
        grouper = StatementGrouper()
        grouper.process_line("select * from T;")
        assert grouper.statements
        assert len(grouper.statements) == 1
        for statement in grouper.get_statements():
            query = tlist2str(statement)
            assert query == 'SELECT * FROM T;'
        assert len(grouper.statements) == 0
        assert grouper.close() is None
