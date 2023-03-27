import math
from configs import config


def translate_mouse_pos(pos: tuple) -> tuple:
    x, y = 0, 0
    if pos[0] < config["BLOB_SIZE"]:
        x = 0
    else:
        x = math.floor(pos[0] / config["BLOB_SIZE"])
    if pos[1] < config["BLOB_SIZE"]:
        y = 0
    else:
        y = math.floor(pos[1] / config["BLOB_SIZE"])
    return y, x


def border_amount(_type: int) -> int:
    match _type:
        case 2:
            return 1
    return 0


def draw_path(path: list, graph: list):
    for p in path[1:-1]:
        graph[p[0]][p[1]].grid_type = 3
