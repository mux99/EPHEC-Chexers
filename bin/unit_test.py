import unittest

from fcts import *
from file_interaction import *

class MyTestCaseM(unittest.TestCase):
    def test_add(self):
        self.assertEqual(vector_add((1,2,3),(4,5,6)), (5,7,9))
        self.assertEqual(vector_add((0,0),(1,2)), (1,2))
        self.assertEqual(vector_add((),()),())
        self.assertRaises(TypeError ,vector_add,("a","a"),("b","b"))
        self.assertRaises(TypeError, vector_add, 'a', (0,0,0))
        self.assertRaises(TypeError, vector_add, (0,0,0), 'a')
        self.assertRaises(IndexError, vector_add, (0,0,0), (0,0))

    def test_sub(self):
        self.assertEqual(vector_sub((1,2,3),(4,5,6)), (-3,-3,-3))
        self.assertEqual(vector_sub((0,0),(1,2)), (-1,-2))
        self.assertEqual(vector_sub((),()),())
        self.assertRaises(TypeError ,vector_sub,("a","a"),("b","b"))
        self.assertRaises(TypeError, vector_sub, 'a', (0,0,0))
        self.assertRaises(TypeError, vector_sub, (0,0,0), 'a')
        self.assertRaises(IndexError, vector_sub, (0,0,0), (0,0))

    def test_cross_product(self):
        self.assertEqual(vector_cross_product((1, 2, 3),(4, 5, 6)), (-3, 6, -3))
        self.assertEqual(vector_cross_product((0, 0, 0),(1, 2, 3)), (0, 0, 0))
        self.assertRaises(TypeError ,vector_cross_product,("a","a","a"),("b","b","b"))
        self.assertRaises(TypeError, vector_cross_product, 'a', (0,0,0))
        self.assertRaises(TypeError, vector_cross_product, (0,0,0), 'a')
        self.assertRaises(IndexError, vector_cross_product, (0,0,0), (0,0))
        self.assertRaises(IndexError, vector_cross_product, (0,0), (0,0))
        self.assertRaises(IndexError, vector_cross_product, (), ())


    def test_is_file(self):
        outfile_path = "testtesttest.test"
        try:
            self.assertFalse(is_file(outfile_path))
            open(outfile_path, 'w')
            self.assertTrue(is_file(outfile_path))
        finally:
            os.remove(outfile_path)
        self.assertRaises(TypeError,4)
        self.assertRaises(TypeError,["p","a","t","h"])

    def test_create_file(self):
        outfile_path = "testtesttest.test"
        try:
            self.assertFalse(is_file(outfile_path))
            create_file(outfile_path)
            self.assertTrue(is_file(outfile_path))
        finally:
            os.remove(outfile_path)
        self.assertRaises(TypeError,4)
        self.assertRaises(TypeError,["p","a","t","h"])

class MyTestCaseH(unittest.TestCase):
    def test_validate_coord(self):
        vec1 = (1, 2, -3)
        vec2 = (-15, 17, -2)
        vec3 = (0, -6, 6)
        self.assertTrue(validate_coords(vec1))
        self.assertFalse(validate_coords(vec2))
        self.assertTrue(validate_coords(vec3))
        self.assertRaises(TypeError, validate_coords, 2)
        self.assertRaises(TypeError, validate_coords, "a")
        self.assertRaises(TypeError, validate_coords, [1,2,3])
        self.assertRaises(IndexError, validate_coords, (1,2))

    def test_screen_to_board(self):
        self.assertEqual(screen_to_board(5, 7, 15), (0, 2, -2))
        self.assertRaises(TypeError, screen_to_board, "a", 5, 7)
        self.assertRaises(TypeError, screen_to_board, 5, "a", 7)
        self.assertRaises(TypeError, screen_to_board, 5, 5, "a")
        self.assertRaises(TypeError, screen_to_board, 5, 5, ["a", "b"])
        self.assertRaises(TypeError, screen_to_board, 5, 5, ("a", "b"))
        self.assertRaises(TypeError, screen_to_board, 5, 5, {"a": "b"})

    def test_warp(self):
        vec1 = (3, 0, -3)
        vec2 = (0, -9, 9)
        self.assertEqual(warp(vec1), vec1)
        self.assertTupleEqual(warp(vec2), (0, 2, -2))
        self.assertRaises(TypeError, warp, "a")
        self.assertRaises(TypeError, warp, 5)
        self.assertRaises(TypeError, warp, 5.2)
        self.assertRaises(TypeError, warp, [1, 2, 4])
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
        self.assertRaises(TypeError, get_pieces_bonus, [1, 2], 3)
        self.assertRaises(TypeError, get_pieces_bonus, (1, 2), 3)
        self.assertRaises(TypeError, get_pieces_bonus, {"a": 0}, 3)

    def test_right_parallel(self):
        self.assertFalse(is_the_right_parallel((-1, 2, 4), (2, 5, 7)))
        self.assertFalse(is_the_right_parallel((1, -2, 4), (2, 5, 7)))
        self.assertTrue(is_the_right_parallel((2, 2, -4), (1, 1, -2)))
        self.assertRaises(TypeError, is_the_right_parallel, 7, "a")
        self.assertRaises(TypeError, is_the_right_parallel, [7,5], {"a": 2})
        self.assertRaises(ValueError, is_the_right_parallel, (1,4,7,9), (1,5))
        self.assertRaises(TypeError, is_the_right_parallel, [7, 5], {"a": 2})
        self.assertRaises(ValueError, is_the_right_parallel, (1, 4, 7, 9), (1, 5))


class MyTestCaseJ(unittest.TestCase):
    def test_other_player(self):
        self.assertEqual(other_player("black"), "white")
        self.assertEqual(other_player("white"), "black")
        self.assertRaises(ValueError, other_player, "steve")
        self.assertRaises(TypeError, other_player, 42)
        self.assertRaises(TypeError, other_player, None)
        self.assertRaises(TypeError, other_player, [1, 2, 3])

    def test_board_to_screen(self):
        self.assertEqual(board_to_screen(0, 0, 1), (2, 0))
        self.assertEqual(board_to_screen(7, 0, 4), (-3, 23))
        self.assertRaises(ValueError, board_to_screen, 0, 0, 0)
        self.assertRaises(TypeError, board_to_screen, 'a', 0, 0)
        self.assertRaises(TypeError, board_to_screen, 0, 'a', 0)
        self.assertRaises(TypeError, board_to_screen, 0, 0, 'a')

    def test_get_starting_pos(self):
        self.assertEqual(get_starting_pos("white"), [(0, 0, 0), (1, 0, -1), (0, -1, 1), (1, -1, 0), (0, -2, 2), (1, -2, 1), (0, -3, 3), (1, -3, 2), (0, -4, 4), (1, -4, 3), (0, -5, 5), (1, -5, 4), (0, -6, 6), (1, -6, 5), (0, -7, 7), (1, -7, 6)])
        self.assertEqual(get_starting_pos("black"), [(6, -3, -3), (7, -3, -4), (6, -4, -2), (7, -4, -3), (6, -5, -1), (7, -5, -2), (6, -6, 0), (7, -6, -1), (6, -7, 1), (7, -7, 0), (6, -8, 2), (7, -8, 1), (6, -9, 3), (7, -9, 2), (6, -10, 4), (7, -10, 3)])
        self.assertRaises(ValueError, get_starting_pos, "steve")
        self.assertRaises(TypeError, get_starting_pos, 42)
        self.assertRaises(TypeError, get_starting_pos, None)
        self.assertRaises(TypeError, get_starting_pos, [1, 2, 3])


    def test_get_starting_pos_test(self):
        self.assertEqual(get_starting_pos_test("white"), [(4, -5, 1)])
        self.assertEqual(get_starting_pos_test("black"), [(4, -4, 0), (4, -6, 2), (5, -5, 0), (5, -6, 1), (3, -4, 1), (3, -5, 2), (2, -6, 4), (5, -8, 3), (2, -2, 0), (3, -2, -1), (3, -7, 4), (6, -8, 2), (1, -3, 2), (1, -4, 3), (5, -3, -2), (6, -4, -2)])
        self.assertRaises(ValueError, get_starting_pos_test, "steve")
        self.assertRaises(TypeError, get_starting_pos_test, 42)
        self.assertRaises(TypeError, get_starting_pos_test, None)
        self.assertRaises(TypeError, get_starting_pos_test, [1, 2, 3])

    def test_get_starting_pos_test2(self):
        self.assertEqual(get_starting_pos_test2("white"), [(4, -5, 1)])
        self.assertEqual(get_starting_pos_test2("black"), [(6, -6, 0)])
        self.assertRaises(ValueError, get_starting_pos_test2, "steve")
        self.assertRaises(TypeError, get_starting_pos_test2, 42)
        self.assertRaises(TypeError, get_starting_pos_test2, None)
        self.assertRaises(TypeError, get_starting_pos_test2, [1, 2, 3])

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
