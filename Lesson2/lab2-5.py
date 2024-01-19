# Переменные булева типа могут принимать только два значения.
# С помощью оператора сравнения == выведите два возможных значения переменной is_equal.
# Обратите внимание на результат применения функции int() к булевому значению.


two = 2

three = 3

#

print(int())

#

print(str())

"""
В языке Python поддерживается множество операций сравнения( ==, >=, < и т.д.).
Все подобные операции имеют одинаковый приоритет. Результат сравнения - булева переменная.
Сравнения могут осуществляться в любом порядке.
"""

one = 1

two = 2

three = 3

# Сравнения (one < two) и (two < three) происходят в одно и то же время.
print(one < two < three)

# Создайте несколько переменных и осуществите различные сравнения между ними, выведите результаты в консоль.
# Задание 6
is_equal = (two == three)
is_greater = (three >= two)
print(is_equal, is_greater)