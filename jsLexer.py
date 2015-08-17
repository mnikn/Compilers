import ply.lex as lex

tokens = (
    'COMMA',        # ,
    'DIVIDE',       # /
    'ELSE',         # else
    'EQUAL',        # =
    'EQUALEQUAL',   # ==
    'FALSE',        # false
    'FUNCTION',     # function
    'GE',           # >=
    'GT',           # >
    'IDENTIFIER',   # factorial
    'IF',           # if
    'LBRACE',       # {
    'LE',           # <=
    'LPAREN',       # (
    'LT',           # <
    'MINUS',        # -
    'NOT',          # !
    'NUMBER',       # 1234 5.678
    'OROR',         # ||
    'ANDAND',       # &&
    'PLUS',         # +
    'MOD',          # %
    'RBRACE',       # }
    'RETURN',       # return
    'RPAREN',       # )
    'SEMICOLON',    # ;
    'STRING',       # "this is a \"tricky\" string"
    'TIMES',        # *
    'TRUE',         # TRUE
    'VAR',          # var 
)

states = (
    ('jscomment','exclusive'),
)

t_ignore = ' ' 

def t_jscomment(t):
    r'/\*'
    t.lexer.begin('jscomment')

def t_jscomment_end(t):
    r'\*/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')

def t_jscomment_error(t):
    t.lexer.skip(1)

def t_error(t):
    t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    pass

def t_COMMA(t):
    r','
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_EQUAL(t):
    r'='
    return t

def t_EQUALEQUAL(t):
    r'=='
    return t

def t_FALSE(t):
    r'false'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GE(t):
    r'>='
    return t

def t_GT(t):
    r'>'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][0-9a-zA-Z_]+'
    return t

def t_IF(t):
    r'if'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_LE(t):
    r'<='
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_LT(t):
    r'<'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_NOT(t):
    r'!'
    return t

def t_NUMBER(t):
    r'[0-9]+(?:.[0-9]+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_OROR(t):
    r'\|\|'
    return t

def t_ANDAND(t):
    r'\&\&'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MOD(t):
    r'%'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_STRING(t):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_TIMES(t):
    r'\*'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_VAR(t):
    r'var'
    return t

jslexer = lex.lex()

"""
webpage = "if (foo){fine;}"
jslexer.input(webpage)
while True:
    tok = jslexer.token()
    if not tok:
        break
    print tok
"""
