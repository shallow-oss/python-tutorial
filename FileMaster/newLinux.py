import cmd


class FileTerminal(cmd.Cmd):
    # 字符串提示符
    # 当命令行终端等待用户输入时，会显示这个提示符
    prompt = '>> '

    def do_hello(self, arg):
        """Say hello"""
        print(arg)
        print('Hello, world!')

    def do_quit(self, arg):
        """Quit the terminal"""
        return True


if __name__ == '__main__':
    file_terminal = FileTerminal()
    file_terminal.cmdloop()
