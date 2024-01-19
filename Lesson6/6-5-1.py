import shapes


def main():
    with open("PDF_6_5_1_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            params = line.strip().split()
            if len(params) == 2:  # Если 2 параметра, то это прямоугольник
                a, b = map(int, params)
                shapes.PrintRectangle(a, b, "PDF_6_5_1_output.txt")
            elif len(params) == 1:  # Если 1 параметр, то это квадрат
                a = int(params[0])
                shapes.PrintSquare(a, "PDF_6_5_1_output.txt")

    print("Фигуры записаны в файл PDF_6_5_1_output.txt")


if __name__ == '__main__':
    main()