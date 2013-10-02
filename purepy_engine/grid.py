from cell import Cell

class Grid(object):
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = { coord : Cell() for coord in self.itercoords() }
    
    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def __getitem__(self, key):
        if key not in self._grid:
            raise IndexError("%s outside of grid" % key)
        return self._grid[key]
    
    def __setitem__(self, key, value):
        if key[0] < 0 or key[0] >= self.rows or \
           key[1] < 0 or key[1] >= self.cols:
            raise IndexError("%s outside of grid" % key)
        self._grid[key] = value

    def itercoords(self):
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                yield (row, col)
        raise StopIteration
