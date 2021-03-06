import unittest

from is_increasing import is_increasing


class Is_increasing_test(unittest.TestCase):

    def test_is_increasing(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))
        self.assertTrue(is_increasing([1]))
        self.assertFalse(is_increasing([5, 6, -10]))
        self.assertFalse(is_increasing([1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
