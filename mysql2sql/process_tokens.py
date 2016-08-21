
from sqlparse.sql import Statement
from sqlparse.tokens import Name, Error, Punctuation


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


class StatementGrouper(object):
    def __init__(self):
        self.tokens = []
        self.statements = []

    def get_statements(self):
        for statement in self.statements:
            yield statement
        self.statements = []

    def process(self, tokens):
        for token in tokens:
            self.tokens.append(token)
            if (token.ttype == Punctuation) and (token.value == ';'):
                self.statements.append(Statement(self.tokens))
                self.tokens = []

    def close(self):
        if self.tokens:
            raise ValueError("Incomplete SQL statement")
