import unittest
from unittest.mock import mock_open, patch
from src.sample.File import File


class TestFile(unittest.TestCase):
    def test_read_file(self):
        content_of_mock = 'test data'
        with patch("builtins.open", mock_open(read_data="test data")) as mock_file:
            self.assertEqual(File('/path.txt').read_file(), content_of_mock)
            mock_file.assert_called_with('/path.txt', 'r')

    def test_write_file(self):
        content_of_mock = 'some data'
        with patch("builtins.open", mock_open(read_data="test_data")) as mock_file:
            File('path.txt').write_file(content_of_mock)
            mock_file.assert_called_with('path.txt', 'w')
            mock_file().write.assert_called_once_with(content_of_mock)

    @patch('os.path.isfile')
    def test_delete_not_existing_file(self, mock_isfile):
        with self.assertRaises(Exception):
            File('path.txt').delete_file()

    @patch('os.path.isfile')
    @patch('os.remove')
    def test_delete_existing_file(self, mock_isfile, mock_remove):
        mock_isfile.return_value = False
        File('/fake/file/path.txt').delete_file()
        mock_remove.assert_called_with('/fake/file/path.txt')

