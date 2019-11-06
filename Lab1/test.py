import unittest
from grammar_checker import check


class TestMainMethod(unittest.TestCase):
    def test1(self):
        self.assertTrue(check('bcdc'))

    def test2(self):
        self.assertTrue(check('bcdaa'))

    def test3(self):
        self.assertTrue(check('bcdacc'))

    def test4(self):
        self.assertTrue(check('bcdacbcc'))

    def test5(self):
        self.assertTrue(check('bcdacbcaa'))

    def test6(self):
        self.assertFalse(check('abc'))

    def test7(self):
        self.assertFalse(check('BdR'))


if __name__ == '__main__':
    unittest.main()
