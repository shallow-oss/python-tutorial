import re


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("File not found.")


def write_file(file_name: str, content: str) -> None:
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found.")


def i_insert(match: re.match, insert: str) -> str:
    return ''.join([insert, match.group()])


def insert_a(match: re.match, insert: str) -> str:
    return ''.join([match.group(), insert])


def sed(command: str, file_name: str) -> None:
    # 匹配命令
    command_match = re.match(r'^([sdia])/([^/]+)/?([^/]+)?$', command)
    if command_match:
        # 命令模式 匹配规则 内容
        command_type = command_match.group(1)
        command_pattern = command_match.group(2)
        command_content = command_match.group(3)
        # 读取文件内容
        content = read_file(file_name)
        match command_type:
            case 's':
                new_content = re.sub(command_pattern, command_content, content)
            case 'd':
                new_content = re.sub(command_pattern, '', content)
            case 'i':
                new_content = re.sub(
                    command_pattern, lambda match: i_insert(match, command_content), content)
            case 'a':
                new_content = re.sub(
                    command_pattern, lambda match: insert_a(match, command_content), content)
        # 保存新的文件内容
        write_file(file_name, new_content)
    else:
        print('Command is error!')
