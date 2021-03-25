import math
import pygame
from queue import PriorityQueue, deque
from heap import swap, min_heapify, build_min_heap, extract_min_util, extract_min

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
        visited = set()
        visited.add(start)
        start.value = 0
        start.parent = None

        while len(nodes) > 0:

            build_min_heap(nodes, len(nodes))

            current_node = nodes[0]

            if current_node is end:
                DIJKSTRA.draw_path(end, start, draw, draw_fin_path)
                end.make_end()
                start.make_start()
                return

            nodes.pop(0)

            for neighbor in current_node.neighbors:

                if neighbor not in visited:
                    if (neighbor.value) > (current_node.value) + 1:
                        neighbor.parent = current_node
                        neighbor.value = current_node.value + 1
                        nodes.append(neighbor)

                    if neighbor == end:
                        DIJKSTRA.draw_path(end, start, draw, draw_fin_path)
                        end.make_end()
                        start.make_start()
                        return

                    neighbor.make_open()
                    visited.add(neighbor)#green
                    draw()

            if current_node != start:
                current_node.make_closed() #red
                draw()

        return