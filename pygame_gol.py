import purepy_engine as engine
import pygame
from pygame.gfxdraw import pixel as p
from pygame import Surface as S
import itertools

def main():
    scale = 4

    x, y = 100, 100
    grid = engine.grid.Grid(x, y)
    engine.randomize(grid)
    white, black = (255, 255, 255), (0, 0, 0)
    color_map = { False : black, True : white }

    def conway_frames():
        while True:
            changes = engine.tick(grid)
            yield changes

    def process_changes(changes):
        for (x1, y1), value in changes:
            for x_add, y_add in itertools.permutations(xrange(4), 2):
                p(screen, x1 * scale + x_add, y1 * scale + y_add, color_map[value])

    pygame.init()
    screen = pygame.display.set_mode((x * scale, y * scale))

    # initial draw
    for (x1,y1) in grid.itercoords():
        for x_add, y_add in itertools.permutations(xrange(4), 2):
            p(screen, x1 * scale + x_add, y1 * scale + y_add, color_map[grid[(x1,y1)].is_alive()])

    # game loop
    for changes in conway_frames():
        process_changes(changes)
        pygame.display.flip()
 
if __name__ == "__main__":
    main()
