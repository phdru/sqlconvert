
from sqlparse import parse
from sqlparse.compat import PY3
from sqlparse import tokens as T


def find_error(token_list):
    """Find an error"""
    for token in token_list.flatten():
        if token.ttype is T.Error:
            return True
    return False


def is_newline_statement(statement):
    for token in statement.tokens[:]:
        if token.ttype is not T.Newline:
            return False
    return True


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
            if token.ttype in (T.Comment.Single, T.Comment.Multiline,
                               T.Newline, T.Whitespace):
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
        raise StopIteration

    def close(self):
        if not self.lines:
            return
        tokens = parse(''.join(self.lines), encoding=self.encoding)
        for token in tokens:
            if (token.ttype not in (T.Comment.Single, T.Comment.Multiline,
                                    T.Newline, T.Whitespace)):
                raise ValueError("Incomplete SQL statement: %s" %
                                 tokens)
        return tokens
