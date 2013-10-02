import random

def tick(grid):
    changes = []
    for coord in grid.itercoords():
        current_value = grid[coord].is_alive()
        value = _next_cell_state(grid, coord)
        if value != current_value:
            changes.append((coord, value))
    for coord, value in changes:
        if value:
            grid[coord].live()
        else:
            grid[coord].die()
    return changes

def randomize(grid):
    for coord in grid.itercoords():
        if random.randint(0, 1) == 1:
            grid[coord].live()
        else:
            grid[coord].die()

def _num_alive_neighbors(grid, coord):
    row, col = coord
    neighbor_coords = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row,     col - 1),                 (row,     col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
    ]
    alive_neighbors = [
        True
        for n_row, n_col in neighbor_coords
        if 0 <= n_row < grid.rows and 0 <= n_col < grid.cols and \
           grid[(n_row, n_col)].is_alive()
    ]
    return len(alive_neighbors)

def _next_cell_state(grid, coord):
    alive = grid[coord].is_alive()
    alive_neighbors = _num_alive_neighbors(grid, coord)
    next_state = (alive and alive_neighbors in [2, 3]) or \
                 (not alive and alive_neighbors == 3)
    return next_state
