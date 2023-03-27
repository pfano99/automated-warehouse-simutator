import time
from collections import deque


def determine_neighbor(row: tuple, arr: list) -> list:
    row_size = len(arr)
    col_size = len(arr[0])
    neighbors = list()

    # LEFT
    if row[0] >= 1:
        neighbors.append((row[0] - 1, row[1]))
    # RIGHT
    if row[0] <= row_size - 2:
        neighbors.append((row[0] + 1, row[1]))
    # TOP
    if row[1] >= 1:
        neighbors.append((row[0], row[1] - 1))
    # BOTTOM
    if row[1] <= col_size - 2:
        neighbors.append((row[0], row[1] + 1))

    return neighbors


def bfs(start: tuple, target: tuple, graph: list) -> list:
    visited = list()
    parent = dict()
    search_queue = deque()

    search_queue.append(start)
    found = False
    parent[start] = None
    while search_queue:
        searched = search_queue.popleft()
        if not searched in visited:
            if target == searched:
                found = True
                break
            time.sleep(0.01)

            neighbors = determine_neighbor(searched, graph)
            for neighbor in neighbors:
                if not neighbor in visited:
                    parent[neighbor] = searched
                if graph[neighbor[0]][neighbor[1]].grid_type != 10:
                    search_queue.append(neighbor)
            visited.append(searched)
            graph[searched[0]][searched[1]].status = False

    path = []
    if found:
        path.append(target)
        while parent[target] is not None:
            path.append(parent[target])
            target = parent[target]

        path.reverse()
    return path
