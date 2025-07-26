import os
import regex


with open('expresiones.txt', 'r') as InFix:
    for expresion in InFix:
        expresion = expresion.strip()
        print(expresion)


def evaluar_expresion(expresion):
    #Aqui va la logica para evaluar, tomarn en cuenta que:
    # - Las operaciones son: +, -, *, /, ^
    #Hay que tomar en cuenta los espacios ' '
    # Restornar True o False si la expresion es valida para evaluar, si no es valida, refactorizarla.
    #Usar Regex para validar la expresion
    OpValidos = ['+', '-', '*', '/', '^']
    if expresion == "" or expresion is None:
        print("La Expresion que se ingreso es invalida")
        return False

def shuntingyard(expresion):
    # Aqui va la logica del algoritmo Shunting Yard para convertir la expresion infija a postfija
    # Retornar la expresion en notacion postfija

    #Esta es la Pila, parece un arreglo, pero se usa como pila
    stack = []
    #Logica va aqui

    #Evaluar la expresion matematica y devolver el resultado
    pass