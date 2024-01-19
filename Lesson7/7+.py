def print_solution(n, path):
    solution = [['' for _ in range(n)] for _ in range(n)]
    for i, (x, y) in enumerate(path):
        solution[x][y] = str(i + 1)
    return solution

def solve_knights_tour(input_file, output_file):
    with open(input_file, 'r') as f:
        line = f.readline().strip()
        parts = line.split(', ')
        M, N, X, Y = [int(part.split('=')[1]) for part in parts]

    board = [[-1 for _ in range(N)] for _ in range(M)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[X - 1][Y - 1] = 1
    path = [(X - 1, Y - 1)]

    def is_valid_move(x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1

    def find_next_move(x, y, board):
        min_moves = float('inf')
        next_x, next_y = -1, -1

        for i in range(8):
            new_x, new_y = x + move_x[i], y + move_y[i]
            if is_valid_move(new_x, new_y, board):
                num_moves = 0
                for j in range(8):
                    check_x, check_y = new_x + move_x[j], new_y + move_y[j]
                    if is_valid_move(check_x, check_y, board):
                        num_moves += 1
                if num_moves < min_moves:
                    min_moves = num_moves
                    next_x, next_y = new_x, new_y

        return next_x, next_y

    for move_number in range(2, M * N + 1):
        x, y = path[-1]
        next_x, next_y = find_next_move(x, y, board)
        if next_x == -1 and next_y == -1:
            print("Маршрут не существует.")
            return
        board[next_x][next_y] = move_number
        path.append((next_x, next_y))

    solution = print_solution(M, path)
    with open(output_file, 'w') as output:
        for row in solution:
            output.write('\t'.join(map(str, row)) + '\n')
    print(f"Маршрут записан в файл '{output_file}'.")

solve_knights_tour('input7hard.txt', 'output7hard.txt')
