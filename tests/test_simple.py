# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from unittest.mock import MagicMock
from src.sample.Note import Note


class TestNote(unittest.TestCase):
    def test_note_value_error1(self):
        test_object = MagicMock(return_value=Note)
        test_object.side_effect = Exception
        self.assertRaises(Exception, test_object, '123', 4.0)

    def test_note_value_error2(self):
        test_object = MagicMock(return_value=Note)
        test_object.side_effect = Exception
        self.assertRaises(Exception, test_object, '123', 4)

    def test_note_value_error3(self):
        test_object = MagicMock(return_value=Note)
        test_object.side_effect = Exception
        self.assertRaises(Exception, test_object, None, 4)

    def test_note_value_error4(self):
        test_object = MagicMock(return_value=Note)
        test_object.side_effect = Exception
        self.assertRaises(Exception, test_object, '123', None)


if __name__ == '__main__':
    unittest.main()
