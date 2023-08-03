# 复杂的输出格式
# 格式化字符串字面值 
year = 2016
event = 'Referendum'

print(f'Results of the {year} {event}')

# str.format() 方法
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# repr() 或 str() 把值转化为字符串

# 格式化字符串字面值
# 字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# 一些修饰符可以在格式化前转换值
# '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()
animals = "65"
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!a}.')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# 字符串 format() 方法
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

# 关键字参数名引用值
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# 0 代表第 0 个参数
# :d 代表的是十进制格式输出
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

import math
print('The value of pi is approximately %5.3f.' % math.pi)


# 读取文件
# 子句体结束后，文件会正确关闭，即便触发异常也可以
with open('base\\test.txt', encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)