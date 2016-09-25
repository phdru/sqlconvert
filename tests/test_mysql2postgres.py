from sqlparse import parse
from sqlobject.tests.dbtest import getConnection
import pytest

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import unescape_strings
from sqlconvert.process_tokens import escape_strings

connection = getConnection()
pytestmark = pytest.mark.skipif(connection.dbName != "postgres",
                                reason="This test requires PostgreSQL")

create_postgres_test_table = """
CREATE TABLE test (
    id serial PRIMARY KEY,
    test_str VARCHAR(255) NOT NULL
);
"""


def test_mysql2postgres_string():
    connection.query(create_postgres_test_table)
    parsed = parse("insert into test (id, test_str) values "
                   "(1, '\"te\\'st\\\"\\n')")[0]
    unescape_strings(parsed)
    escape_strings(parsed, 'postgres')
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test (id, test_str) VALUES " \
                    u"(1, E'\"te''st\"\\n')"
    connection.query(query)
    test_str = connection.queryOne("SELECT test_str FROM test WHERE id=1")[0]
    assert test_str == u"\"te'st\"\n"
