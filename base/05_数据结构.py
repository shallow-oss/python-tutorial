# 列表详解
# 初始化列表
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
fruits.insert(2,'appcl')
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
from collections import deque
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


# 5.1.3