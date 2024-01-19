import os
def legendre(n, x):
    if n == 0:
        return 1  # P0(x) = 1
    elif n == 1:
        return x  # P1(x) = x
    else:
        P0 = 1
        P1 = x
        for k in range(2, n + 1):
            P2 = ((2 * k - 1) * x * P1 - (k - 1) * P0) / k
            P0 = P1
            P1 = P2
        return P1

# Чтение данных N и X из файла или клавиатуры, здесь я предполагаю, что вы знаете как их получить.
# Например, здесь просто задаются значения для примера.
N = int(input("Введите значение N: "))
X = float(input("Введите значение X: "))

# Вычисляем значения полиномов от P0(x) до PN(x)
values = [legendre(i, X) for i in range(N + 1)]

output_file_path = 'output_1-1.txt'

# Проверка существования файла
if not os.path.exists(output_file_path):
    print(f"Файл {output_file_path} не найден.")
else:
    # Запись значений в файл
    with open(output_file_path, 'w') as f:
        for value in values:
            f.write(f'{value}\n')




