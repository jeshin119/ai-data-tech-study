import LeapYear
import unittest

class TestLeapYear(unittest.TestCase):
    def test_2020(self):
        r=LeapYear.is_leap_year(2020)
        self.asserEtEqual(r, True)

if __name__=='__main__':
    unittest.main