import math
import pygame
from queue import PriorityQueue, deque

class DFS:

    @staticmethod
    def draw_path(end, start, draw, draw_fin_path):
        node = end
        while node:
            if node != start and node != end:
                node.make_path()
            draw()
            node = node.parent

        draw_fin_path()

    @staticmethod
    def dfs(draw, draw_fin_path, grid, start, end):
        nodes = deque()
        nodes.appendleft(start)
        visited = set()
        visited.add(start)

        start.parent = None

        while nodes:
            current_node = nodes.popleft()
            if current_node is end:
                DFS.draw_path(end, start, draw, draw_fin_path)
                end.make_end()
                start.make_start()
                return
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbor.parent = current_node
                    if neighbor == end:
                        DFS.draw_path(end, start, draw, draw_fin_path)
                        end.make_end()
                        start.make_start()
                        return
                    neighbor.make_open()
                    nodes.appendleft(neighbor)
                    draw()
            if current_node != start:
                current_node.make_closed()
                draw()
        return