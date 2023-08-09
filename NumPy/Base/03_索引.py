import numpy as np

# 单个元素索引
x = np.arange(10)
# 一维与正常数组无异

# 二维
x.shape = (2, 5)
print(x[1, 3])
# 若使用一维的方法索引二维数组，则返回子维数组
print(x[0])

# 索引数组
# NumPy数组可以使用其他数组进行索引，除元组之外
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])
print(x[np.array([[1, 1], [2, 3]])])

# 索引多维数组
y = np.arange(35).reshape(5, 7)
print(y)
# 索引数组具有相同的形状
# (0,0) (2,1) (4,2)
print(y[np.array([0, 2, 4]), np.array([0, 1, 2])])
# 索引数组的形状不同，尝试将它们广播为相同的形状
print(y[np.array([0, 2, 4]), 1])
print(y[np.array([0, 2, 4])])

# 布尔或“掩码”索引数组
b = y > 20
print(y[b])

x = np.arange(30).reshape(2, 3, 5)
print(x)
b = np.array([[True, True, False], [False, True, True]])
print(x[b])

# 将索引数组与切片组合
print(y)
# np.array([0, 2, 4]) 指定要选择的行 0，2，4
# 1:3 指定要选择的列 1，2 包含前，不包含后
x = y[np.array([0, 2, 4]), 1:3]
print(x)

print(y)
b = y > 20
print(b)
x = y[b[:, 5], 1:3]
print(x)

# 结构索引工具
print(y.shape)
# 对数组 y 进行了维度扩展操作，将二维扩充为三维
print(y[:, np.newaxis, :].shape)

x = np.arange(5)
# 利用广播机制自动扩展数组的维度
x = x[:, np.newaxis] + x[np.newaxis, :]
print(x)

z = np.arange(81).reshape(3, 3, 3, 3)
print(z)
# 省略号语法可用于选择剩余的未指定维度
print(z[1, ..., 2])

# 为索引数组赋值
x = np.arange(10)
# 分配常量
x[2:7] = 1
print(x)
# 分配与索引大小一致的数组
x[2:7] = np.arange(5)
# 较高类型分配给较低类型会导致赋值更改

# 在程序中处理可变数量的索引
indices = (1, 1, 1, 1)
print(z)
print(z[indices])
# slice() 函数在程序中指定切片
indices = (1, 1, 1, slice(0, 2))
print(z[indices])
# 使用Ellipsis对象通过代码指定省略号
indices = (1, Ellipsis, 1)  # same as [1,...,1]
print(z[indices])
