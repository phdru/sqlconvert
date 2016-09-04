
from sqlparse.sql import Comment
from sqlparse import tokens as T


def requote_names(token_list):
    """Remove backticks, quote non-lowercase identifiers"""
    for token in token_list.flatten():
        if token.ttype is T.Name:
            value = token.value
            if (value[0] == "`") and (value[-1] == "`"):
                value = value[1:-1]
            if value.islower():
                token.normalized = token.value = value
            else:
                token.normalized = token.value = '"%s"' % value


def remove_directives(statement):
    """Remove /*! directives */ from the first-level"""
    new_tokens = []
    for token in statement.tokens:
        if isinstance(token, Comment):
            subtokens = token.tokens
            if subtokens:
                comment = subtokens[0]
                if comment.ttype is T.Comment.Multiline and \
                        comment.value.startswith('/*!'):
                    continue
        new_tokens.append(token)
    statement.tokens = new_tokens


def process_statement(statement):
    requote_names(statement)
    remove_directives(statement)
