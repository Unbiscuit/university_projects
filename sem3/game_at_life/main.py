import time

import pygame
import numpy as np

col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)


def update(surface, cur, sz, in_progress=False):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]
        col = col_background if cur[r, c] == 0 else col_alive

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            if in_progress:
                col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            if in_progress:
                col = col_alive

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt


def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Game of Life")

    cells = np.zeros((dimy, dimx))
    surface.fill(col_grid)
    update(surface, cells, cellsize)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    running = not running
                    update(surface, cells, cellsize)
                    pygame.display.update()

                if event.key == pygame.K_r:
                    cells = np.random.randint(2, size=(dimy, dimx))
                    update(surface, cells, cellsize)
                    pygame.display.update()

                if event.key == pygame.K_c:
                    cells = np.random.randint(1, size=(dimy, dimx))
                    update(surface, cells, cellsize)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if cells[pos[1] // cellsize, pos[0] // cellsize] == 0:
                    cells[pos[1] // cellsize, pos[0] // cellsize] = 1

                update(surface, cells, cellsize)
                pygame.display.update()
                pygame.event.clear()
                time.sleep(0.01)

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()

                if cells[pos[1] // cellsize, pos[0] // cellsize] == 1:
                    cells[pos[1] // cellsize, pos[0] // cellsize] = 0

                update(surface, cells, cellsize)
                pygame.display.update()
                pygame.event.clear()
                time.sleep(0.01)

        surface.fill(col_grid)

        if running:
            cells = update(surface, cells, cellsize, in_progress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == "__main__":
    main(80, 45, 20)