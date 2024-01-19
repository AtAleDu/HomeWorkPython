def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    elif a == b == c:
        return "Треугольник равносторонний"
    elif a == b or a == c or b == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник общего вида"

# Вводим длины сторон треугольника
side1 = float(input("Введите длину первой стороны: "))
side2 = float(input("Введите длину второй стороны: "))
side3 = float(input("Введите длину третьей стороны: "))

# Получаем результат и выводим его
result = triangle(side1, side2, side3)
print(result)
