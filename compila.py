import ply.lex as lex

tabla_variables = []
tokens=['keyword','id','oprel','numero','signo']
def t_keyword(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]|[Ff][Rr][Oo][Mm]|[Ww][Hh][Ee][Rr][Ee]'
    return t
def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
def t_oprel(t):
    r'<=|>=|<>|<|>|='
    return t
def t_numero(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t
def t_signo(t):
    r','
    return t
t_ignore = ' \t\n'

codigo = 'SeLECT col1,col2 from mi_Tabla wHERE col1 < 20'
lexer = lex.lex(debug=True)

lexer.input(codigo)

for token in lexer:
    print(token)