import unittest
import os
import shutil

from unittest.mock import patch
from io import StringIO
from FileMaster import FileTerminal


class FileTerminalTest(unittest.TestCase):
    def setUp(self):
        self.file_terminal = FileTerminal()
        self.path = os.getcwd()
        self.test_environment = os.path.join(
            self.path, 'Tools\FileMaster\TestEnvironment')

    def test_do_pwd(self):
        with patch('FileMaster.FileTerminal.path', new=os.getcwd()), \
                patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.file_terminal.do_pwd(None)
            output = mock_stdout.getvalue().strip()
            expected_output = os.getcwd()
            self.assertEqual(output, expected_output)

    def test_do_ls(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment), \
                patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.file_terminal.do_ls(None)
            output = mock_stdout.getvalue().strip()
            expected_output = "Folder：Folder1 Folder2\nFile：File.txt"
            self.assertEqual(output, expected_output)

    def test_do_cd(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            self.file_terminal.do_cd('Folder1')
            current_dir = self.file_terminal.path
            target_dir = os.path.join(self.test_environment, 'Folder1')
            self.assertEqual(current_dir, target_dir)
            os.chdir(self.path)

    def test_do_mkdir(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            self.file_terminal.do_mkdir('Folder3')
            folder_path = os.path.join(self.test_environment, 'Folder3')
            folder_exist = os.path.exists(folder_path)
            self.assertTrue(folder_exist)
            shutil.rmtree(folder_path)

    def test_do_rm(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            folder_path = os.path.join(self.test_environment, 'Folder3')
            os.makedirs(folder_path)
            self.file_terminal.do_rm(folder_path)
            folder_exist = os.path.exists(folder_path)
            self.assertFalse(folder_exist)

    def test_do_cp(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            folder_path = os.path.join(self.test_environment, 'Folder3')
            os.makedirs(folder_path)
            file_name = os.path.join(self.test_environment, 'File.txt')
            self.file_terminal.do_cp(' '.join((file_name, folder_path)))
            file_exist = os.path.exists(file_name)
            file_cp_exist = os.path.exists(
                os.path.join(folder_path, 'File.txt'))
            self.assertTrue(file_exist, file_cp_exist)
            shutil.rmtree(folder_path)

    def test_do_mv(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            folder_path = os.path.join(self.test_environment, 'Folder3')
            os.makedirs(folder_path)
            file_name = os.path.join(self.test_environment, 'File.txt')
            self.file_terminal.do_mv(' '.join((file_name, folder_path)))
            file_exist = os.path.exists(file_name)
            file_mv_exist = os.path.exists(
                os.path.join(folder_path, 'File.txt'))
            self.assertFalse(file_exist)
            self.assertTrue(file_mv_exist)
            shutil.rmtree(folder_path)

    def test_do_touch(self):
        with patch('FileMaster.FileTerminal.path', new=self.test_environment):
            file1_name = os.path.join(self.test_environment, 'File1.txt')
            file2_name = os.path.join(self.test_environment, 'File2.txt')
            self.file_terminal.do_touch(' '.join((file1_name, file2_name)))
            file1_exist = os.path.exists(file1_name)
            file2_exist = os.path.exists(file2_name)
            self.assertTrue(file1_exist, file2_exist)
            os.remove(file1_name)
            os.remove(file2_name)

    def tearDown(self):
        file_name = 'Tools\FileMaster\TestEnvironment\File.txt'
        with open(file_name, "w") as file:
            pass
        self.file_terminal = None


if __name__ == '__main__':
    unittest.main()
