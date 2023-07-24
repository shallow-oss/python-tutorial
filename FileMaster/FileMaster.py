import cmd
import os
import shutil


class FileTerminal(cmd.Cmd):
    # 字符串提示符
    # 当命令行终端等待用户输入时，会显示这个提示符
    prompt = '>> '
    path = os.getcwd()

    def do_pwd(self, arg):
        path = self.path
        print(path)

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
        print(f"Folder：{' '.join(folder for folder in folders)}")
        print(f"File：{' '.join(file for file in files)}")

    def do_cd(self, arg):
        try:
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
            os.remove(arg)
        elif os.path.isdir(arg):
            # 如果是文件夹，先删除文件夹内的内容，然后删除文件夹本身
            shutil.rmtree(arg)
        else:
            print("Folder or File is not exist.")

    def do_cp(self, args):
        file_name, directory = args.split()
        try:
            shutil.copy(file_name, directory)
        except FileNotFoundError:
            print("File is not Found.")

    def do_quit(self, arg):
        """退出终端"""
        return True

    def do_help(self, arg):
        if arg:
            # 处理特定命令的帮助信息
            if arg == "pwd":
                print("print name of current/working directory.")
            elif arg == "ls":
                print("list directory contents.")
            elif arg == "cd":
                print("Change the working directory.")
            elif arg == 'mkdir':
                print('make directories.')
            elif arg == 'rm':
                print('remove files or directories.')
            else:
                print("Unknown command:", arg)
        else:
            # 显示所有命令的帮助信息
            print("Available commands:")
            print("  pwd  - print name of current/working directory")
            print("  ls - list directory contents")
            print("  cd - Change the working directory")
            print('  mkdir - make directories')
            print('  rm - remove files or directories')
            print("  quit - Exit the program")


if __name__ == '__main__':
    file_terminal = FileTerminal()
    file_terminal.cmdloop()
