""" Функции - это удобный способ разделить ваш код на полезные блоки, сделать его более читабельным и помочь в его повторном использовании.

Функции определяются с помощью ключевого слова def, за которым следует имя функции. """


def hello_world():  # Функция с именем "hello_world"
    print("Hello, World!")  # Обратите внимание на отступ!


# Определите функцию с именем fun, печатающую при своем вызове любой афоризм


# Это основная программа (Напишите эту заметку при написании основной программы)

for i in range(3):
    hello_world()  # вызов функции, определенной выше

# замените дубликаты строк в файле (реализуйте подпрограмму, которая печатает сообщение на экран)
"""""
print('I want to be a function')
print('I want to be a function')
print('I want to be a function')
"""""
def iwantToBeaFunction():
    for i in range(3):
        print('I want to be a function')


iwantToBeaFunction()
# -----------------------------------------------------------------------------------------#


""" Параметры функции определены в скобках (), следующих после имени функции.  

Параметры ведут себя как переменные, видимые исключительно внутри тела функции """


def foo(x):  # x - параметр функции
    print("x = " + str(x))


def square(x):
    print("Квадрат числа", x, "равен", x ** 2)

square(4)
square(8)
square(15)
square(23)
square(42)


# -----------------------------------------------------------------------------------------#


""" Функции могут возвращать значения, использую ключевое слово return.  

Вы можете использовать возвращаемое значение, чтобы присвоить его переменной или просто вывести его на экран. """


def sum_two_numbers(a, b):
    return a + b  # возвращаем результат


c = sum_two_numbers(3, 12)  # присвоить результат переменной 'c'


# В последовательности Фибоначчи первые два числа равны 1 и 1, и каждое следующее число равно сумме двух предыдущих.
# Напишите функцию, возвращающую список из чисел Фибоначчи до n.
def fib(n):
    """Возвращает список, содержащий числа Фибоначчи до n"""
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a + b  # обновляем значения a и b
    return result

print(fib(10))

