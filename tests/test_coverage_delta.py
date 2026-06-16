from __future__ import print_function
import unittest
from cd.coverage_delta import code_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(code_case_1('x', True, 1, 3))
