from grid import Grid
import random
import pygame
from pygame.gfxdraw import pixel as p
from pygame import Surface as S
import itertools

def main():
    scale = 4

    x, y = 100, 100
    grid = Grid(x, y)
    for index in grid.iterindexes():
        r = random.randint(0, 1)
        if r == 1:
            grid.set_alive(*index)
    white, black = (255, 255, 255), (0, 0, 0)
    color_map = { False : black, True : white }


    def conway_frames():
        while True:
            step = grid.compute_step()
            yield step
            grid.apply_step(step)

    def process_step(step):
        for (x1, y1), value in step:
            for x_add, y_add in itertools.permutations(xrange(4), 2):
                p(screen, x1 * scale + x_add, y1 * scale + y_add, color_map[value])

    pygame.init()
    screen = pygame.display.set_mode((x * scale, y * scale))

    # initial draw
    for (x1,y1) in grid.iterindexes():
        for x_add, y_add in itertools.permutations(xrange(4), 2):
            p(screen, x1 * scale + x_add, y1 * scale + y_add, color_map[grid.is_alive(x1,y1)])

    # game loop
    for step in conway_frames():
        process_step(step)
        pygame.display.flip()
 
if __name__ == "__main__":
    main()
