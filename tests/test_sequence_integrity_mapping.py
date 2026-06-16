from __future__ import print_function
import unittest
from br.sequence_integrity_mapping import sim_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(sim_case_1('x', True, 1, 3))
