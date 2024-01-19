def binomial_coefficient(n, m):
    if m == 0 or m == n:
        return 1
    if n < m:
        return 0
    return binomial_coefficient(n - 1, m - 1) + binomial_coefficient(n - 1, m)

def main():
    # Ввод данных с клавиатуры
    n = int(input("Введите значение N: "))
    m = int(input("Введите значение M: "))

    # Проверка корректности ввода
    if n < 0 or m < 0:
        print("Неверные входные данные. Оба числа должны быть неотрицательными.")
    else:
        result = binomial_coefficient(n, m)
        print(f"C({n}, {m}) = {result}")

        # Запись результата в файл
        with open('output_2-2.txt', 'w') as f:
            f.write(f"C({n}, {m}) = {result}\n")

if __name__ == "__main__":
    main()
