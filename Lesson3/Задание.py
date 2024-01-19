N = int(input("Введите целое число от 2 до 9: "))

top = N * '``@..@   '
middle1 = N * '`(_____) '
middle2 = N * '(>____<) '
bottom = N * '^^~~~~^^ '

print(top,middle1,middle2,bottom, sep = '\n')
