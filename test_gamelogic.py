import unittest
from flatfile_gol import grid_from_str, str_from_grid
import purepy_engine as engine

def grids_equal(grid, other_grid):
    if grid.rows != other_grid.rows or grid.cols != other_grid.cols:
        return False
    for coord in grid.itercoords():
        if grid[coord].is_alive() != other_grid[coord].is_alive():
            return False
    return True

class TestGameRules(unittest.TestCase):

    def test_no_neighbors(self):
        start = """
+----+
|*   |
|    |
|    |
|    |
+----+
"""
        finish = """
+----+
|    |
|    |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))
    
    def test_one_neighbor(self):
        start = """
+----+
|*   |
|*   |
|    |
|    |
+----+
"""
        finish = """
+----+
|    |
|    |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))
    
    def test_two_neighbors(self):
        start = """
+----+
|**  |
|*   |
|    |
|    |
+----+
"""
        finish = """
+----+
|**  |
|**  |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_three_neighbors(self):
        start = """
+----+
|**  |
|**  |
|    |
|    |
+----+
"""
        finish = """
+----+
|**  |
|**  |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_four_neighbors(self):
        start = """
+----+
|*** |
|**  |
|    |
|    |
+----+
"""
        finish = """
+----+
|* * |
|* * |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))
    
    def test_five_neighbors(self):
        start = """
+----+
|*** |
|*** |
|    |
|    |
+----+
"""
        finish = """
+----+
|* * |
|* * |
| *  |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_six_neighbors(self):
        start = """
+----+
|*** |
|*** |
|*   |
|    |
+----+
"""
        finish = """
+----+
|* * |
|  * |
|*   |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))
    
    def test_seven_neighbors(self):
        start = """
+----+
|*** |
|*** |
|*   |
|    |
+----+
"""
        finish = """
+----+
|* * |
|  * |
|*   |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_seven_neighbors(self):
        start = """
+----+
|*** |
|*** |
|**  |
|    |
+----+
"""
        finish = """
+----+
|* * |
|    |
|* * |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_eight_neighbors(self):
        start = """
+----+
|*** |
|*** |
|*** |
|    |
+----+
"""
        finish = """
+----+
|* * |
|   *|
|* * |
| *  |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

class TestEdges(unittest.TestCase):
    
    def test_topleft(self):
        start = """
+----+
|**  |
|*   |
|    |
|    |
+----+
"""
        finish = """
+----+
|**  |
|**  |
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_topright(self):
        start = """
+----+
|  **|
|   *|
|    |
|    |
+----+
"""
        finish = """
+----+
|  **|
|  **|
|    |
|    |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_bottomleft(self):
        start = """
+----+
|    |
|    |
|*   |
|**  |
+----+
"""
        finish = """
+----+
|    |
|    |
|**  |
|**  |
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))

    def test_bottomright(self):
        start = """
+----+
|    |
|    |
|   *|
|  **|
+----+
"""
        finish = """
+----+
|    |
|    |
|  **|
|  **|
+----+
"""
        start_grid = grid_from_str(start)
        engine.tick(start_grid)
        finish_grid = grid_from_str(finish)
        self.assertTrue(grids_equal(start_grid, finish_grid))