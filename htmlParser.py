from htmlLexer import *
import ply.yacc as yacc

start = 'exp'

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

def p_element_word(p):
    'elt : word'
    p[0] = ('Word-element',p[1])

def p_element_tag(p):
    'elt : LANGLE WORD tag-args RANGLE html ANGLESLASH WORD RANGLE'
    p[0] = ("tag-element",p[2],p[3],p[5],p[7])
