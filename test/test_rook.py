import unittest
from game.rook import Rook

class TestRook(unittest.TestCase):

    def test_horizontal_or_vertical(self):
        # Test horizontal movement
        self.assertEqual(Rook.horizontal_or_vertical(0, 0, 0, 5), "horizontal")
        # Test vertical movement
        self.assertEqual(Rook.horizontal_or_vertical(0, 0, 5, 0), "vertical")
        # Test invalid movement (diagonal)
        self.assertEqual(Rook.horizontal_or_vertical(0, 0, 5, 5), "invalid")

    def test_is_valid_movement(self):
        # Test valid horizontal movement
        self.assertTrue(Rook.is_valid_movement("horizontal"))
        # Test valid vertical movement
        self.assertTrue(Rook.is_valid_movement("vertical"))
        # Test invalid movement
        self.assertFalse(Rook.is_valid_movement("invalid"))

if __name__ == '__main__':
    unittest.main()