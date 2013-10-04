import random
import collections
import itertools

class Cells(collections.MutableSet):

    def __init__(self, iterable=(), dimensions=None, defaultcolor=(255,255,255)):
        self._dict = { x : defaultcolor for x in iterable }
        self._dimensions = dimensions
        self._defaultcolor = defaultcolor

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return self._dict.iterkeys()

    def __len__(self):
        return len(self._dict)
    
    def add(self, item):
        self._dict[item] = self._defaultcolor

    def discard(self, item):
        if item in self._dict:
            del self._dict[item]

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = dimensions

    def get_color(self, coord):
        return self._dict[coord]

    def set_color(self, coord, color):
        self._dict[coord] = color


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
    
    parent_colors = {
        (row,col) : collections.Counter([
            cells.get_color((row+i, col+j))
            for i in kernel
            for j in kernel
            if (row+i, col+j) in cells
        ])
        for (row,col), count in neighbors.iteritems()
        if (row,col) not in cells and count == 3
    }

    for coord, count in neighbors.iteritems():
        if coord not in cells and count == 3:
            row, col = coord
            cells.add(coord)
            highest_freq = parent_colors[coord].most_common(1)[0][1]
            most_common = [x for x in parent_colors[coord].most_common() if x[1] == highest_freq]
            selected = random.randint(0, len(most_common) - 1)
            cells.set_color(coord, parent_colors[coord].most_common()[selected][0])
        elif coord in cells and count not in [3, 4]:
            cells.remove(coord)

def randomized_cells(dimensions, colors=None):
    rows, cols = dimensions
    cells = Cells({
        coord
        for coord in itertools.product(xrange(rows), xrange(cols))
        if random.randint(0, 1) == 1
    }, dimensions)
    if colors is not None:
        for coord in cells:
            color_idx = random.randint(0, len(colors) - 1)
            color = colors[color_idx]
            cells.set_color(coord, color)

    return cells
