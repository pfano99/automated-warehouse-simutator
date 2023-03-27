import random
from collections import deque


class Order:
    def __init__(self, by: tuple, to: tuple, product: str, priority):
        self.by = by
        self.to = to
        self.product = product
        self.priority = priority


def generate_mission(graph: list, mission: deque):
    storage = list()
    tills = list()

    random.seed()
    gen = random.randint(1, 20)
    if gen > 10:
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j].grid_type == 11:
                    storage.append(graph[i][j].position)
                elif graph[i][j].grid_type == 12:
                    tills.append(graph[i][j].position)

        random.seed()
        to = storage[random.randint(0, len(storage) - 1)]
        random.seed()
        by = tills[random.randint(0, len(tills) - 1)]
        order = Order(by, to, "test", 1)
        mission.append(order)
