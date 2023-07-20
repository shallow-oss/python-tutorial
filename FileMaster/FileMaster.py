import os
import sys


def display_menu():
    print("------------FileMaster------------")
    print("\t[1] 显示当前目录")
    print("\t[2] 切换目录")
    print("\t[3] 创建文件夹")
    print("\t[4] 创建文件")
    print("\t[5] 复制文件/文件夹")
    print("\t[6] 移动文件/文件夹")
    print("\t[7] 删除文件/文件夹")
    print("\t[8] 重命名文件/文件夹")
    print("\t[9] 显示帮助")
    print("\t[0] 退出程序")


def list_curr_path():
    return os.getcwd(), os.listdir()


def FileMaster():
    display_menu()
    while True:
        control = input("请输入选项：")
        match control:
            case '1':
                curPath, files = list_curr_path()
                list_str = ','.join(str(file) for file in files)
                print(f"当前位于{curPath}")
                print(f"当前文件夹下有 {list_str} 文件")
            case '9':
                display_menu()
            case '0':
                print("退出程序")
                sys.exit()  # 退出程序
            case _:
                print("请重新输入")


if __name__ == "__main__":
    FileMaster()
