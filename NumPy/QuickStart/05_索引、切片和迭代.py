import numpy as np

# 索引、切片和迭代
# 一维
a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])
a[:6:2] = -1000
print(a)
print(a[::-1])
print(a)
for i in a:
    print(i**(1/3.))

# 多维的数组


def f(x, y):
    return 10*x+y


# 基于数组索引来创建数组
"""
np.fromfunction(function, shape, **kwargs)

参数:
function: 一个接受数组索引作为输入并返回相应数组值的函数
shape: 输出数组的形状，元组
**kwargs: 可以传递给函数的额外关键字参数

返回:
numpy.ndarray: 数组元素是函数应用于每个坐标位置。
"""
b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
# 基础按位置索引
# b[行，列]
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3, :])
# 当提供的索引少于轴的数量时，缺失的索引被认为是完整的切片:
print(b[-1])

# 三个点（ ... ）表示产生完整索引元组所需的冒号
c = np.arange(24).reshape(2, 3, 4)
print(c)
print(c[1, ...])
print(c[..., 2])

b = np.fromfunction(f, (5, 4), dtype=int)
# 对多维数组迭代是相对于第一个轴
for row in b:
    print(row)

# 对数组中的每个元素执行操作，可以使用flat属性
for element in b.flat:
    print(element)
