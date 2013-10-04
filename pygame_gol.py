import engine
import pygame
from pygame.gfxdraw import pixel as p
from pygame import Surface as S
import itertools

def main():
    scale = 4

    x, y = 100, 100
    cells = engine.randomized_cells((x,y))
    white, black = (255, 255, 255), (0, 0, 0)

    def process_living(cells):
        for (x1, y1) in cells:
            for x_add, y_add in itertools.permutations(xrange(4), 2):
                p(screen, x1 * scale + x_add, y1 * scale + y_add, white)

    pygame.init()
    screen = pygame.display.set_mode((x * scale, y * scale))

    # game loop
    while True:
        pygame.display.flip()
        pygame.display.get_surface().fill(black)
        process_living(cells)
        engine.tick(cells)
 
if __name__ == "__main__":
    main()
