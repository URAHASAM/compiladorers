class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def ft(s, c):
    if s == 0:
        if c == 't':
            return Nodo('t'), 1
        else:
            return None, 0
    elif s == 1:
        if c == 'h':
            return Nodo('h'), 2
        else:
            return None, 0
    elif s == 2:
        if c == 'e':
            return Nodo('e'), 3
        else:
            return None, 0
    elif s == 3:
        if c == 'n':
            return Nodo('n'), 4
        else:
            return None, 0
    else:
        return None, 0

def verificarNum(cadena):
    estado = 12
    for c in cadena:
        if estado == 12:
            if c.isdigit():
                estado = 13
            else:
                estado = -1
                break
        elif estado == 13:
            if c.isdigit():
                estado = 13
            elif c == '.':
                estado = 14
            elif c in ('E', 'e'):
                estado = 16
            elif c == '#':
                estado = 20
            else:
                estado = -1
                break
        elif estado == 14:
            if c.isdigit():
                estado = 15
            else:
                estado = -1
                break
        elif estado == 15:
            if c.isdigit():
                estado = 15
            elif c in ('E', 'e'):
                estado = 16
            elif c == '#':
                estado = 21
            else:
                estado = -1
                break
        elif estado == 16:
            if c == '+' or c == '-':
                estado = 17
            elif c.isdigit():
                estado = 18
            else:
                estado = -1
                break
        elif estado == 17:
            if c.isdigit():
                estado = 18
            else:
                estado = -1
                break
        elif estado == 18:
            if c.isdigit():
                estado = 18
            elif c == '#':
                estado = 19
            else:
                estado = -1
                break

    if estado == 13 or estado == 15 or estado == 18 or estado == 19 or estado == 20 or estado == 21:
        return "Numero"
    else:
        return "es un elemento oprel"

def clasificar_subcomponentes(subcomponente):
    if subcomponente.isalpha():
        return "Cadena"
    elif subcomponente.isdigit():
        return "Numero"
    else:
        return "Simbolo"

def clasificar_lexema(lexema):
    subcomponentes = []
    subcomponente_actual = ""

    for c in lexema:
        if c.isalnum() or c == '.' or c in ('E', 'e', '+', '-'):
            subcomponente_actual += c
        else:
            if subcomponente_actual:
                subcomponentes.append(subcomponente_actual)
            subcomponente_actual = ""
            subcomponentes.append(c)

    if subcomponente_actual:
        subcomponentes.append(subcomponente_actual)

    clasificaciones = [clasificar_subcomponentes(sub) for sub in subcomponentes]

    return list(zip(subcomponentes, clasificaciones))

def probar_clasificar_lexema():
    ejemplos = [
        "<=",  # Operador Relacional
        "+ 123",  # Combinación de componentes
        "abc",  # Identificador
        "123ee",
        "123.45 e ++",
        "1234 e + 5",
        "23 e - 24",
        "0.3456",
        "10.11 e 12",
        "suma",
        "then",
        "while",
        "123 #",
    ]

    for lexema in ejemplos:
        clasificaciones = clasificar_lexema(lexema)
        print(f'Lexema: "{lexema}" - Clasificaciones: {clasificaciones}')

probar_clasificar_lexema()