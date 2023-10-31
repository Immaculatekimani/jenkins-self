import unittest
from check import checking


class Testing(unittest.TestCase):
    def test_presence(self):
        self.assertTrue(checking("./remi.sh"))
    
    def test_absence(self):
        self.assertFalse(checking("sue.sh"))


#this is the main area
if __name__ == '__main__':
    unittest.main