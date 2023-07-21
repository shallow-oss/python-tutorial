# 列表可以包含不同类型的元素
squares = [1, 4, 9, 16, 25]
print(squares)

# 列表也支持索引和切片
# 切片操作返回包含请求元素的新列表
print(squares[0])

print(squares[-3:])

# 列表的合并操作
print(squares + [36, 49, 64, 81, 100])

# 列表的元素可以进行改变
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)

# append() 方法 可以在列表结尾添加新元素
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# 为切片赋值可以改变列表大小
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

# len()函数也支持列表，返回列表的长度
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)