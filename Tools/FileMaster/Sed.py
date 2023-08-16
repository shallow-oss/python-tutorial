import re


class Command:
    def command_s(self, pattern, content, command_content):
        new_content = re.sub(pattern, command_content, content)
        return new_content

    def command_d(self, pattern, content, command_content):
        new_content = re.sub(pattern, '', content)
        return new_content

    def command_i(self, pattern, content, command_content):
        new_content = re.sub(
            pattern, lambda match: i_insert(match, command_content), content)
        return new_content

    def command_a(self, pattern, content, command_content):
        new_content = re.sub(
            pattern, lambda match: insert_a(match, command_content), content)
        return new_content


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
        cmd = Command()
        methods = {
            's': cmd.command_s,
            'd': cmd.command_d,
            'i': cmd.command_i,
            'a': cmd.command_a
        }
        # 读取文件内容
        content = read_file(file_name)
        new_content = methods[command_type](
            pattern=command_pattern, content=content, command_content=command_content)
        write_file(file_name, new_content)
    else:
        print('Command is error!')
