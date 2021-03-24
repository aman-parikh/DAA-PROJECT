import pygame
import math
import random
from dfs import DFS
from backtracking import BACKTRACK
from dijkstra import DIJKSTRA

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

clock = pygame.time.Clock()

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
        self.parent = None
        self.value = 2**10

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
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

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

def is_prime(n):

    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False

    return True

def make_automated_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)

            n = random.randrange(1, 100)

            if i+j <= n+10:
                spot.color = BLACK

            grid[i].append(spot)

    return grid

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    #clock.tick(60)

    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

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
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def draw_fin_path(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            if spot.color in [BLACK, PURPLE, WHITE, ORANGE, TURQUOISE]:
                spot.draw(win)

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

    if preference['Generation'] == 1:
        grid = make_grid(ROWS, width)

    else:
        grid = make_automated_grid(ROWS, width)

    start = None
    end = None

    startX = starY = 0

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():

            # Close the window
            if event.type == pygame.QUIT:
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
                if start and end:
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    if event.key == pygame.K_d:
                        pygame.display.set_caption('DFS Path Finding algorithm')
                        DFS.dfs(lambda: draw(win, grid, ROWS, width), lambda: draw_fin_path(win, grid, ROWS, width), grid, start, end)
                        return

                    if event.key == pygame.K_b:
                        pygame.display.set_caption('BAKCTRACKING Path Finding algorithm')

                        bin_grid = []

                        for row in grid:
                            temp = []
                            for spot in row:
                                if spot == end:
                                    temp.append(2)
                                elif spot.color == WHITE or spot.color == ORANGE:
                                    temp.append(0)
                                elif spot.color == BLACK:
                                    temp.append(1)
                            bin_grid.append(temp)

                        BACKTRACK.backtracking(lambda: draw_bin(win, bin_grid, grid, ROWS, width, start),
                                               lambda: draw_fin_path(win, grid, ROWS, width),
                                                bin_grid, start, end, startX, startY, grid)
                        BACKTRACK.draw_path(end, start, lambda: draw(win, grid, ROWS, width), lambda: draw_fin_path(win, grid, ROWS, width))
                        return

                    if event.key == pygame.K_k:
                        pygame.display.set_caption('DIJKSTRA Path Finding algorithm')
                        DIJKSTRA.dijkstra(lambda: draw(win, grid, ROWS, width), lambda: draw_fin_path(win, grid, ROWS, width), grid, start, end)
                        return
    pygame.quit()

def call(win, width, preference):
    main(win, width, preference)
    return