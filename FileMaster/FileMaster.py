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


def list_curr_path(path):
    # 获取当前目录
    current_dir = path
    # 获取当前目录下的所有项（文件和文件夹）
    items = os.listdir(current_dir)
    # 过滤出文件和文件夹
    folders = [item for item in items if os.path.isdir(
        os.path.join(current_dir, item))]
    files = [item for item in items if os.path.isfile(
        os.path.join(current_dir, item))]

    return folders, files


def FileMaster():
    display_menu()
    path = os.getcwd()
    while True:
        control = input("请输入选项：")
        match control:
            case '1':
                folders, files = list_curr_path(path)
                print(f"当前位于 {path} 路径下")
                print(f"当前路径下有 {' '.join(folder for folder in folders)} 目录")
                print(f"当前路径下有 {' '.join(file for file in files)} 文件")
            case '2':
                path = input("请输入目标目录：")
            case '3':
                folder_path = input("将在当前目录下创建文件夹，请输入文件夹名称：")
                os.mkdir(os.path.join(path, folder_path))
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case '0':
                print("退出程序")
                sys.exit()  # 退出程序
            case _:
                print("请重新输入")


if __name__ == "__main__":
    FileMaster()
