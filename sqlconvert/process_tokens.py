
from sqlparse.sql import Comment
from sqlobject.converters import sqlrepr
from sqlparse import parse
from sqlparse.compat import PY3
from sqlparse import tokens as T


def find_error(token_list):
    """Find an error"""
    for token in token_list.flatten():
        if token.ttype is T.Error:
            return True
    return False


def is_comment_or_space(token):
    return isinstance(token, Comment) or \
        token.ttype in (T.Comment, T.Comment.Single, T.Comment.Multiline,
                        T.Newline, T.Whitespace)


def is_newline_statement(statement):
    for token in statement.tokens[:]:
        if token.ttype is not T.Newline:
            return False
    return True


def escape_strings(token_list, dbname):
    """Escape strings"""
    for token in token_list.flatten():
        if token.ttype is T.String.Single:
            value = token.value[1:-1]  # unquote by removing apostrophes
            value = sqlrepr(value, dbname)
            token.normalized = token.value = value


if PY3:
    xrange = range


class StatementGrouper(object):
    """Collect lines and reparse until the last statement is complete"""

    def __init__(self, encoding=None):
        self.lines = []
        self.statements = []
        self.encoding = encoding

    def process_line(self, line):
        self.lines.append(line)
        self.process_lines()

    def process_lines(self):
        statements = parse(''.join(self.lines), encoding=self.encoding)
        last_stmt = statements[-1]
        for i in xrange(len(last_stmt.tokens) - 1, 0, -1):
            token = last_stmt.tokens[i]
            if is_comment_or_space(token):
                continue
            if token.ttype is T.Punctuation and token.value == ';':
                break  # The last statement is complete
            # The last statement is still incomplete - wait for the next line
            return
        self.lines = []
        self.statements = statements

    def get_statements(self):
        for stmt in self.statements:
            yield stmt
        self.statements = []
        return

    def close(self):
        if not self.lines:
            return
        tokens = parse(''.join(self.lines), encoding=self.encoding)
        for token in tokens:
            if not is_comment_or_space(token):
                raise ValueError("Incomplete SQL statement: %s" %
                                 tokens)
        self.lines = []
        self.statements = []
        return tokens
