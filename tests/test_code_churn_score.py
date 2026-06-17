from __future__ import print_function
import unittest
from dp.code_churn_score import ccs_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(ccs_case_1('x', True, 1, 3))
