import unittest
import a_chop
import b_chop
import c_chop
import d_chop
import e_chop

def cheating(query, subject):
    try:
        return subject.index(query)
    except ValueError:
        return -1

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.chop = cheating

    def test_1(self):
        self.assertEqual(-1, self.chop(3, []))
        self.assertEqual(-1, self.chop(3, [1]))
        self.assertEqual(0,  self.chop(1, [1]))
    def test_2(self):
        self.assertEqual(0,  self.chop(1, [1, 3, 5]))
        self.assertEqual(1,  self.chop(3, [1, 3, 5]))
        self.assertEqual(2,  self.chop(5, [1, 3, 5]))
        self.assertEqual(-1, self.chop(0, [1, 3, 5]))
        self.assertEqual(-1, self.chop(2, [1, 3, 5]))
        self.assertEqual(-1, self.chop(4, [1, 3, 5]))
        self.assertEqual(-1, self.chop(6, [1, 3, 5]))
    def test_3(self):
        self.assertEqual(0,  self.chop(1, [1, 3, 5, 7]))
        self.assertEqual(1,  self.chop(3, [1, 3, 5, 7]))
        self.assertEqual(2,  self.chop(5, [1, 3, 5, 7]))
        self.assertEqual(3,  self.chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, self.chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, self.chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, self.chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, self.chop(6, [1, 3, 5, 7]))
    def test_4(self):
        self.assertEqual(2,  self.chop(5, [1, 3, 5, 7, 10, 15, 22, 32, 47, 69, 72, 94, 103]))

class MethodATest(BaseTest):
    def setUp(self):
        self.chop = a_chop.chop

class MethodBTest(BaseTest):
    def setUp(self):
        self.chop = b_chop.chop

class MethodCTest(BaseTest):
    def setUp(self):
        self.chop = c_chop.chop

class MethodDTest(BaseTest):
    def setUp(self):
        self.chop = d_chop.chop

class MethodETest(BaseTest):
    def setUp(self):
        self.chop = e_chop.chop
