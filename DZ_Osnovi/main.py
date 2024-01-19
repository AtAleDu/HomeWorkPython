def Power(a, b) -> float:
    if b == 0:
        return 1.0
    elif b > 0:
        return a ** b
    elif b < 0:
        return 1 / (a ** abs(b))

a, b = map(float, input('Введите 2 целых числа (основание и степень): ').split())
output = Power(a, int(b))
print(f'Число {a} в степени {b} равно: {output}')
