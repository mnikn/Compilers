import ply.lex as lex

tokens = (
    'LANGLE',       # <
    'LANGSLASH',    # </
    'RANGLE',       # >
    'EQUAL',        # =
    'STRING',       # "hello"
    'WORD',         # Welcome!
)


states = (
    ('htmlcomment','exclusive'),
)

t_ignore = ' ' #shortcut for whitespace

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
    token.lexer.skip(1) #error

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGSLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token

def t_NUMBER(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

"""
webpage = "Hello Good"
htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
    tok = htmllexer.token()
    if not tok:
        break
    print tok
"""
