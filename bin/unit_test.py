import unittest

from fcts import *
#
#
#
#
#
#
#
#
#
#
#
#
#
#

class TestVectors(unittest.TestCase):
    def test_add(self):
        self.assertEqual(vector_add((1,2,3),(4,5,1)), (5,7,4))
        self.assertEqual(vector_add((0,0,0),(1,2,3)), (1,2,3))
    def test_sub(self):
        self.assertEqual(vector_sub((1,2,3),(4,5,6)), (-3,-3,-3))
        self.assertEqual(vector_sub((0,0,0),(1,2,3)), (-1,-2,-3))

    def test_cross_product(self):
        self.assertEqual(vector_cross_product((1, 2, 3),(4, 5, 6)), (-3, 6, -3))
        self.assertEqual(vector_cross_product((0, 0, 0),(1, 2, 3)), (0, 0, 0))

class MyTestCaseH(unittest.TestCase):
    def test_validate_coord(self):
        vec1 = (1, 2, -3)
        vec2 = (-15, 17, -2)
        vec3 = (0, -6, 6)
        self.assertFalse(validate_coords(vec1))
        self.assertFalse(validate_coords(vec2))
        self.assertTrue(validate_coords(vec3))
        self.assertRaises(TypeError, validate_coords, 2)
        self.assertRaises(TypeError, validate_coords, "a")
        self.assertRaises(TypeError, validate_coords, [1,2,3])
        self.assertRaises(IndexError, validate_coords, (1,2))

    def test_screen_to_board(self):
        self.assertEqual(screen_to_board(5,7,15), (0,2,-2))
        self.assertRaises(TypeError, screen_to_board, "a", 5, 7)
        self.assertRaises(TypeError, screen_to_board, 5, "a", 7)
        self.assertRaises(TypeError, screen_to_board, 5, 5, "a")
        self.assertRaises(TypeError, screen_to_board, 5, 5, ["a", "b"])
        self.assertRaises(TypeError, screen_to_board, 5, 5, ("a", "b"))
        self.assertRaises(TypeError, screen_to_board, 5, 5, {"a": "b"})

    def test_warp(self):
        vec1 = (3,0,-3)
        vec2 = (0, -9, 9)
        self.assertEqual(warp(vec1), vec1)
        self.assertTupleEqual(warp(vec2), (0,2,-2))
        self.assertRaises(TypeError, warp, "a")
        self.assertRaises(TypeError, warp, 5)
        self.assertRaises(TypeError, warp, 5.2)
        self.assertRaises(TypeError, warp, [1,2,4])
        self.assertRaises(TypeError, warp, {"a": 50})

    def test_takes_score(self):
        self.assertEqual(takes_score(2), 200)
        self.assertRaises(TypeError, takes_score, 2.5)
        self.assertRaises(TypeError, takes_score, "a")
        self.assertRaises(TypeError, takes_score, ["a", 55])
        self.assertRaises(TypeError, takes_score, ("a", 55))
        self.assertRaises(TypeError, takes_score, {"a": 55})
        self.assertRaises(ValueError, takes_score, -5)

    def test_pieces_bonus(self):
        self.assertEqual(get_pieces_bonus(10, 3), 51200)
        self.assertRaises(TypeError, get_pieces_bonus, 5.2, 3)
        self.assertRaises(TypeError, get_pieces_bonus, 3.5, 7)
        self.assertRaises(TypeError, get_pieces_bonus, 3, "a")
        self.assertRaises(TypeError, get_pieces_bonus, "a", 3)
        self.assertRaises(ValueError, get_pieces_bonus, -2, 5)
        self.assertRaises(ValueError, get_pieces_bonus, 2, -5)
        self.assertRaises(ValueError, get_pieces_bonus, 0, 5)
        self.assertRaises(TypeError, get_pieces_bonus, [1,2], 3)
        self.assertRaises(TypeError, get_pieces_bonus, (1, 2), 3)
        self.assertRaises(TypeError, get_pieces_bonus, {"a": 0}, 3)

    def test_right_parallel(self):
        self.assertFalse(is_the_right_parallel((-1,2,4), (2,5,7)))
        self.assertFalse(is_the_right_parallel((1, -2, 4), (2, 5, 7)))
        self.assertTrue(is_the_right_parallel((2, 2, -4), (1, 1, -2)))
        self.assertRaises(TypeError, is_the_right_parallel, 7, "a")
        self.assertRaises(TypeError, is_the_right_parallel, [7,5], {"a": 2})
        self.assertRaises(ValueError, is_the_right_parallel, (1,4,7,9), (1,5))
class TestFiles(unittest.TestCase):
    def test_is_file(self):
        pass
    def test_create_file(self):
        pass
    def test_readcsv(self):
        pass

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
