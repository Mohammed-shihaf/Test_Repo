from __future__ import print_function
import unittest
from st.test_case_granularity import tcg_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(tcg_case_1('x', True, 1, 3))
