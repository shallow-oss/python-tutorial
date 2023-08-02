import re


def getContent(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File is not Found.")


def saveContent(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("File is not Found.")


def sed(command, file_name):
    command = command.split('/')
    match command[0]:
        case 's' | 'd':
            content = getContent(file_name)
            pattern = command[1].encode("unicode_escape").decode()
            replacement = command[2].encode(
                "unicode_escape").decode() if command[0] == 's' else ''
            new_content = re.sub(pattern, replacement, content)
            saveContent(file_name, new_content)
        case 'i' | 'a':
            content = getContent(file_name)
            pattern = command[1].encode("unicode_escape").decode()
            insert = command[2] + \
                command[1] if command[0] == 'i' else command[1] + command[2]
            insert = insert.encode("unicode_escape").decode()
            new_content = re.sub(pattern, insert, content)
            saveContent(file_name, new_content)
        case _:
            print('输入错误')
            pass


# sed('s/[0-9]/NUM', 'FileMaster\File.txt')
# sed('d/NUM', 'FileMaster\File.txt')
# sed('i/oceen/the ', 'FileMaster\File.txt')
# sed('a/delicous/ meal', 'FileMaster\File.txt')
# sed('ad/pattern/inserted text', 'FileMaster\File.txt')
