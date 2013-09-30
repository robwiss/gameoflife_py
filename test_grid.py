import unittest
from grid import Grid

class TestNumAliveNeighbors(unittest.TestCase):
    """Tests to verify that the _num_alive_neighbors method works properly
    
Each corner is tested, then an area in the middle of the board is tested.
    """
    
    def test_topleft(self):
        g = Grid(4,4)
        self.assertEqual(g._num_alive_neighbors(0,0), 0)
        g.set_alive(0,1)
        self.assertEqual(g._num_alive_neighbors(0,0), 1)
        g.set_alive(1,0)
        self.assertEqual(g._num_alive_neighbors(0,0), 2)
        g.set_alive(1,1)
        self.assertEqual(g._num_alive_neighbors(0,0), 3)
    
    def test_topright(self):
        g = Grid(4,4)
        self.assertEqual(g._num_alive_neighbors(0,3), 0)
        g.set_alive(0,2)
        self.assertEqual(g._num_alive_neighbors(0,3), 1)
        g.set_alive(1,2)
        self.assertEqual(g._num_alive_neighbors(0,3), 2)
        g.set_alive(1,3)
        self.assertEqual(g._num_alive_neighbors(0,3), 3)

    def test_bottomleft(self):
        g = Grid(4,4)
        self.assertEqual(g._num_alive_neighbors(3,0), 0)
        g.set_alive(2,0)
        self.assertEqual(g._num_alive_neighbors(3,0), 1)
        g.set_alive(2,1)
        self.assertEqual(g._num_alive_neighbors(3,0), 2)
        g.set_alive(3,1)
        self.assertEqual(g._num_alive_neighbors(3,0), 3)

    def test_bottomright(self):
        g = Grid(4,4)
        self.assertEqual(g._num_alive_neighbors(3,3), 0)
        g.set_alive(3,2)
        self.assertEqual(g._num_alive_neighbors(3,3), 1)
        g.set_alive(2,2)
        self.assertEqual(g._num_alive_neighbors(3,3), 2)
        g.set_alive(2,3)
        self.assertEqual(g._num_alive_neighbors(3,3), 3)

    def test_not_edge(self):
        g = Grid(4,4)
        self.assertEqual(g._num_alive_neighbors(1,1), 0)
        g.set_alive(0,0)
        self.assertEqual(g._num_alive_neighbors(1,1), 1)
        g.set_alive(0,1)
        self.assertEqual(g._num_alive_neighbors(1,1), 2)
        g.set_alive(0,2)
        self.assertEqual(g._num_alive_neighbors(1,1), 3)
        g.set_alive(1,0)
        self.assertEqual(g._num_alive_neighbors(1,1), 4)
        g.set_alive(1,2)
        self.assertEqual(g._num_alive_neighbors(1,1), 5)
        g.set_alive(2,0)
        self.assertEqual(g._num_alive_neighbors(1,1), 6)
        g.set_alive(2,1)
        self.assertEqual(g._num_alive_neighbors(1,1), 7)
        g.set_alive(2,2)
        self.assertEqual(g._num_alive_neighbors(1,1), 8)

class TestNextCellState(unittest.TestCase):
    """Tests to verify that the rules for death and reproduction work"""

    def test_alive_with_less_than_two(self):
        """Any live cell with fewer than two live neighbours dies, as if caused by under-population."""
        g = Grid(4,4)
        g.set_alive(0,0)
        self.assertEqual(g._next_cell_state(0,0), False)
        g.set_alive(0,1)
        self.assertEqual(g._next_cell_state(0,0), False)
    
    def test_alive_with_two_or_three(self):
        """Any live cell with two or three live neighbours lives on to the next generation."""
        g = Grid(4,4)
        g.set_alive(0,0)
        g.set_alive(0,1)
        g.set_alive(1,1)
        self.assertEqual(g._next_cell_state(0,0), True)
        g.set_alive(1,0)
        self.assertEqual(g._next_cell_state(0,0), True)

    def test_alive_with_more_than_three(self):
        """Any live cell with more than three live neighbours dies, as if by overcrowding."""
        g = Grid(4,4)
        g.set_alive(1,1)
        g.set_alive(0,0)
        g.set_alive(0,1)
        g.set_alive(0,2)
        g.set_alive(1,0)
        self.assertEqual(g._next_cell_state(1,1), False)
        g.set_alive(1,2)
        self.assertEqual(g._next_cell_state(1,1), False)
        g.set_alive(2,0)
        self.assertEqual(g._next_cell_state(1,1), False)
        g.set_alive(2,1)
        self.assertEqual(g._next_cell_state(1,1), False)
        g.set_alive(2,2)
        self.assertEqual(g._next_cell_state(1,1), False)

    def test_dead_with_three(self):
        """Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction."""
        g = Grid(4,4)
        g.set_alive(0,0)
        g.set_alive(0,1)
        g.set_alive(1,0)
        self.assertEqual(g._next_cell_state(1,1), True)

