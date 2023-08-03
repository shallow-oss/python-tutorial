import re

# /([^/]+|/[^/]+)/?$


commands = ["s/[0-9]+/NUM", "d/(NUM)", "i/Test/I", "a/Test/A"]

for command in commands:
    match = re.match(r'^([sdia])/([^/]+)/?([^/]+)?$', command)
    if match:
        cmd_type = match.group(1)
        cmd_arg1 = match.group(2)
        cmd_arg2 = match.group(3)
        print(f"匹配成功：命令类型：{cmd_type}，命令参数1：{cmd_arg1}，命令参数2：{cmd_arg2}")
    else:
        print(f"不匹配：{command}")
