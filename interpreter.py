# This program is a simple calculator that takes an expression as input and returns the result of the operation.
import re

def main():
    statement = input("Expression: ").strip()

    # Expresión regular para encontrar la operación y los operandos
    pattern = r"(\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(\d+(?:\.\d+)?)"
    match = re.match(pattern, statement)

    if not match:
        print("Expresión no válida")
        return

    a, operator, b = match.groups()
    a, b = float(a), float(b)

    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(subtract(a, b))
    elif operator == "*":
        print(multiply(a, b))
    elif operator == "/":
        if b == 0:
            print("No se puede dividir por cero")
        else:
            print(divide(a, b))

def add(a, b):
    return round(a + b, 1)

def subtract(a, b):
    return round(a - b, 1)

def multiply(a, b):
    return round(a * b, 1)

def divide(a, b):
    return round(a / b, 1)

main()
