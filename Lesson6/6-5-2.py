import os
import re

# Функция для подсчета количества цифр, суммы и произведения цифр в числе
def analyze_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    num_sum = sum(int(digit) for digit in num_str)
    num_product = 1
    for digit in num_str:
        num_product *= int(digit)
    return num_str, num_digits, num_sum, num_product

# Проверяем наличие файла input.txt в текущей директории
if os.path.exists("PDF_6_5_2_input.txt"):
    try:
        with open("PDF_6_5_2_input.txt", "r") as input_file:
            input_data = input_file.read()
            # Используем регулярное выражение для поиска числа в тексте
            match = re.search(r'\d+', input_data)
            if match:
                input_number = int(match.group())
                result = analyze_number(input_number)
                with open("PDF_6_5_2_output.txt", "w") as output_file:
                    output_file.write(f"Число: {result[0]}\n")
                    output_file.write(f"Количество цифр: {result[1]}\n")
                    output_file.write(f"Сумма цифр: {result[2]}\n")
                    output_file.write(f"Произведение цифр: {result[3]}\n")
            else:
                print("Файл PDF_6_5_2_input.txt не содержит числа.")
                with open("PDF_6_5_2_output.txt", "w") as output_file:
                    output_file.write("Файл PDF_6_5_2_input.txt не содержит числа.")
    except ValueError:
        print("Файл input.txt содержит некорректное число.")
        with open("PDF_6_5_2_output.txt", "w") as output_file:
            output_file.write("Файл PDF_6_5_2_input.txt содержит некорректное число.")
else:
    print("Файл PDF_6_5_2_input.txt не найден в текущей директории.")
    with open("PDF_6_5_2_output.txt", "w") as output_file:
        output_file.write("Файл PDF_6_5_2_input.txt не найден в текущей директории.")
