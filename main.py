import unittest
from polygon import Triangle


class TriangleTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run(self):
        self.assertEqual(3, Triangle.get_shape(3, 3, 3))
        self.assertEqual(2, Triangle.get_shape(3, 3, 4))
        self.assertEqual(1, Triangle.get_shape(3, 4, 5))
        self.assertEqual(-1, Triangle.get_shape(3, 3, 6))


if __name__ == '__main__':
    unittest.main()
