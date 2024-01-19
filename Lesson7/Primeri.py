n = int(input("Введите пример значения n "))  # Пример значения n
"""Рекурсивный алгоритм"""
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

"""Итерационный алгоритм """
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Вычисление факториала с помощью рекурсивной функции
result_recursive = factorial_recursive(n)
print(f"Факториал {n} (рекурсивно): {result_recursive}")

# Вычисление факториала с помощью итерационной функции
result_iterative = factorial_iterative(n)
print(f"Факториал {n} (итерационно): {result_iterative}")

