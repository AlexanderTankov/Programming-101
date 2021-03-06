import unittest

from is_an_bn import is_an_bn


class Is_an_bn_test(unittest.TestCase):

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))
        self.assertFalse(is_an_bn("rado"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))
        self.assertTrue(is_an_bn("aaaaabbbbb"))
if __name__ == '__main__':
    unittest.main()
