import pygame
import math
from queue import PriorityQueue, deque
from tkinter import messagebox
from tkinter import *
import tkinter

root = tkinter.Tk()
root.withdraw()

class ASTAR:

    @staticmethod
    def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def draw_path(came_from, current, start, draw, draw_fin_path):
        total_wt = 0

        while current in came_from:
            total_wt += current.weight
            current = came_from[current]
            if current != start:
                current.make_path()
            draw()

        draw_fin_path()
        messagebox.showinfo('Total weight', total_wt)

    @staticmethod
    def astar(draw, draw_fin_path, grid, start, end):

        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}

        g_score = {spot: float('inf') for row in grid for spot in row}
        g_score[start] = 0
        f_score = {spot: float('inf') for row in grid for spot in row}
        f_score[start] = ASTAR.h(start.get_pos(), end.get_pos())

        open_set_hash = {start}

        while not open_set.empty():

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                ASTAR.draw_path(came_from, current, start, draw, draw_fin_path)
                current.make_end()
                start.make_start()
                break

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + ASTAR.h(neighbor.get_pos(), end.get_pos())

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)

                        if neighbor is not start and neighbor is not end:
                            neighbor.make_open()
                    draw()

            if current != start:
                current.make_closed()
                draw()

        return