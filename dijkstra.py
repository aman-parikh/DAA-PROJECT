import math
import pygame
from queue import PriorityQueue, deque
from heapq import heapify, heappush, heappop

class DIJKSTRA:

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
    def dijkstra(draw, draw_fin_path, grid, start, end):
        inf = 10**9

        nodes = list()
        nodes.append(start)
        start.value = 0
        start.parent = None

        while len(nodes) > 0:
            heapify(nodes)
            current_node = nodes[0]

            if current_node is end:
                DIJKSTRA.draw_path(end, start, draw, draw_fin_path)
                end.make_end()
                start.make_start()
                return

            heappop(nodes)

            for neighbor in current_node.neighbors:
                if (neighbor.value) > (current_node.value) + 1:
                    neighbor.parent = current_node
                    neighbor.value = current_node.value + 1
                    nodes.append(neighbor)

                if neighbor is end:
                    DIJKSTRA.draw_path(end, start, draw, draw_fin_path)
                    end.make_end()
                    start.make_start()
                    return

                neighbor.make_open()
                draw()

            if current_node != start:
                current_node.make_closed()
                draw()

        return