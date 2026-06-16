from __future__ import print_function
import unittest
from pc.automated_quality_enforcement import aqe_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(aqe_case_1('x', True, 1, 3))
