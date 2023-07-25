import numpy as np

# 通过常规 Python 的列表或元组推导，得到 NumPy 的数组
# 列表
a = np.array([2, 3, 4])
print(a)
# dtype 数据类型对象
print(a.dtype)
# 元组
b = np.array((1.2, 3.5, 5.1))
print(b)
print(b.dtype)

# 调用 array 的时候传入多个数字参数的创建数组的方式是错误的，需要传入列表或元组
# a = np.array(1, 2, 3, 4)    # WRONG

# 创建数组时可以显式的指定数组的数据类型
# np.array(列表或元组, dtype=数据类型)
# 常见数据类型 bool int64 uint64 float64 complex
c = np.array([[1, 0], [3, 4]], dtype=bool)
print(c)

# 通常数组的元素最初是未知的，大小则是已知的
# NumPy 提供了创建具有初始占位符内容的数组，默认情况下，创建的数组的 dtype 是 float64 类型的。
# 函数 zeros() 创建一个由0组成的数组
zero = np.zeros((3, 4))
print(zero)

# 函数 ones() 创建一个由1组成的数组
one = np.ones((2, 3, 4), dtype=np.int64)
print(one)

# 函数 empty () 创建一个的数组,其初始内容是随机的，取决于内存的状态,
empty = np.empty((2, 3))
print(empty)

# 创建数字组成的数组
# NumPy 提供了一个类似于 range 的函数，该函数返回数组而不是列表。
range1 = np.arange(10, 30, 5)
print(range1)

# linspace 函数用于接收我们需要的元素数量，而不是使用步长
# np.linspace(start, end, number)
linspace = np.linspace(0, 2, 9)
print(linspace)
