import Factorial    # The code to test
import unittest     # The test framework

class Test_TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.test_factorial(Factorial.factorial(3), 6)
        self.test_factorial(Factorial.factorial(4), 24)
        self.test_factorial(Factorial.factorial(4), 120)

if __name__ == '__main__':
    unittest.main()
