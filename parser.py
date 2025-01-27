# parser.py

from tokens import TOKEN_TYPES

class ASTNode:
    """Базовый класс для узлов AST"""
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def __repr__(self):
        return f"{self.node_type}({self.value}, {self.children})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        """Создает AST"""
        root = ASTNode("PROGRAM")
        while self.pos < len(self.tokens):
            statement = self.parse_statement()
            if statement:
                root.children.append(statement)
        return root

    def parse_statement(self):
        """Распознаем операторы (переменные, вывод, условия и т.д.)."""
        if self.match("VAR"):
            return self.parse_assignment()
        elif self.match("PRINT"):
            return self.parse_print()
        elif self.match("IF"):
            return self.parse_if()
        elif self.match("ELIF") or self.match("ELSE"):
            raise SyntaxError("Unexpected 'elif' or 'else' without preceding 'if'")
        elif self.match("NEWLINE"):
            self.pos += 1  # Пропускаем пустые строки
            return None
        else:
            raise SyntaxError(f"Неожиданный токен: {self.tokens[self.pos]}")

    def parse_assignment(self):
        self.expect("VAR")
        var_name = self.expect("IDENTIFIER")[1]
        self.expect("ASSIGN")
        value = self.expect("NUMBER")[1]
        return ASTNode("ASSIGNMENT", (var_name, value))

    def parse_print(self):
        self.expect("PRINT")
        self.expect("LPAREN")
        var_name = self.expect("IDENTIFIER")[1]
        self.expect("RPAREN")
        return ASTNode("PRINT", var_name)

    def parse_if(self):
        """Обработка конструкции if-elif-else."""
        self.expect("IF")
        condition = self.parse_condition()
        self.expect("COLON")

        # Парсим тело if
        body = []
        while not self.match("ELIF") and not self.match("ELSE") and not self.match("NEWLINE"):
            statement = self.parse_statement()
            if statement:
                body.append(statement)

        # Парсим elif блоки
        elif_body = []
        while self.match("ELIF"):
            self.expect("ELIF")
            elif_condition = self.parse_condition()
            self.expect("COLON")
            statements = []
            while not self.match("ELIF") and not self.match("ELSE") and not self.match("NEWLINE"):
                statement = self.parse_statement()
                if statement:
                    statements.append(statement)
            elif_body.append((elif_condition, statements))

        # Парсим else блок
        else_body = []
        if self.match("ELSE"):
            self.expect("ELSE")
            self.expect("COLON")
            while not self.match("NEWLINE"):
                statement = self.parse_statement()
                if statement:
                    else_body.append(statement)

        return ASTNode("IF", (condition, body, elif_body, else_body))

    def match(self, token_type):
        return self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type

    def expect(self, token_type):
        if self.match(token_type):
            self.pos += 1
            return self.tokens[self.pos - 1]
        raise SyntaxError(f"Ожидался {token_type}, получен {self.tokens[self.pos][0]}")

    def parse_condition(self):
        """Парсим условное выражение (например, x > 10 или x == y)"""
        left = self.expect("IDENTIFIER")[1]

        if self.match("GT"):
            operator = "GT"
        elif self.match("LT"):
            operator = "LT"
        elif self.match("EQ"):
            operator = "EQ"
        elif self.match("NEQ"):
            operator = "NEQ"
        elif self.match("GTE"):
            operator = "GTE"
        elif self.match("LTE"):
            operator = "LTE"
        else:
            raise SyntaxError("Ожидался оператор сравнения")

        self.expect(operator)

        if self.match("NUMBER"):
            right = self.expect("NUMBER")[1]
        elif self.match("IDENTIFIER"):
            right = self.expect("IDENTIFIER")[1]
        else:
            raise SyntaxError("Ожидалась переменная или число в правой части условия")

        return (left, operator, right)

        self.expect(operator)

        if self.match("NUMBER"):
            right = self.expect("NUMBER")[1]
        elif self.match("IDENTIFIER"):
            right = self.expect("IDENTIFIER")[1]
        else:
            raise SyntaxError("Ожидалась переменная или число в правой части условия")

        return (left, operator, right)


