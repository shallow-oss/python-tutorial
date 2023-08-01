'''
use for GitHub520 project auto flush
'''


import subprocess
import requests


def get_host_content(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


# get host file
url = "https://raw.fastgit.org/521xueweihan/GitHub520/main/hosts"
host_content = get_host_content(url)

host_file_path = r'C:\Windows\System32\drivers\etc\hosts'

# del old hosts
del_start_marker = "# GitHub520 Host Start"
del_end_marker = "# GitHub520 Host End"

# read host content
with open(host_file_path, 'r') as file:
    lines = file.readlines()

# find start and end marker
start_line = None
end_line = None
for i, line in enumerate(lines):
    if line.strip() == del_start_marker:
        start_line = i
    elif line.strip() == del_end_marker:
        end_line = i

# del old
if start_line is not None and end_line is not None:
    del lines[start_line:end_line+1]

# save host
# write new host
with open(host_file_path, 'w') as file:
    file.writelines(lines)
    file.write(host_content)

print("内容已成功写入host文件。")


# 执行 ipconfig /flushdns 命令
subprocess.run(['ipconfig', '/flushdns'], capture_output=True, text=True)

print("DNS缓存已成功刷新。")
