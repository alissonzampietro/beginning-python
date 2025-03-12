import unittest
from modules.calc_area import square

## Here we're going to talk about a util topic in the software world: Unit Testing.
# Unit Testing is a process of testing a small part of the code.
# And in python we don't need to install any extra lib to do it
# It comes with the unittest library incorporated
# In this case, we're going to test the function 'sum'.

# class TestSum(unittest.TestCase):
#     def test_sum(self):
#         self.assertEqual(calc_area.square(2,3), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()

print(calc_area.square(2,2))