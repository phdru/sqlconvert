
from sqlparse.sql import Comment, Function, Identifier, Parenthesis, Statement
from sqlparse import tokens as T
from .process_tokens import escape_strings, is_comment_or_space


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
                ("\\'", "'"),
                ("''", "'"),
                ('\\b', '\b'),
                ('\\n', '\n'),
                ('\\r', '\r'),
                ('\\t', '\t'),
                ('\\\032', '\032'),
                ('\\\\', '\\'),
            ):
                value = value.replace(orig, repl)
            token.normalized = token.value = value


def is_insert(statement):
    for token in statement.tokens:
        if is_comment_or_space(token):
            continue
        return (token.ttype is T.DML) and (token.normalized == 'INSERT')


def split_ext_insert(statement):
    """Split extended INSERT into multiple standard INSERTs"""
    insert_tokens = []
    values_tokens = []
    last_token = None
    expected = 'INSERT'
    for token in statement.tokens:
        if is_comment_or_space(token):
            insert_tokens.append(token)
            continue
        elif expected == 'INSERT':
            if (token.ttype is T.DML) and (token.normalized == 'INSERT'):
                insert_tokens.append(token)
                expected = 'INTO'
                continue
        elif expected == 'INTO':
            if (token.ttype is T.Keyword) and (token.normalized == 'INTO'):
                insert_tokens.append(token)
                expected = 'TABLE_NAME'
                continue
        elif expected == 'TABLE_NAME':
            if isinstance(token, (Function, Identifier)):
                insert_tokens.append(token)
                expected = 'VALUES'
                continue
        elif expected == 'VALUES':
            if (token.ttype is T.Keyword) and (token.normalized == 'VALUES'):
                insert_tokens.append(token)
                expected = 'VALUES_OR_SEMICOLON'
                continue
        elif expected == 'VALUES_OR_SEMICOLON':
            if isinstance(token, Parenthesis):
                values_tokens.append(token)
                continue
            elif token.ttype is T.Punctuation:
                if token.value == ',':
                    continue
                elif token.value == ';':
                    last_token = token
                    break
        raise ValueError(
            'SQL syntax error: expected "%s", got %s "%s"' % (
                expected, token.ttype, token.normalized))
    for values in values_tokens:
        # The statemnt sets `parent` attribute of the every token to self
        # but we don't care.
        vl = [values]
        if last_token:
            vl.append(last_token)
        statement = Statement(insert_tokens + vl)
        yield statement


def process_statement(statement, quoting_style='sqlite'):
    requote_names(statement)
    unescape_strings(statement)
    remove_directive_tokens(statement)
    escape_strings(statement, quoting_style)
    if is_insert(statement):
        for statement in split_ext_insert(statement):
            yield statement
    else:
        yield statement
