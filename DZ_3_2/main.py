
# Остальной код тестов оставляем без изменений

def is_valid_expression(expression):
    def is_operator(char):
        return char in {'+', '-', '*', '/'}

    def is_variable_or_digit(char):
        return char is not None and char.isalnum()

    stack = []
    last_char = None

    for char in expression:
        if is_variable_or_digit(char):
            if is_variable_or_digit(last_char):
                return False
        elif is_operator(char):
            if is_operator(last_char) or last_char is None or last_char == '(':
                return False
        elif char == '(':
            if is_variable_or_digit(last_char) or last_char == ')':
                return False
        elif char == ')':
            if is_operator(last_char) or last_char == '(' or last_char is None:
                return False

        last_char = char

    if is_operator(last_char) or last_char == '(':
        return False

    return True

# Пример использования:
expressions_to_check = [
    "a+b+c",
    "(a*b)/z+f",
    "a+(b*c)",
    "x+y*z)/w",
    "a1+b2*c3"
]

for expression in expressions_to_check:
    if is_valid_expression(expression):
        print(f"Выражение '{expression}' записано правильно.")
    else:
        print(f"Выражение '{expression}' записано неправильно.")
