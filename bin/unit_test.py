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
