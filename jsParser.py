from jsLexer import *
import ply.yacc as yacc

start = 'js'

precedence = (
    ('left','OROR'),
    ('left','ANDAND'),
    ('left','EQUALEQUAL'),
    ('left','LT','LE','GT','GE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MOD'),
    ('right','NOT'),
)

def p_js(p):
    'js : element js'
    p[0] = [p[1]] + p[2]

def p_js_empty(p):
    'js : '
    p[0] = []

def p_element_function(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('function',p[2],p[4],p[6])

def p_element_stmt(p):
    'element : stmt SEMICOLON'
    p[0] = ("stmt",p[1])

def p_optparams(p):
    'optparams : params'
    p[0] = p[1]

def p_optparams_empty(p):
    'optparams : '
    p[0] = []

def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [p[1]] + p[3]

def p_params_one(p):
    'params : IDENTIFIER'
    p[0] = [p[1]]

def p_compoundstmt(p):
    'compoundstmt : LBRACE stmts RBRACE'
    p[0] = p[2]

def p_stmts_empty(p):
    'stmts : '
    p[0] = []

def p_stmts(p):
    'stmts : stmt SEMICOLON stmts'
    p[0] = [p[1]] + p[3]

def p_stmt_if(p):
    'stmt : IF exp compoundstmt'
    p[0] = ('if-then',p[2],p[3])

def p_stmt_if_else(p):
    'stmt : IF exp compoundstmt ELSE compoundstmt'
    p[0] = ('if-then-else',p[2],p[3],p[5])

def p_stmt_assigment(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ('assign',p[1],p[3])

def p_stmt_return(p):
    'stmt : RETURN exp'
    p[0] = ("return",p[2])

def p_stmt_var(p):
    'stmt : VAR IDENTIFIER EQUAL exp'
    p[0] = ("var",p[2],p[4])

def p_stmt_exp(p):
    'stmt : exp'
    p[0] = ('exp',p[1])

# experession

def p_exp_identifier(p): 
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1]) 
        
def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ('number',p[1])

def p_exp_string(p):
    'exp : STRING'
    p[0] = ('string',p[1])
    
def p_exp_true(p):
    'exp : TRUE'
    p[0] = ('true','true')
    
def p_exp_false(p):
    'exp : FALSE'
    p[0] = ('false','false')
    
def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ('not', p[2])
    
def p_exp_parens(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]

def p_exp_binop(p):
    '''exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp MOD exp
           | exp DIVIDE exp
           | exp EQUALEQUAL exp
           | exp LE exp
           | exp LT exp
           | exp GE exp
           | exp GT exp
           | exp ANDAND exp
           | exp OROR exp
    '''
    p[0] = ('binop',p[1],p[2],p[3])

def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ('call',p[1],p[3])

def p_exp_optargs(p):
    'optargs : args'
    p[0] = p[1]

def p_optargs_empty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_one(p):
    'args : exp'
    p[0] = [p[1]]


jsparser = yacc.yacc() 

def test_parser(input_string): 
        jslexer.input(input_string) 
        parse_tree = jsparser.parse(input_string,lexer=jslexer) 
        return parse_tree

# Simple function with no arguments and a one-statement body.
jstext1 = "function myfun() { return nothing ; }"
jstree1 = [('function', 'myfun', [], [('return', ('identifier', 'nothing'))])]

print test_parser(jstext1) == jstree1


