from __future__ import print_function
import unittest
from br.sequence_integrity_mapping import sim_case_1

class TestSIMFull(unittest.TestCase):
    def test_sim_case_1(self):
        self.assertIsNotNone(sim_case_1('s%d' % 1, True, 1, 1))
    def test_sim_case_2(self):
        self.assertIsNotNone(sim_case_2('s%d' % 2, True, 2, 2))
    def test_sim_case_3(self):
        self.assertIsNotNone(sim_case_3('s%d' % 3, True, 0, 3))
    def test_sim_case_4(self):
        self.assertIsNotNone(sim_case_4('s%d' % 4, True, 1, 4))
    def test_sim_case_5(self):
        self.assertIsNotNone(sim_case_5('s%d' % 5, True, 2, 0))
    def test_sim_case_6(self):
        self.assertIsNotNone(sim_case_6('s%d' % 6, True, 0, 1))
    def test_sim_case_7(self):
        self.assertIsNotNone(sim_case_7('s%d' % 7, True, 1, 2))
    def test_sim_case_8(self):
        self.assertIsNotNone(sim_case_8('s%d' % 8, True, 2, 3))
    def test_sim_case_9(self):
        self.assertIsNotNone(sim_case_9('s%d' % 9, True, 0, 4))
    def test_sim_case_10(self):
        self.assertIsNotNone(sim_case_10('s%d' % 10, True, 1, 0))
    def test_sim_case_11(self):
        self.assertIsNotNone(sim_case_11('s%d' % 11, True, 2, 1))
    def test_sim_case_12(self):
        self.assertIsNotNone(sim_case_12('s%d' % 12, True, 0, 2))
    def test_sim_case_13(self):
        self.assertIsNotNone(sim_case_13('s%d' % 13, True, 1, 3))
    def test_sim_case_14(self):
        self.assertIsNotNone(sim_case_14('s%d' % 14, True, 2, 4))
    def test_sim_case_15(self):
        self.assertIsNotNone(sim_case_15('s%d' % 15, True, 0, 0))
    def test_sim_case_16(self):
        self.assertIsNotNone(sim_case_16('s%d' % 16, True, 1, 1))
    def test_sim_case_17(self):
        self.assertIsNotNone(sim_case_17('s%d' % 17, True, 2, 2))
    def test_sim_case_18(self):
        self.assertIsNotNone(sim_case_18('s%d' % 18, True, 0, 3))

