# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = 9.0

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
print(int(float_number))
stroka = "234"
char = 'q'
integer = 1
double = 3.2
print("_______________________________________________________________")

print(type(stroka))
print(type(char))
print(type(integer))
print(type(double))

print("_______________________________________________________________")

print(int(float_number))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

print(int(stroka))
print(float(double))
str(str(integer))
