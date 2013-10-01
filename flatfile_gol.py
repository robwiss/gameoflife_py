"""Flat file Game of Life

Usage:
  flatfile_gol.py [--empty=<ROWxCOL> | --rand=<ROWxCOL>] <filename>
  flatfile_gol.py (-h | --help)

Options:
  -h --help          Show this screen
  --empty=<ROWxCOL>  Initialize filename with an empty game board of size ROW x
                     COL. E.g. "8x8"
  --rand=<ROWxCOL>   Initialize filename with a randomized game board of size
                     ROW x COL. E.g. "8x8"
"""

from docopt import docopt
from grid import Grid
import random

def grid_from_str(grid_string):
    tmpgrid = grid_string.strip().split('\n')
    # trim header and footer
    tmpgrid = tmpgrid[1:-1]
    # trim side borders
    tmpgrid = [x.strip()[1:-1] for x in tmpgrid]
    
    grid = Grid(len(tmpgrid), len(tmpgrid[0]))
    for row, col in grid.iterindexes():
        if tmpgrid[row][col] == '*':
            grid.set_alive(row, col)
        else:
            grid.set_dead(row, col)

    return grid

def str_from_grid(grid):
    headerfooter = '+' + '-' * grid.cols + '+'
    token = { True : '*', False : ' ' }
    board = [
        '|' + ''.join([
            token[grid.is_alive(row,col)]
            for col in xrange(grid.cols)
        ]) + '|'
        for row in xrange(grid.rows)
    ]
    board.insert(0, headerfooter)
    board.append(headerfooter)
    return '\n'.join(board)

def main():
    arguments = docopt(__doc__)
    filename = arguments['<filename>']
    empty = arguments['--empty'] is not None
    rand = arguments['--rand'] is not None
    dimensions = None
    if empty:
        dimensions = arguments['--empty']
    if rand:
        dimensions = arguments['--rand']
    if dimensions is not None:
        dim = dimensions.split('x')
        rows = int(dim[0])
        cols = int(dim[1])
        grid = Grid(rows, cols)
        if rand:
            for index in grid.iterindexes():
                r = random.randint(0, 1)
                if r == 1:
                    grid.set_alive(*index)
        with open(filename, 'w') as f:
            f.write(str_from_grid(grid))
        return
    
    with open(filename, 'r') as f:
        grid = grid_from_str(f.read())
    grid.tick()
    with open(filename, 'w') as f:
        f.write(str_from_grid(grid))

if __name__ == '__main__':
    main()
