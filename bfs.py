import math
import pygame
from queue import PriorityQueue, deque

class BFS:

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
    def bfs(draw, draw_fin_path, grid, start, end):
        nodes = deque()
        nodes.appendleft(start)
        visited = set()
        visited.add(start)

        start.parent = None

        while nodes:
            current_node = nodes.popleft()
            if current_node is end:
                BFS.draw_path(end, start, draw, draw_fin_path)
                end.make_end()
                start.make_start()
                return
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbor.parent = current_node
                    if neighbor == end:
                        BFS.draw_path(end, start, draw, draw_fin_path)
                        end.make_end()
                        start.make_start()
                        return
                    neighbor.make_open()
                    nodes.append(neighbor)
                    draw()
            if current_node != start:
                current_node.make_closed()
                draw()
        return