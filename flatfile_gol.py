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
import purepy_engine as engine

def grid_from_str(grid_string):
    tmpgrid = grid_string.strip().split('\n')
    # trim header and footer
    tmpgrid = tmpgrid[1:-1]
    # trim side borders
    tmpgrid = [x.strip()[1:-1] for x in tmpgrid]
    
    grid = engine.grid.Grid(len(tmpgrid), len(tmpgrid[0]))
    for coord in grid.itercoords():
        row, col = coord
        if tmpgrid[row][col] == '*':
            grid[coord].live()
        else:
            grid[coord].die()

    return grid

def str_from_grid(grid):
    headerfooter = '+' + '-' * grid.cols + '+'
    token = { True : '*', False : ' ' }
    board = [
        '|' + ''.join([
            token[grid[(row,col)].is_alive()]
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
        grid = engine.grid.Grid(rows, cols)
        if rand:
            engine.randomize(grid)
        with open(filename, 'w') as f:
            f.write(str_from_grid(grid))
        return
    
    with open(filename, 'r') as f:
        grid = grid_from_str(f.read())
    engine.tick(grid)
    with open(filename, 'w') as f:
        f.write(str_from_grid(grid))

if __name__ == '__main__':
    main()
