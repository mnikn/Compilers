import ply.lex as lex
import ply.yacc as yacc
import re

start = 'exp'

tokens = (
    'LANGLE',       # <
    'LANGSLASH',    # </
    'RANGLE',       # >
    'EQUAL',        # =
    'STRING',       # "hello"
    'WORD',         # Welcome!
    'ANDAND',       # &&
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
    'PLUS',         # +
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
    ('htmlcomment','exclusive'),
)

precedence = (
    ('left', 'OROR'), 
    ('left', 'ANDAND'), 
    ('left', 'EQUALEQUAL'), 
    ('left', 'LT', 'LE', 'GT', 'GE'), 
    ('left', 'PLUS', 'MINUS'), 
    ('left', 'TIMES', 'DIVIDE'), 
    ('right', 'NOT'),
)

t_ignore = ' ' #shortcut for whitespace

#Lex

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

#Parse

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number",p[1])

def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ("not",p[2])

def p_html(p):
    'html : elt html'
    p[0] = [p[1]] + p[2]

def p_html_emptsy(p):
    'html : '
    p[0] = []

def p_elt_word(p):
    'elt : word'
    p[0] = ('Word-element',p[1])

def p_elt_tag(p):
    'elt : LANGLE word tag-args RANGLE html ANGLESLASH word RANGLE'
    p[0] = ("tag-element",p[2],p[3],p[5],p[7])

def p_exp_binop(p):
    """exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp"""
    p[0] = ("binop",p[1],p[2],p[3])

def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call",p[1],p[3])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1]

def p_optargs_empty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]

def p_error(p):
    print "Syntax error in input!"

webpage = """Hello<!-- comment -->Good"""
htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
    tok = htmllexer.token()
    if not tok:
        break
    print tok
