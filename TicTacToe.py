import pygame
import sys
import random
import time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((480, 480))
piece_size = 80
img_x = pygame.image.load('x.png')
img_empty = pygame.image.load('empty.png')
img_o = pygame.image.load('o.png')
grid = [['', '', ''], ['', '', ''], ['', '', '']]
wins = [[(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]]

pygame.display.set_caption('TicTacToe')

img_empty = pygame.transform.scale(img_empty, (160, 160))
img_o = pygame.transform.scale(img_o, (160, 160))
img_x = pygame.transform.scale(img_x, (160, 160))

turn = 'x'
player = ''

if random.randint(0, 1) == 0:
    player = 'o'
else:
    player = ''

font = pygame.font.SysFont(None, 200)
font_img = font.render('', True, (0, 1, 0))


def get_random_field():
    global turn, grid
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if grid[x][y] == '':
        grid[x][y] = turn
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    else:
        get_random_field()


while True:
    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for x in range(3):
        for y in range(3):
            if grid[x][y] == '':
                screen.blit(img_empty, (x*160, y*160))
            if grid[x][y] == 'o':
                screen.blit(img_o, (x*160, y*160))
            if grid[x][y] == 'x':
                screen.blit(img_x, (x*160, y*160))

    x = 0
    y = 0

    if player == turn:
        for i in grid:
            for ii in i:
                if ii == '':
                    if mx in range(x+8, x+151):
                        if my in range(y+8, y+151):
                            if pygame.mouse.get_pressed() == (True, False, False):
                                grid[int(x/160)][int(y/160)] = turn
                                # print(str(grid))
                                if turn == 'x':
                                    turn = 'o'
                                else:
                                    turn = 'x'
                y += 160
            x += 160
            y = 0
    else:
        t = random.random() / 2
        time.sleep(t)
        get_random_field()

    # name = turn

    won = (
           (grid[0][0] == turn and
            grid[1][0] == turn and
            grid[2][0] == turn) or  # across the bottom
           (grid[0][1] == turn and
            grid[1][1] == turn and
            grid[2][1] == turn) or  # across the middle
           (grid[0][2] == turn and
            grid[1][2] == turn and
            grid[2][2] == turn) or  # across the top
           (grid[0][0] == turn and
            grid[0][1] == turn and
            grid[0][2] == turn) or  # down the left side
           (grid[1][0] == turn and
            grid[1][1] == turn and
            grid[1][2] == turn) or  # down the middle
           (grid[2][0] == turn and
            grid[2][1] == turn and
            grid[2][2] == turn) or  # down the right side
           (grid[0][0] == turn and
            grid[1][1] == turn and
            grid[2][2] == turn) or  # diagonal /
           (grid[0][2] == turn and
            grid[1][1] == turn and
            grid[2][0] == turn))

    if won:
        font_img = font.render(turn + ' won', True, (100, 255, 100))
        screen.blit(font_img, (50, 150))

    death = 0

    for i in grid:
        for ii in i:
            if ii != '':
                death += 1

    if death == 8:
        font_img = font.render('no one won', True, (100, 255, 100))
        screen.blit(font_img, (50, 150))

    pygame.display.update()
