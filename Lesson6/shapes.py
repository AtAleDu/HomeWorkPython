def PrintRectangle(a, b, file):
    with open(file, 'w') as f:
        for i in range(a):
            if i == 0 or i == a - 1:
                f.write('* ' * b + '\n')
            else:
                f.write('*' + '  ' * (b - 2) + ' *\n')


def PrintSquare(a, file):
    with open(file, 'w') as f:
        for i in range(a):
            if i == 0 or i == a - 1:
                f.write('* ' * a + '\n')
            else:
                f.write('*' + '  ' * (a - 2) + ' *\n')
