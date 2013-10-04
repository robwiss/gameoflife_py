import random
import collections
import itertools

class Cells(collections.MutableSet):

    def __init__(self, iterable=(), dimensions=None):
        self._set = set(iterable)
        self._dimensions = dimensions

    def __contains__(self, item):
        return item in self._set

    def __iter__(self):
        return iter(self._set)

    def __len__(self):
        return len(self._set)
    
    def add(self, item):
        self._set.add(item)

    def discard(self, item):
        self._set.discard(item)

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = dimensions    


def tick(cells):
    if cells.dimensions is not None:
        rows, cols = cells.dimensions
    
    kernel = (-1, 0, 1)
    # for each coordinate bordering each alive cell, figure out how many alive
    # neighbors there are
    neighbors = collections.Counter([
        (row+i,col+j)
        for row,col in cells
        for i in kernel
        for j in kernel
        if cells.dimensions is None or (0 <= row+i < rows and 0 <= col+j < cols)
    ])
    
    for coord, count in neighbors.iteritems():
        if count == 3 or (count == 4 and coord in cells):
            cells.add(coord)
        elif coord in cells:
            cells.remove(coord)

def randomized_cells(dimensions):
    rows, cols = dimensions
    cells = Cells({
        coord
        for coord in itertools.product(xrange(rows), xrange(cols))
        if random.randint(0, 1) == 1
    }, dimensions)

    return cells
