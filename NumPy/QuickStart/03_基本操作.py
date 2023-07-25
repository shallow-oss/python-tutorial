from math import pi
import numpy as np

# 基本操作
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
# 数量相同才可进行操作
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a < 35)

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
# * 在NumPy中是按照对应元素进行 * 运算，与一般矩阵乘法不同
print(A*B)
# 矩阵乘积可以使用@运算符或dot函数或方法执行
# @
print(A @ B)
# A.dot(B)
print(A.dot(B))
print(B.dot(A))

# 某些操作(+= *=)会更直接更改被操作的矩阵数组而不会创建新矩阵数组
a = np.ones((2, 3), dtype=int)
# np.random.random 0-1 随机数创建
b = np.random.random((2, 3))
print(b)
a *= 3
print(a)
b += a
print(b)
# dtype 不匹配
# a += b

# 当使用不同类型的数组进行操作时，结果数组的类型对应于更一般或更精确的数组
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype)
c = a+b
print(c)
print(c.dtype)
d = np.exp(c*1j)
print(d)
print(d.dtype)

# 许多一元操作，例如计算数组中所有元素的总和，都是作为ndarray类的方法实现的
a = np.random.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())

# 指定axis 参数,沿数组的指定轴应用操作
b = np.arange(12).reshape(3, 4)
print(b)
# axis = 1表示横轴，方向从左到右；axis = 0表示纵轴，方向从上到下
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b.min(axis=1))
# 计算沿指定轴的数组元素的累积和
# 结果数组的形状与输入数组相同
print(b.cumsum(axis=0))
