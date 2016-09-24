from sqlparse import parse
from sqlobject.tests.dbtest import getConnection
import py.test

from sqlconvert.print_tokens import tlist2str
from sqlconvert.process_mysql import unescape_strings


create_postgres_test_table = """
CREATE TABLE test (
    id serial PRIMARY KEY,
    test_str VARCHAR(255) NOT NULL
);
"""


def test_mysql2postgres_string():
    connection = getConnection()
    if connection.dbName != "postgres":
        py.test.skip("This test requires PostgreSQL")
    connection.query(create_postgres_test_table)
    parsed = parse("insert into test (id, test_str) "
                   "values (1, '\"te\\'st\\\"')")[0]
    unescape_strings(parsed)
    query = tlist2str(parsed)
    assert query == u"INSERT INTO test (id, test_str) VALUES (1, '\"te''st\"')"
    connection.query(query)
    test_str = connection.queryOne("SELECT test_str FROM test WHERE id=1")[0]
    assert test_str == u"\"te'st\""
