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
