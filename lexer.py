# lexer.py

import re
from tokens import TOKEN_REGEX


def lexer(code):
    """Разбивает входной код на токены."""
    tokens = []
    lines = code.split('\n')

    for line in lines:
        code = line.strip()
        if not code:
            continue

        while code:
            matched = False
            for pattern, token_type in TOKEN_REGEX:
                regex = re.compile(pattern)
                match = regex.match(code)
                if match:
                    text = match.group(0)
                    if token_type:
                        tokens.append((token_type, text))
                    code = code[len(text):]
                    matched = True
                    break

            if not matched:
                raise SyntaxError(f"Неизвестный символ: {code[0]}")

        tokens.append(("NEWLINE", "\\n"))  # Добавляем токен новой строки

    return tokens


# Тест
if __name__ == "__main__":
    example_code = """
    per x = 10
    if x > 5:
        out(x)
    else:
        out(0)
    """

    tokens = lexer(example_code)
    print("Токены:", tokens)
