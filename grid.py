class Grid(object):
    """Grid for use in playing the game of life.

Example:
g = Grid(8,8)
g.set_alive(0,0)
g.set_alive(0,1)
g.set_alive(1,0)
g.tick()
print g.is_alive(1,1)
"""
    def __init__(self, rows, cols):
        self._grid = [[False] * cols for r in xrange(rows)]
        self._rows = rows
        self._cols = cols
        self._last_step = None
    
    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def last_step(self):
        return self._last_step

    def is_alive(self, row, col):
        return self._grid[row][col]
    
    def set_alive(self, row, col):
        self._grid[row][col] = True

    def set_dead(self, row, col):
        self._grid[row][col] = False

    def tick(self):
        step = []
        for index in self.iterindexes():
            current_value = self._grid[index[0]][index[1]]
            value = self._next_cell_state(*index)
            if value != current_value:
                step.append((index, value))
                self._grid[index[0]][index[1]] = value
        self._last_step = step

    def _num_alive_neighbors(self, row, col):
        neighbor_indexes = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row,     col - 1),                 (row,     col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
        ]
        alive_neighbors = [
            True
            for n_row, n_col in neighbor_indexes
            if 0 <= n_row < self.rows and 0 <= n_col < self.cols and \
               self.is_alive(n_row, n_col)
        ]
        return len(alive_neighbors)

    def _next_cell_state(self, row, col):
        alive = self.is_alive(row, col)
        alive_neighbors = self._num_alive_neighbors(row, col)
        next_state = (alive and alive_neighbors in [2, 3]) or \
                     (not alive and alive_neighbors == 3)
        return next_state

    def iterindexes(self):
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                yield (row, col)
        raise StopIteration
