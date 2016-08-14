
from sqlparse.sql import TokenList
from sqlparse.tokens import Name, Error


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
