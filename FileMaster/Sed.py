def sed(command, file_mame):
    try:
        command = command.split('/')
        match command[0]:
            case 's':
                print('替换匹配的字符串')
                pass
            case 'd':
                print('删除匹配的行')
                pass
            case 'i':
                print('匹配行前追加文本')
                pass
            case 'a':
                print('匹配行后追加文本')
                pass
            case _:
                print('输入错误')
                pass
    except FileNotFoundError:
        print("File is not Found.")


sed('s/old/new', 'file.txt')
sed('d/pattern', 'file.txt')
sed('i/pattern/inserted text', 'file.txt')
sed('a/pattern/inserted text', 'file.txt')
sed('ad/pattern/inserted text', 'file.txt')
