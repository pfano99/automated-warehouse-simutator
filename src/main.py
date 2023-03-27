from collections import deque
from threading import Thread
import logging
import pygame

from blob import Blob, generate_blobs, get_available_packing
from configs import config, grid_colors
from graph import generate_graph
from missons import Order, generate_mission
from path_finding import bfs
from utils import translate_mouse_pos, border_amount

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

COLS = int(config["WINDOW_WIDTH"] / config["BLOB_SIZE"])
ROWS = int(config["WINDOW_HEIGHT"] / config["BLOB_SIZE"])

pygame.init()
screen = pygame.display.set_mode((config["WINDOW_WIDTH"], config["WINDOW_HEIGHT"]))
clock = pygame.time.Clock()
pygame.display.set_caption("automated-warehouse-simulation")

PACKING_SPACES = dict()


def main_game():
    global screen

    missions = deque()

    running = True
    graph = generate_graph(ROWS, COLS, PACKING_SPACES)

    blobs = generate_blobs(config["BLOB_COUNT"], PACKING_SPACES)
    generate_mission(graph, missions)

    logging.info("missions: %s", len(missions))
    logging.info("agents: %s", len(blobs))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(config["FILL_WHITE"])
        generate_mission(graph, missions)

        render_graph(graph, COLS, ROWS)

        res = starter(blobs, missions)
        if res:
            work(res[0], res[1], graph)

        render_agents(blobs)
        pygame.display.flip()

    pygame.quit()


def render_agents(blobs: deque):
    for blob in blobs:
        pygame.draw.rect(screen, blob.color, blob.rect, 0)


def starter(blobs: list, missions: deque) -> tuple:
    if missions:
        for blob in blobs:
            if blob.available:
                return blob, missions.popleft()
    return None


def work(blob: Blob, mission: Order, graph: list):
    if blob.available:
        def handler():
            blob.available = False
            # Goto package
            p1 = translate_mouse_pos((blob.rect.x, blob.rect.y))
            p2 = translate_mouse_pos(mission.to)

            store_path = bfs(p1, p2, graph)
            PACKING_SPACES[(blob.rect.x, blob.rect.y)] = 0  # Setting the packing spot where the blob was to available
            logging.info("Getting package from: {} to {}".format(p1, p2))
            blob.path = store_path
            blob.action(graph)
            # Goto till
            p3 = translate_mouse_pos((blob.rect.x, blob.rect.y))
            p4 = translate_mouse_pos(mission.by)
            logging.info("Delivering package from: {} to {}".format(p3, p4))
            till_path = bfs(p3, p4, graph)
            blob.path = till_path
            blob.action(graph)
            p5 = translate_mouse_pos((blob.rect.x, blob.rect.y))
            packing = get_available_packing(PACKING_SPACES)
            PACKING_SPACES[packing] = 1
            p6 = translate_mouse_pos(packing)
            logging.info("Mission done going to a packing spot: {}".format(p6))
            packing_path = bfs(p5, p6, graph)
            blob.path = packing_path
            blob.action(graph)

            blob.available = True

        Thread(target=handler).start()
    return


def render_graph(graph, rows, cols):
    global screen
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, grid_colors[graph[i][j].grid_type], graph[i][j].rect,
                             border_amount(graph[i][j].grid_type))


if __name__ == '__main__':
    main_game()
