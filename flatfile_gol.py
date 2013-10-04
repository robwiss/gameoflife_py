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
import engine

def cells_from_str(cells_string):
    tmpcells = cells_string.strip().split('\n')
    # trim header and footer
    tmpcells = tmpcells[1:-1]
    # trim side borders
    tmpcells = [x.strip()[1:-1] for x in tmpcells]

    dimensions = (len(tmpcells), len(tmpcells[0]))
    
    cells = engine.Cells({
        (row,col)
        for row, line in enumerate(tmpcells)
        for col, value in enumerate(line)
        if value == '*'
    }, dimensions)

    return cells

def str_from_cells(cells):
    rows, cols = cells.dimensions
    headerfooter = '+' + '-' * cols + '+'
    token = { True : '*', False : ' ' }
    board = [
        '|' + ''.join([
            token[(row,col) in cells]
            for col in xrange(cols)
        ]) + '|'
        for row in xrange(rows)
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
        dimensions = [int(x) for x in dimensions.split('x')]
        if rand:
            cells = engine.randomized_cells(dimensions)
        else:
            cells = Cells(dimensions=dimensions)
        with open(filename, 'w') as f:
            f.write(str_from_cells(cells))
        return
    
    with open(filename, 'r') as f:
        cells = cells_from_str(f.read())
    engine.tick(cells)
    with open(filename, 'w') as f:
        f.write(str_from_cells(cells))

if __name__ == '__main__':
    main()
