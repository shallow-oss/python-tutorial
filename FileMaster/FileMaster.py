import cmd
import os
import shutil
import re
from Sed import sed


class FileTerminal(cmd.Cmd):
    # 字符串提示符
    # 当命令行终端等待用户输入时，会显示这个提示符
    prompt = '>> '
    path = os.getcwd()

    def do_pwd(self, arg):
        print(self.path)

    def do_ls(self, arg):
        # 获取当前目录
        current_dir = self.path
        # 获取当前目录下的所有项（文件和文件夹）
        items = os.listdir(current_dir)
        # 过滤出文件和文件夹
        folders = [item for item in items if os.path.isdir(
            os.path.join(current_dir, item))]
        files = [item for item in items if os.path.isfile(
            os.path.join(current_dir, item))]
        # 显示文件夹和文件
        print(f"Folder：{' '.join(folder for folder in folders)}")
        print(f"File：{' '.join(file for file in files)}")

    def do_cd(self, arg):
        try:
            # 改变当前工作目录
            os.chdir(arg)
        except FileNotFoundError:
            print("File Not Found,Please try again!")
        except OSError:
            print("Please try again!")
        else:
            self.path = os.getcwd()

    def do_mkdir(self, arg):
        os.makedirs(os.path.join(self.path, arg))

    def do_rm(self, arg):
        if os.path.isfile(arg):
            # 删除文件
            os.remove(arg)
        elif os.path.isdir(arg):
            # 如果是文件夹，先删除文件夹内的内容，然后删除文件夹本身
            shutil.rmtree(arg)
        else:
            print("Folder or File is not exist.")

    def do_cp(self, args):
        try:
            file_name, directory = args.split()
            shutil.copy(file_name, directory)
        except FileNotFoundError:
            print("File is not Found.")
        except ValueError:
            print("Please try again!")
            print("example: cp FILE DIRECTORY")

    def do_mv(self, args):
        try:
            file_name, directory = args.split()
            shutil.move(file_name, directory)
        except ValueError:
            print("Please try again!")
            print("example: mv FILE DIRECTORY")

    def do_touch(self, args):
        fileNames = args.split()
        for file_name in fileNames:
            if os.path.exists(file_name):
                covered = input("file is exists,Is it covered?[Y/n]")
                if covered.lower() == 'y':
                    file = open(file_name, "w")
                    file.close()
            else:
                file = open(file_name, "w")
                file.close()

    def do_cat(self, arg):
        try:
            with open(arg, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("File is not Found!")

    def do_sed(self, args):
        print(args)
        try:
            command, file_name = args.split()
            sed(command, file_name)
        except ValueError:
            print("Please try again!")
            print("example: sed COMMAND FILE")

    def do_quit(self, arg):
        """退出终端"""
        return True

    def do_help(self, arg):
        if arg:
            # 处理特定命令的帮助信息
            match arg:
                case 'pwd':
                    print("print name of current/working directory.")
                case 'ls':
                    print("list directory contents.")
                case 'cd':
                    print("Change the working directory.")
                    print("    ex: cd DIRECTORY")
                case 'mkdir':
                    print('make directories.')
                    print('    ex: mkdir DIRECTORY')
                case 'rm':
                    print('remove files or directories.')
                    print('    ex: rm FILE')
                case 'cp':
                    print('copy file.')
                    print('    ex: cp FILE DIRECTORY')
                case 'mv':
                    print('move files or directories.')
                    print('    ex: mv FILE DIRECTORY')
                case 'touch':
                    print('create null files.')
                    print('    ex: touch FILE ...')
                case 'cat':
                    print('print file on the standard output.')
                    print('    ex: cat FILE')
                case 'sed':
                    print('txt editor.')
                    print('    ex: sed COMMAND FILE')
                case _:
                    print("Unknown command:", arg)
        else:
            # 显示所有命令的帮助信息
            print("Available commands:")
            print("  pwd  - print name of current/working directory")
            print("  ls - list directory contents")
            print("  cd - Change the working directory")
            print('  mkdir - make directories')
            print('  rm - remove files or directories')
            print('  cp - copy file')
            print('  mv - move files or directories')
            print('  touch - create null files')
            print('  cat - print file on the standard output')
            print('  sed - txt editor')
            print("  quit - Exit the program")


if __name__ == '__main__':
    file_terminal = FileTerminal()
    file_terminal.cmdloop()
