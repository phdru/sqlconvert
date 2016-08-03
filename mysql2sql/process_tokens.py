
from sqlparse.sql import TokenList
from sqlparse.tokens import Name


def requote_names(token_list):
    """Remove backticks, quote non-lowercase identifiers"""
    for token in token_list:
        if isinstance(token, TokenList):
            requote_names(token)
        else:
            if token.ttype is Name:
                value = token.value
                if (value[0] == "`") and (value[-1] == "`"):
                    value = value[1:-1]
                if value.islower():
                    token.normalized = token.value = value
                else:
                    token.normalized = token.value = '"%s"' % value
