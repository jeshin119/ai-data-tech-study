import LeapYear
import unittest

class TestLeapYear(unittest.TestCase):
    def test_2020(self):
        r = LeapYear.is_leap_year(2020)
        self.assertEqual(r, True)

class TestLeapYearFalse(unittest.TestCase):
    def test_1900(self):
        r = LeapYear.is_leap_year(1900)
        self.assertEqual(r, False)

if __name__=='__main__':
    unittest.main()