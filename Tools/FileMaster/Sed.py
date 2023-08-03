import re


def Content(file_name: str, content: str = None):
    try:
        if content is None:
            with open(file_name, 'r') as file:
                content = file.read()
                return content
        else:
            with open(file_name, 'w') as file:
                file.write(content)
    except FileNotFoundError:
        print("File is not Found.")


def i_insert(match, insert):
    return ''.join([insert, match.group()])


def insert_a(match, insert):
    return ''.join([match.group(), insert])


def s(pattern, replacement, file_name):
    content = Content(file_name)
    new_content = re.sub(pattern, replacement, content)
    Content(file_name, new_content)


def d(pattern, file_name):
    content = Content(file_name)
    new_content = re.sub(pattern, '', content)
    Content(file_name, new_content)


def i(pattern, insert, file_name):
    content = Content(file_name)
    new_content = re.sub(
        pattern, lambda match: i_insert(match, insert), content)
    Content(file_name, new_content)


def a(pattern, insert, file_name):
    content = Content(file_name)
    new_content = re.sub(
        pattern, lambda match: insert_a(match, insert), content)
    Content(file_name, new_content)


def sed(cmd: str, file_name: str):
    cmd_match = re.match(r'^([sdia])/([^/]+)/?([^/]+)?$', cmd)
    if cmd_match:
        cmd_type = cmd_match.group(1)
        cmd_arg1 = cmd_match.group(2)
        cmd_arg2 = cmd_match.group(3)
        if cmd_arg2:
            eval(cmd_type + "('" + cmd_arg1 + "', '" +
                 cmd_arg2 + "', '" + file_name + "')")
        else:
            eval(cmd_type + "('" + cmd_arg1 + "', '" + file_name + "')")
    else:
        print('Command is Error!')


# sed('s/[0-9]+/NUM', 'Tools\FileMaster\File.txt')
# sed('d/NUM', 'Tools\FileMaster\File.txt')
# sed('i/[0-9]+/NUM: ', 'Tools\FileMaster\File.txt')
# sed('a/[0-9]+/ :NUM', 'Tools\FileMaster\File.txt')
