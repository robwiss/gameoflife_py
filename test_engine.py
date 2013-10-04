import unittest
from flatfile_gol import cells_from_str, str_from_cells
import engine

def grids_equal(grid, other_grid):
    if grid.rows != other_grid.rows or grid.cols != other_grid.cols:
        return False
    for coord in grid.itercoords():
        if grid[coord].is_alive() != other_grid[coord].is_alive():
            return False
    return True

class TestGameRules(unittest.TestCase):

    def test_grid(self):
        start = """
+----+
|*   |
|    |
|    |
|    |
+----+
"""
        cells = cells_from_str(start)
        self.assertTrue((0,0) in cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)
    
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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)
    
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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)
    
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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)
    
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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)

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
        cells = cells_from_str(start)
        engine.tick(cells)
        finish_cells = cells_from_str(finish)
        self.assertEqual(cells, finish_cells)
