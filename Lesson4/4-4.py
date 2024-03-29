"""
МНОЖЕСТВО в Python -  это структура данных, содержащая не повторяющиеся элементы в случайном порядке.
"""

a = set()  # Создание пустого множества

a.add(1)  # Добавление элемента в множество

a.add(2)

a.add(1)

print(a)  # Объясните результат

b = set("hello")  # Преобразование строки в множество


print(b)  # Объясните результат

"""
Множества удобно использовать для удаления повторяющихся элементов из списка
"""

a = ['aa', 'ab', 'aa', 'ba']

elementsA = set(a)
print(set(elementsA))

"""
Множества поддерживают стандартные операции других структур данных - len, in, clear и т.п. 
"""

# Вставьте пропущенную строку, чтобы оператор print выводил True

b = ['aa', 'ab', 'aa', 'ba']

# Вставьте пропущенную строку
print(len(b) == len(set(b)))

"""
Помимо базовых операций, множества в Python поддерживают операции математических множеств (объединение(union), пересечение(intersection))
"""

a = {1, 2, 3, 4}  # Создание множества
b = {3, 4, 5, 6}
c = a.union(b)  # Объединение множества
print(c)

# Вставьте пропущенное действие, чтобы в консоль вывелось пересечение множеств a и b

d = a.intersection(b)
print(d)