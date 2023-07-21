# 'X' "X" '''X''' """X""" 可以用于创建字符串
# 如字符串内容中有 ' " 等符号可以使用转义字符，也可选用不同的符号创建字符串
# 反斜杠 \ 用于转义字符
s = 'doesn\'t'
print(s)

s = "doesn't"
print(s)

s = '''X'''
print(s)

s = """X"""
print(s)

# 如果不希望转义成特殊字符，可以在引号前添加 r 使用原始字符串
s = r'C:\some\name'
print('C:\some\name')
print(s)

# 字符串可以包含多行
# 多行字符串使用 """X""" 来创建，如想要编程换行而打印时不想换行则可以使用 \ 来取消换行
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
""")

# 字符串可以使用 + 进行合并，* 进行重复
print(3 * 'un' + 'ium')

# 相邻的两个或多个字符串（引号标注的字符）会自动合并
s = 'Py' 'thon' " hello "
print(s)

# 合并多个变量，或合并变量与字面值，要用 +
prefix = 'Py'
print(prefix + "thon")

# 字符串支持索引 （下标访问），第一个字符的索引是 0
# 索引还支持负数，用负数索引时，从右边开始计数
# 索引越界则会报错
word = 'Python'
print(word[0])
print(word[-1])

# 字符串还支持切片
print(word[0:2])

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""
# 切片索引有默认值
# 省略开始索引时，默认值为0
# 省略结束索引时，默认值为字符串的结尾
print(word[:2])

# s[:i] + s[i:] 总是等于 s
print(word[:2] + word[2:])

# 切片会自动处理越界索引
print(word[42:])

# Python 字符串不能修改,为不可变对象
# 对字符串中某个索引位置进行赋值则会报错
# 如需修改字符串则需要新建
print('J' + word[1:])
print(word[:2] + 'py')

# len() 用于返回字符串的长度
s = 'supercalifragilisticexpialidocious'
print(len(s))