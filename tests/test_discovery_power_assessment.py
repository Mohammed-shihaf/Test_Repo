from __future__ import print_function
import unittest
from cd.discovery_power_assessment import dpa_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(dpa_case_1('x', True, 1, 3))
