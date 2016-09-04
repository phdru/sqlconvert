
from sqlparse import parse
from sqlparse.compat import PY3
from sqlparse.tokens import Name, Error, Punctuation, Comment, Newline, \
    Whitespace


def requote_names(token_list):
    """Remove backticks, quote non-lowercase identifiers"""
    for token in token_list.flatten():
        if token.ttype is Name:
            value = token.value
            if (value[0] == "`") and (value[-1] == "`"):
                value = value[1:-1]
            if value.islower():
                token.normalized = token.value = value
            else:
                token.normalized = token.value = '"%s"' % value


def find_error(token_list):
    """Find an error"""
    for token in token_list.flatten():
        if token.ttype is Error:
            return True
    return False


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
            if token.ttype in (Comment.Single, Comment.Multiline,
                               Newline, Whitespace):
                continue
            if token.ttype is Punctuation and token.value == ';':
                break  # The last statement is complete
            # The last statement is still incomplete - wait for the next line
            return
        self.lines = []
        self.statements = statements

    def get_statements(self):
        for stmt in self.statements:
            yield stmt
        self.statements = []

    def close(self):
        if not self.lines:
            return
        tokens = parse(''.join(self.lines), encoding=self.encoding)
        for token in tokens:
            if (token.ttype not in (Comment.Single, Comment.Multiline,
                                    Newline, Whitespace)):
                raise ValueError("Incomplete SQL statement: %s" %
                                 tokens)
        return tokens
