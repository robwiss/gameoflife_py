import engine_color as engine
import pygame
from pygame.gfxdraw import pixel as p
import itertools
import time

def main():
    scale = 5
    sleep_interval = 0

    x, y = 200, 200
    colors = [
        (0,   14,  255),
        (12,  232, 146),
        (250, 255, 0),
        (232, 115, 12),
        (255, 13,  226),
    ]

    cells = engine.randomized_cells((x,y), colors)
    gray10 = (0x1a, 0x1a, 0x1a)

    def process_living(cells):
        for (x1, y1) in cells:
            for x_add, y_add in itertools.permutations(xrange(scale), 2):
                p(screen, x1 * scale + x_add, y1 * scale + y_add, cells.get_color((x1,y1)))

    pygame.init()
    screen = pygame.display.set_mode((x * scale, y * scale))

    # game loop
    while True:
        pygame.display.flip()
        pygame.display.get_surface().fill(gray10)
        process_living(cells)
        engine.tick(cells)
        time.sleep(sleep_interval)
 
if __name__ == "__main__":
    main()
