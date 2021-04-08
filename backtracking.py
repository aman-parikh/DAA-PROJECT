import math
import pygame
from tkinter import messagebox
from tkinter import *
import tkinter

root = tkinter.Tk()
root.withdraw()

class BACKTRACK:

    @staticmethod
    def draw_path(end, start, draw, draw_fin_path):
        node = end
        total_wt = 0
        while node:
            total_wt += node.weight
            if node != start and node != end:
                node.make_path()
            draw()
            node = node.parent

        draw_fin_path()

        messagebox.showinfo('Total weight', total_wt)


    @staticmethod
    def backtracking(draw_bin, draw_fin_path, grid, start, end, row, col, Cellgrid):
        if grid[row][col] == 2:#return condition
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
