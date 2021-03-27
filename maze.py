import pygame
import math
import random
from dfs import DFS
from backtracking import BACKTRACK
from dijkstra import DIJKSTRA
from bfs import BFS
from astar import ASTAR
from tkinter import messagebox
from tkinter import *
import tkinter

root = tkinter.Tk()
root.withdraw()
pygame.init()

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
BROWN = (165, 42, 42)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

font2 = pygame.font.SysFont('arial', 10, bold=True)

clock = pygame.time.Clock()

class Spot:
    def __init__(self, row, col, width, total_rows, choice):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
        self.parent = None
        self.value = 2**10
        if choice == 1:
            self.weight = random.randrange(2, 100)
        else:
            self.weight = 1

    def get_pos(self):
        return self.row, self.col

    def is_not_visited(self):
        return self.color == WHITE

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == BROWN

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = BROWN

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        text = font2.render(str(self.weight), True, BLACK)
        win.blit(text, (self.x, self.y))

    def draw_fin(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        text = font2.render(str(self.weight), True, BLACK)
        win.blit(text, (self.x, self.y))

    def draw_weight(self, win):
        text = font2.render(str(self.weight), True, BLACK)
        win.blit(text, (self.x, self.y))

    def update_neighbors(self, grid):
        self.neighbors = []

        # Lower square
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Upper Square
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Right Square
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Left Sqaure
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

def make_grid(rows, width, choice):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows, choice)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width, x):
    clock.tick(x)

    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw_fin(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def draw_bin(win, bin_grid, grid, rows, width, start):
    win.fill(WHITE)

    for i in range(len(bin_grid)):
        for j in range(len(bin_grid[i])):
            if grid[i][j] == start:
                continue
            elif bin_grid[i][j] == 0:
                grid[i][j].color = WHITE
            elif bin_grid[i][j] == 1:
                grid[i][j].color = BLACK
            elif bin_grid[i][j] == 2:
                grid[i][j].color = TURQUOISE
            elif bin_grid[i][j] == 3:
                grid[i][j].make_open()
            elif bin_grid[i][j] == 4:
                grid[i][j].make_closed()

    for row in grid:
        for spot in row:
            spot.draw_fin(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def draw_fin_path(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            if spot.color in [RED, GREEN] and spot.color is not PURPLE:
                spot.color = WHITE

            if spot.color in [BLACK, PURPLE, WHITE, BROWN, TURQUOISE]:
                spot.draw_fin(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width, preference):
    ROWS = 30
    x = 60

    grid = make_grid(ROWS, width, preference['Generation'])

    if preference['Speed'] == 1:
        x = 10
    elif preference['Speed'] == 2:
        x = 30
    elif preference['Speed'] == 3:
        x = 100

    start = None
    end = None

    startX = starY = 0

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width, x)
        for event in pygame.event.get():

            # Close the window
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if started:
                continue
                # Left Mouse Click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    startX = row
                    startY = col
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pygame.quit()
                    run = False
                    break

                if start and end:
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    if event.key == pygame.K_s:

                        if preference['Algo'] == 1:
                            pygame.display.set_caption('BFS Path Finding algorithm')
                            BFS.bfs(lambda: draw(win, grid, ROWS, width, x),
                                    lambda: draw_fin_path(win, grid, ROWS, width), grid, start, end)
                            return

                        if preference['Algo'] == 2:
                            pygame.display.set_caption('BAKCTRACKING Path Finding algorithm')

                            bin_grid = []

                            for row in grid:
                                temp = []
                                for spot in row:
                                    if spot == end:
                                        temp.append(2)
                                    elif spot.color == WHITE or spot.color == BROWN:
                                        temp.append(0)
                                    elif spot.color == BLACK:
                                        temp.append(1)
                                bin_grid.append(temp)

                            BACKTRACK.backtracking(lambda: draw_bin(win, bin_grid, grid, ROWS, width, start),
                                                   lambda: draw_fin_path(win, grid, ROWS, width),
                                                    bin_grid, start, end, startX, startY, grid)
                            BACKTRACK.draw_path(end, start, lambda: draw(win, grid, ROWS, width, x), lambda: draw_fin_path(win, grid, ROWS, width))
                            return

                        if preference['Algo'] == 3:
                            pygame.display.set_caption('DIJKSTRA Path Finding algorithm')
                            DIJKSTRA.dijkstra(lambda: draw(win, grid, ROWS, width, x), lambda: draw_fin_path(win, grid, ROWS, width), grid, start, end)
                            return

                        if preference['Algo'] == 4:
                            pygame.display.set_caption('A* Path Finding algorithm')
                            ASTAR.astar(lambda: draw(win, grid, ROWS, width, x), lambda: draw_fin_path(win, grid, ROWS, width), grid, start, end)
                            return

    pygame.quit()

def call(win, width, preference):
    main(win, width, preference)
    return