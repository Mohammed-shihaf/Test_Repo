from __future__ import print_function
import unittest
from df.audit_trail_verification import atv_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(atv_case_1('x', True, 1, 3))
