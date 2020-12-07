import unittest
from src.note import Note

class TestNote(unittest.TestCase):

    def test_set(self):
        Note('maciej', 3.0)

    def test_set_exception1(self):
        self.assertRaises(TypeError, Note, True, 3.0)

    def test_set_exception2(self):
        self.assertRaises(TypeError, Note, 'maciej', 2)

    def test_set_exception3(self):
        self.assertRaises(TypeError, Note, note=2)

    def test_set_exception4(self):
        self.assertRaises(ValueError, Note, '', 2.0)

    def test_set_exception5(self):
        self.assertRaises(ValueError, Note, 'Maciej', 10.0)

    def test_getName(self):
        test = Note('Maciej', 3.0)
        self.assertEqual(test.getName(), 'Maciej')

    def test_getNote(self):
        test = Note('Maciej', 3.0)
        self.assertEqual(test.getNote(), 3.0)

