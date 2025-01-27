from lexer import lexer
from parser import Parser

code = """
per x = 10
if x > 5:
    out(x)
elif x == 5:
    out("x равен 5")
else:
    out(0)
"""

tokens = lexer(code)
print("Токены:", tokens)

parser = Parser(tokens)
ast = parser.parse()
print("AST:", ast)
