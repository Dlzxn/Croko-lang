# tokens.py

# Типы токенов, используемых в языке
TOKEN_TYPES = {
    "VAR": "per",
    "PRINT": "out",
    "INPUT": "in",
    "IF": "if",
    "ELIF": "elif",
    "ELSE": "else",
    "FOR": "for",
    "TO": "to",
    "WITH": "with",
    "WHILE": "while",
    "FUNC": "func",
    "CLASS": "class",
    "TRY": "try",
    "TRYELSE": "tryelse",
    "FINAL": "final",
    "ERROR": "error",
    "ASSIGN": "=",
    "COLON": ":",
    "LPAREN": "(",
    "RPAREN": ")",
    "NUMBER": "NUMBER",
    "IDENTIFIER": "IDENTIFIER",
    "STRING": "STRING",
    "GT": ">",
    "LT": "<",
    "EQ": "==",
    "NEQ": "!=",
    "GTE": ">=",
    "LTE": "<="
}

# Регулярные выражения для поиска токенов в коде
TOKEN_REGEX = [
    (r'==', "EQ"),          # Равно (проверка равенства должна идти раньше одиночного "=")
    (r'!=', "NEQ"),         # Не равно
    (r'>=', "GTE"),         # Больше или равно
    (r'<=', "LTE"),         # Меньше или равно
    (r'>', "GT"),           # Больше
    (r'<', "LT"),           # Меньше
    (r'=', "ASSIGN"),       # Оператор присваивания (обрабатывается в конце, чтобы не мешал "==")
    (r'\bper\b', "VAR"),
    (r'\bout\b', "PRINT"),
    (r'\bin\b', "INPUT"),
    (r'\bif\b', "IF"),
    (r'\belif\b', "ELIF"),
    (r'\belse\b', "ELSE"),
    (r'\bfor\b', "FOR"),
    (r'\bto\b', "TO"),
    (r'\bwith\b', "WITH"),
    (r'\bwhile\b', "WHILE"),
    (r'\bfunc\b', "FUNC"),
    (r'\bclass\b', "CLASS"),
    (r'\btry\b', "TRY"),
    (r'\btryelse\b', "TRYELSE"),
    (r'\bfinal\b', "FINAL"),
    (r'\berror\b', "ERROR"),
    (r':', "COLON"),
    (r'\(', "LPAREN"),
    (r'\)', "RPAREN"),
    (r'\d+', "NUMBER"),
    (r'[a-zA-Z_]\w*', "IDENTIFIER"),
    (r'"[^"]*"', "STRING"),
    (r'\s+', None)  # Пробелы игнорируем
]

