from numpy import newaxis
import numpy as np

# 改变数组的形状
print("改变数组的形状----------------------")
a = np.floor(10*np.random.random((3, 4)))
print(a)
print(a.shape)

# 返回一个修改后的数组，但不会更改原始数组
# a.ravel() 将多维数组展平为一维数组
print(a.ravel())
# a.reshape() 将数组重新调整为指定的形状
print(a.reshape(6, 2))
# a.T 获取数组的转置
print(a.T)

# a.resize((2,6)) 会修改数组本身
# 在 reshape 操作中将 size 指定为-1，则会自动计算其他的 size 大小
print(a.reshape(-1, 2))

# 将不同数组堆叠在一起
print("将不同数组堆叠在一起---------------")
a = np.floor(10*np.random.random((2, 2)))
print(a)
b = np.floor(10*np.random.random((2, 2)))
print(b)
# 延垂直方向堆叠两个或多个数组
print(np.vstack((a, b)))
# 沿水平方向堆叠两个或多个数组
print(np.hstack((a, b)))
# np.column_stack((a, b))
# 与 hstack 类似
# 用于沿列方向堆叠两个或多个一维数组
print(np.column_stack((a, b)))

a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b)))
print(np.hstack((a, b)))
print(a[:, newaxis])

# 将一个数组拆分成几个较小的数组
print("将一个数组拆分成几个较小的数组------------------")
a = np.floor(10*np.random.random((2, 12)))
print(a)
# np.hsplit(a, 3) 用于将数组 a 沿水平方向（列方向）进行拆分
# numpy.hsplit(arr, indices_or_sections)
# indices_or_sections：指定拆分的索引位置或拆分的段数。可以是一个整数，表示要均匀拆分的段数；也可以是一个整数数组，表示要在哪些索引位置进行拆分
print(np.hsplit(a, 4))
print(np.hsplit(a, (3, 4)))
