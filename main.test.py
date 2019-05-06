import unittest

from main import rearrange, num_of_ones

class Test(unittest.TestCase):
    def test_case1(self):
        """ Check if rearrange() runs as expected """
        nums = [5, 3, 7, 10, 14]
        n = 5
        self.assertListEqual(rearrange(nums, n), [3,5,10,7,14])
    
    def test_case2(self):
        """ Check if rearrange() runs as expected """
        nums = [1, 2, 3]
        n = 3
        self.assertNotEqual(rearrange(nums, n), [3,2,1])

    def test_case3(self):
        """ Check if nums_of_ones() runs as expected """
        self.assertEqual(num_of_ones(3), 2)

    def test_case4(self):
        """ Check if nums_of_ones() runs as expected """
        self.assertNotEqual(num_of_ones(111), 3)

if __name__ == "__main__":
    unittest.main()