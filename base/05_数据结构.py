# 列表详解
# 初始化列表
from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# list.count(x)
# 返回列表中元素 x 出现的次数
# print()
print(fruits.count('apple'))
print(fruits.count('tangerine'))

# list.index(x[, start[, end]])
# 返回列表中第一个值为 x 的元素的零基索引
# 可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列
# 返回的索引是相对于整个序列的开始计算的，而不是 start 参数
print(fruits.index('banana'))
print(fruits.index('banana', 4))

# list.reverse()
# 翻转列表中的元素
fruits.reverse()
print(fruits)

# list.append(x)
# 在列表末尾添加一个元素 x
fruits.append('grape')
print(fruits)

# list.sort(*, key=None, reverse=False)
# 就地排序列表中的元素，并不是所有数据都可以进行排序
fruits.sort()
print(fruits)

# list.pop([i])
# 删除列表中指定位置的元素，并返回被删除的元素
# 未指定位置时，删除并返回列表的最后一个元素
print(fruits.pop())
print(fruits)

# list.extend(iterable)
# 用可迭代对象的元素扩展列表
fruits.extend(['orange', 'apple'])
print(fruits)

# list.insert(i, x)
# 在指定位置插入元素,第一个参数是插入元素的索引
fruits.insert(2, 'appcl')
print(fruits)

# list.remove(x)
# 从列表中删除第一个值为 x 的元素，未找到时触发异常
fruits.remove('appcl')
print(fruits)

# list.copy()
# 返回列表的浅拷贝
new = fruits.copy()
print(new)

# list.clear()
# 删除列表里的所有元素
new.clear()
print(new)

# 用列表实现堆栈
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

# 用列表实现队列
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
queue.popleft()
print(queue)

# 列表推导式
# 对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列
# 无副作用地计算平方列表
# squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
print(squares)

# 列表推导式的方括号内包含以下内容
# 一个表达式  一个 for 子句 零个或多个 for 或 if 子句
# 结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表

# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)
print(list(zip(*matrix)))

# del 语句
# 按索引从列表中移除元素，而不是值
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# del 从列表中移除切片
del a[2:4]
print(a)
# del 清空整个列表
del a[:]
print(a)

# 元组和序列
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# 元组可以由元组组成
u = t, (1, 2, 3, 4, 5)
print(u)
# 元组是不可变的
# t[0] = 88888
# 元组可以包含可变的数据类型
v = ([1, 2, 3], [3, 2, 1])
print(v)
# 创建空元组
empty = ()
# 创建有一个元素的元组，需要在元素后加逗号
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

# 集合
# 集合是由不重复元素组成的无序容器
# 初始化集合
# 创建空集合只能使用set()
empty = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
# a 有 b 没有
print(a - b)
# a 有 b 也有
print(a | b)
# a b 都有的
print(a & b)
# a b 不共有的
print(a ^ b)

# 字典
# 字典以 关键字 为索引，关键字通常是字符串或数字，也可以是其他任意不可变类型
# 字典的键必须是唯一的
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
# list(字典) 返回该字典中所有键的列表
print(list(tel))
# 排列
sorted(tel)
print(tel)
# 检查字典里是否存在某个键,使用 in
print('guido' in tel)
print('jack' not in tel)
# dict() 构造函数可以直接用键值对序列创建字典
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# 字典推导式可以用任意键值表达式创建字典
{x: x**2 for x in (2, 4, 6)}
# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷
dict(sape=4139, guido=4127, jack=4098)


# 在字典中循环，用 items() 方法可同时取出键和对应的值
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)