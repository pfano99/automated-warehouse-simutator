import time

from pygame import Rect
from configs import config


class Blob:
    def __init__(self, position: tuple, color: tuple, size: tuple):
        self.color = color
        self.size = size
        self.rect: Rect = Rect(position[0], position[1], size[0], size[0])
        self.path = list()
        self.order = None
        self.available = True

    def action(self, grid: list):
        """ follow the path """
        for path in self.path:
            _grid = grid[path[0]][path[1]].position
            self.rect.update((_grid[0], _grid[1]), self.size)
            time.sleep(0.5)


def generate_blobs(number: int, packing_spaces: dict) -> list:
    agents = list()
    for i in range(number):
        packing = get_available_packing(packing_spaces)
        agent = Blob(packing, config["BLOB_COLOR"], (config["BLOB_SIZE"], config["BLOB_SIZE"]))
        agents.append(agent)
        packing_spaces[packing] = 1
    return agents


def get_available_packing(packing_spaces) -> tuple:
    for key in packing_spaces.keys():
        if packing_spaces[key] == 0:
            return key
