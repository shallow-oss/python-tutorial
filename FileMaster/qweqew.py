import re

pattern = r'went'  # 匹配字母 "d"
text = 'went'

result = re.sub(pattern, r'Xd', text)
print(result)
