"""
Этот модуль содержит класс Calculator
"""

#калькулятор классов:
class Calculator:

#определение __инициализации__(самостоятельно):
    def __init__(self):
        self.current = 0

#определение add(self, сумма):
    def add(self, amount):
        self.current += amount

#определение get_current(self):
    def get_current(self):
        return self.current # return: Ключевое слово в Python для возврата значения из функции или метода.

"""Таким образом, когда вы вызываете метод get_current для объекта класса Calculator, он возвращает текущее значение атрибута current для этого конкретного объекта."""