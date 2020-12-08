from src.NotesService import NotesService
from src.note import Note
import unittest
from unittest.mock import Mock

class TestNotesService(unittest.TestCase):

    def test_init(self):
        NotesService()

    def setUp(self):
        self.tmp = NotesService()

    def test_add(self):
        self.tmp.notesStorage.add = Mock()
        self.tmp.notesStorage.add.return_value = Note('Aleks', 5.0)
        self.assertEqual(self.tmp.add(Note('Aleks', 5.0)).getName(), 'Aleks')

    def test_add_exception(self):
        self.tmp.notesStorage.add = Mock(side_effect=TypeError('Wrong value type'))
        self.assertRaises(TypeError, self.tmp.add, 1)

    def test_averageOf(self):
        self.tmp.notesStorage.getAllNotesOfName = Mock()
        self.tmp.notesStorage.getAllNotesOfName.return_value = [3.0, 4.0]
        self.assertEqual(self.tmp.averageOf('Maciej'), 3.5)

    def test_averageOfexception(self):
        self.tmp.notesStorage.getAllNotesOfName = Mock(side_effect=TypeError('Wrong Value Type'))
        self.assertRaises(TypeError, self.tmp.averageOf, 3)

    def test_clear(self):
        self.tmp.notesStorage.clear = Mock()
        self.tmp.notesStorage.clear.return_value = True
        self.assertEqual(self.tmp.clear(), True)
