import sys
import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE'
}

tokens = [
    'ID', 'CTEI', 'CTEF',
    'OPENPARENTHESES', 'CLOSEPARENTHESES',
    'DOT', 'TWODOTS', 'SEMICOLON',
    'OPENBRACE', 'CLOSEBRACE',
    'GREATER', 'LESS', 'DIFFERENT', 'CTESTRING',
    'EQUALS', 'DIVIDE', 'MULTIPLY',
    'PLUS', 'MINUS',
] + list(reserved.values())

t_OPENPARENTHESES = r'\('
t_CLOSEPARENTHESES = r'\)'
t_SEMICOLON = r'\;'
t_TWODOTS = r'\:'
t_OPENBRACE = r'\{'
t_CLOSEBRACE = r'\}'
t_EQUALS = r'\='
t_DOT = r'\.'
t_GREATER = r'\>'
t_LESS = r'\<'
t_DIFFERENT = r'\<>'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ignore = r' '

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTESTRING(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

def t_error(t):
    print("a character not valid was found")
    t.lexer.skip(1)

lexer = lex.lex()

'#parser'

def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON vars bloque
            | PROGRAM ID SEMICOLON vars
            | PROGRAM ID SEMICOLON bloque
            | PROGRAM ID SEMICOLON
    '''
    p[0] = "PROGRAM COMPILED"

def p_vars(p):
    '''
    vars : VAR varsP
    '''

def p_varsP(p):
    '''
    varsP : ID TWODOTS tipo SEMICOLON
        | ID TWODOTS tipo SEMICOLON varsP
        | ID DOT varsP
    '''

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''
    p[0] = p[1]

def p_bloque(p):
    '''
    bloque : OPENBRACE bloqueP CLOSEBRACE
    '''

def p_bloqueP(p):
    '''
    bloqueP : estatuto
            | estatuto bloqueP
            | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
            | condicion
            | escritura
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMICOLON
    '''

def p_expresion(p):
    '''
    expresion : exp expresionP
    '''

def p_expresionP(p):
    '''
    expresionP : GREATER exp
            | LESS exp
            | DIFFERENT exp
            | empty
    '''

def p_escritura(p):
    '''
    escritura : PRINT OPENPARENTHESES escrituraP CLOSEPARENTHESES SEMICOLON
    '''

def p_escrituraP(p):
    '''
    escrituraP : expresion
            | expresion DOT escrituraP
            | CTESTRING
            | CTESTRING DOT
    '''

def p_condicion(p):
    '''
    condicion : condicionP bloque SEMICOLON
            | condicionP bloque ELSE bloque SEMICOLON
    '''

def p_condicionP(p):
    '''
    condicionP : IF OPENPARENTHESES expresion CLOSEPARENTHESES
    '''

def p_exp(p):
    '''
    exp : termino expP
    '''

def p_expP(p):
    '''
    expP : PLUS exp
         | MINUS exp
         | empty
    '''

def p_termino(p):
    '''
    termino : factor terminoP
    '''

def p_terminoP(p):
    '''
    terminoP : MULTIPLY terminoP
            | DIVIDE terminoP
            | empty
    '''

def p_factor(p):
    '''
    factor : OPENPARENTHESES expresion CLOSEPARENTHESES
            | factorP
    '''

def p_factorP(p):
    '''
    factorP : PLUS varcte
            | MINUS varcte
            | varcte
    '''

def p_varcte(p):
    '''
    varcte : ID
            | CTEI
            | CTEF
    '''

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
   print("Syntax error in input!")


parser = yacc.yacc()

if __name__ == '__main__':
    try:
        archivo = open('test_fail.txt','r')
        info = archivo.read()
        archivo.close()
        if(yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("success")
        else:
            print("syntax error")
    except EOFError:
        print(EOFError)