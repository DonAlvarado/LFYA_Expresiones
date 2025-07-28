import os
import regex

def evaluar_expresion(expresion):
    OpValidos = ['+', '-', '*', '/', '^']
    if not expresion or expresion.strip() == "":
        print("La Expresión que se ingresó es inválida")
        return False

    patron = r'^[\dA-Za-z\s\+\-\*/\^\(\)]+$'
    if not regex.match(patron, expresion):
        print(f"Expresión inválida (caracteres no permitidos): {expresion}")
        return False

    stack = []
    for char in expresion:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                print(f"Paréntesis no balanceados: {expresion}")
                return False
        
        

    if stack:
        print(f"Paréntesis no balanceados: {expresion}")
        return False

    return True


def shuntingyard(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = []
    salida = []

    tokens = expresion.split()

    for token in tokens:
        if token.isalnum():
            salida.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                salida.append(operadores.pop())
            operadores.pop()
        else:
            while (operadores and operadores[-1] != '(' and
                precedencia.get(token, 0) <= precedencia.get(operadores[-1], 0)):
                salida.append(operadores.pop())
            operadores.append(token)

    while operadores:
        salida.append(operadores.pop())

    return ' '.join(salida)


# 🤖 Prompt: Ya se que para operar todo tengo que recorrer de char en char, lo que pasa es que
# que funciones en python tengo que utilizar para convertir los caracteres a numeros y como
# hacer que los operadores se interpreten como operadores matematicos para los numeros.

def Operar(postfix):
    stack = []
    Chars = postfix.split()

    for char in Chars:
        if char.isalnum():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(str(float(a) + float(b)))
            elif char == '-':
                stack.append(str(float(a) - float(b)))
            elif char == '*':
                stack.append(str(float(a) * float(b)))
            elif char == '/':
                stack.append(str(float(a) / float(b)))
            elif char == '^':
                stack.append(str(float(a) ** float(b)))

    return stack[0] if stack else None