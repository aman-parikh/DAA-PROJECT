import math
import pygame

class BACKTRACK:

    @staticmethod
    def draw_path(end, start, draw, draw_fin_path):
        node = end
        while node:
            if node != start and node != end:
                node.make_path()
            draw()
            node = node.parent
            # print(node.parent)
            # print(node.color)
        draw_fin_path()

    @staticmethod
    def backtracking(draw_bin, draw_fin_path, grid, start, end, row, col, Cellgrid):
        if grid[row][col] == 2:
            return True

        elif grid[row][col] == 0:

            grid[row][col] = 3

            draw_bin()

            #print(row, len(grid))

            if row < len(grid) - 1:
                # Explore path below
                if BACKTRACK.backtracking(draw_bin, draw_fin_path, grid, start, end, row + 1, col, Cellgrid):
                    Cellgrid[row + 1][col].parent = Cellgrid[row][col]
                    return True
            if row > 0:
                # Explore path above
                if BACKTRACK.backtracking(draw_bin, draw_fin_path, grid, start, end, row - 1, col, Cellgrid):
                    Cellgrid[row - 1][col].parent = Cellgrid[row][col]
                    return True
            if col < len(grid[row]) - 1:
                # Explore path to the right
                if BACKTRACK.backtracking(draw_bin, draw_fin_path, grid, start, end, row, col+1, Cellgrid):
                    Cellgrid[row][col + 1].parent = Cellgrid[row][col]
                    return True
            if col > 0:
                # Explore path to the left
                if BACKTRACK.backtracking(draw_bin, draw_fin_path, grid, start, end, row, col - 1, Cellgrid):
                    Cellgrid[row][col - 1].parent = Cellgrid[row][col]
                    return True

            grid[row][col] = 4
            draw_bin()