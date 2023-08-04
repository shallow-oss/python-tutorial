import unittest
from unittest.mock import patch
from io import StringIO
from FileMaster import FileTerminal
import os


class FileTerminalTest(unittest.TestCase):
    def setUp(self):
        self.file_terminal = FileTerminal()
        self.path = 'Tools\FileMaster\TestEnvironment'

    def test_pwd(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.file_terminal.do_pwd('')
            output = fake_out.getvalue().strip()
            expected_output = os.getcwd()
            self.assertEqual(output, expected_output)

    def test_do_ls(self):
        with patch('FileMaster.FileTerminal.path', new=self.path), \
                patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.file_terminal.do_ls(None)
            output = mock_stdout.getvalue().strip()
            expected_output = "Folder：Folder1 Folder2\nFile：File.txt"
            self.assertEqual(output, expected_output)

    def tearDown(self):
        self.file_terminal = None


if __name__ == '__main__':
    unittest.main()
