from pygame import Rect
from configs import config


class Grid:
    def __init__(self, position: tuple, grid_type: str, size: tuple):
        self.grid_type: int = grid_type
        self.position: tuple = position
        self.rect: Rect = Rect(position[0], position[1], size[0], size[0])


def generate_graph(rows: int, cols: int, packing_spaces: dict):
    graph = list()
    for i in range(rows):
        graph.append(list())
        for j in range(cols):
            pos_x = (config["WINDOW_WIDTH"] / cols) * j
            pos_y = (config["WINDOW_HEIGHT"] / rows) * i
            size_x = config["WINDOW_WIDTH"] / cols
            size_y = config["WINDOW_HEIGHT"] / rows
            graph[i].append(
                Grid((pos_x, pos_y), 2, (size_x, size_y))
            )
    add_borders(graph)
    add_storage_section(graph)
    add_checkout_session(graph)
    add_blob_packing_session(graph, packing_spaces)
    return graph


def add_borders(graph: list):
    col_size = len(graph[0])
    row_size = len(graph)
    for i in range(4, row_size - 4):
        for j in range(1, col_size - 1):
            if j % 2 == 0:
                graph[i][j].grid_type = 10


def add_storage_section(graph: list):
    col_size = len(graph[0])

    for j in range(1, col_size - 1):
        if j % 2 == 0:
            graph[0][j].grid_type = 11


def add_blob_packing_session(graph: list, packing_spaces: dict):
    for i in range(4, len(graph) - 4):
        if i % 2 == 0:
            graph[i][0].grid_type = 14
            graph[i][len(graph[i]) - 1].grid_type = 14
            packing_spaces[graph[i][0].position] = 0  # zero for available and one for taken
            packing_spaces[graph[i][len(graph[i]) - 1].position] = 0  # zero for available and one for taken


def add_checkout_session(graph: list):
    col_size = len(graph[0])
    row_size = len(graph)
    for j in range(1, col_size - 1):
        if j % 2 == 0:
            graph[row_size - 1][j].grid_type = 12
