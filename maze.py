import math
import pygame

# Colors for various types of cells
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

class Cell:

    def __init__(self, row, col, x, y, total_rows, total_cols):
        self.row = row
        self.col = col
        self.x = row * x
        self.y = col * y
        self.color = WHITE
        self.width = y
        self.height = x
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.parent = None

    def get_pos(self):
        return self.row, self.col

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

    def make_end(self):
        self.color = GREEN

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = PURPLE

    def draw_cell(self, win):
        pygame.draw.rect(win, self.color, (self.row, self.col, self.width, self.height))

    def update_neighbours(self, grid):

        self.neighbours = []

        #upper cell
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbours.append(grid[self.row-1][self.col])

        #below cell
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbours.append(grid[self.row+1][self.col])

        #left cell
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbours.append(grid[self.row][self.col-1])

        #right cell
        if self.col < self.total_cols - 1 and grid[self.row][self.col+1].is_barrier():
            self.neighbours.append(grid[self.row][self.col+1])


def make_grid(rows, width, columns, height):
    grid = []

    gapC = width // columns
    gapR = height // rows

    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(Cell(i, j, gapR, gapC, rows, columns))

        grid.append(temp)

    return grid

def draw_grid(win, grid, width, height, rows, columns):
    gapC = width // columns
    gapR = height // rows

    for i in range(rows+1):
        pygame.draw.line(win, GREY, (0, i*gapR), (width, i*gapR))
        
        for j in range(columns+1):
            pygame.draw.line(win, GREY, (j*gapC, 0), (j*gapC, height))

    pygame.display.update()

def draw(win, grid, width, height, rows, columns):
    win.fill(WHITE)

    for row in grid:
        for cell in row:
            cell.draw_cell(win)

    draw_grid(win, grid, width, height, rows, columns)


