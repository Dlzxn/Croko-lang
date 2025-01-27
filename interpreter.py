# interpreter.py

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, node):
        if node.node_type == "PROGRAM":
            for child in node.children:
                self.interpret(child)
        elif node.node_type == "ASSIGNMENT":
            var_name, value = node.value
            self.variables[var_name] = int(value)
            print(f"Переменная {var_name} = {value}")
        elif node.node_type == "PRINT":
            var_name = node.value
            if var_name in self.variables:
                print(f"Вывод: {self.variables[var_name]}")
            else:
                raise RuntimeError(f"Переменная '{var_name}' не найдена")
