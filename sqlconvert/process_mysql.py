
from sqlparse.sql import Comment
from sqlparse import tokens as T


def _is_directive_token(token):
    if isinstance(token, Comment):
        subtokens = token.tokens
        if subtokens:
            comment = subtokens[0]
            if comment.ttype is T.Comment.Multiline and \
                    comment.value.startswith('/*!'):
                return True
    return False


def is_directive_statement(statement):
    tokens = statement.tokens
    if not _is_directive_token(tokens[0]):
        return False
    if tokens[-1].ttype is not T.Punctuation or tokens[-1].value != ';':
        return False
    for token in tokens[1:-1]:
        if token.ttype not in (T.Newline, T.Whitespace):
            return False
    return True


def remove_directive_tokens(statement):
    """Remove /*! directives */ from the first-level"""
    new_tokens = []
    for token in statement.tokens:
        if _is_directive_token(token):
            continue
        new_tokens.append(token)
    statement.tokens = new_tokens


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


def unescape_strings(token_list):
    """Unescape strings"""
    for token in token_list.flatten():
        if token.ttype is T.String.Single:
            value = token.value
            for orig, repl in (
                ('\\"', '"'),
                ("\\'", "''"),
                ('\\\032', '\032'),
            ):
                value = value.replace(orig, repl)
            token.normalized = token.value = value


def process_statement(statement):
    remove_directive_tokens(statement)
    requote_names(statement)
    unescape_strings(statement)
