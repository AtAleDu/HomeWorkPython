import os

def is_prime(n):
    """Проверка, является ли число простым."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def generate_primes_up_to_n(n):
    """Генерация списка простых чисел до заданного числа N."""
    return [i for i in range(2, n+1) if is_prime(i)]

# Основная часть программы
file_content = ""
if os.path.exists("PDF_6_5_3_input.txt"):
    with open("PDF_6_5_3_input.txt", "r", encoding="utf-8") as f:
        file_content = f.read().strip()

if not file_content or file_content == "-":
    with open("PDF_6_5_3_output.txt", "w", encoding="utf-8") as f:
        f.write("Файл с входными данными не\nобнаружен")
else:
    try:
        N = int(file_content)
        primes = generate_primes_up_to_n(N)

        with open("PDF_6_5_3_output.txt", "w", encoding="utf-8") as out_file:
            out_file.write(" ".join(map(str, primes)))
    except ValueError:
        with open("PDF_6_5_3_output.txt", "w", encoding="utf-8") as out_file:
            out_file.write("Неверный формат данных в файле input.txt")
