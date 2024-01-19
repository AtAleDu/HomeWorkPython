import pygame
import sys
import random

def check_win(mas, sign):
    for row in mas:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(mas[row][col] == sign for row in range(3)):
            return True
    if all(mas[i][i] == sign for i in range(3)) or all(mas[i][2 - i] == sign for i in range(3)):
        return True
    return False

def show_winner(player):
    print(f"Игрок {player} выиграл!")

pygame.init()
size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height + size_block + margin)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики - нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_run = True

def draw_board():
    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'x':
                color = red
            elif mas[row][col] == 'o':
                color = green
            else:
                color = white
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == red:
                pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
            elif color == green:
                pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)

draw_board()

while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if 0 <= row < 3 and 0 <= col < 3 and mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                    if check_win(mas, 'x'):
                        show_winner('X')
                        game_run = False
                else:
                    mas[row][col] = 'o'
                    if check_win(mas, 'o'):
                        show_winner('O')
                        game_run = False
                query += 1
        elif event.type == pygame.MOUSEBUTTONUP:
            # Добавь здесь код для обработки нажатия кнопки "Игра с компьютером"
            pass

    draw_board()
    pygame.display.update()
