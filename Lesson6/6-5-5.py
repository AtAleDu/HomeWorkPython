import numpy as np
import random

# Считываем N и M из файла input.txt
with open("PDF_6_5_5_intput.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())

# Считываем K из файла
with open("PDF_6_5_5_intput.txt", "r") as input_file:
    lines = input_file.readlines()
    K = int(lines[-1].split()[-1])

# Генерируем матрицу A размера N x M
matrix_A = np.random.randint(0, 2, size=(N, M))

# Генерируем матрицу B размера M x K
matrix_B = np.random.randint(1, 10, size=(M, K))

# Записываем матрицы A и B в файл output.txt
with open("PDF_6_5_5_output.txt", "w") as output_file:
    output_file.write("Матрица A:\n")
    np.savetxt(output_file, matrix_A, fmt="%d", delimiter=" ")
    output_file.write("\nМатрица B:\n")
    np.savetxt(output_file, matrix_B, fmt="%d", delimiter=" ")

# Вычисляем произведение матриц A и B
matrix_AB = np.dot(matrix_A, matrix_B)

# Записываем произведение в файл output.txt
with open("PDF_6_5_5_output.txt", "a") as output_file:
    output_file.write("\nМатрица A*B:\n")
    np.savetxt(output_file, matrix_AB, fmt="%d", delimiter=" ")

print("Матрицы сгенерированы и результат записан в PDF_6_5_5_output.txt")
