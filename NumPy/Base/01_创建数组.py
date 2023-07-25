import numpy as np

# 将 Python 自带的数组对象（列表和元组）转换成NumPy
x = np.array([2, 3, 1, 0])
x = np.array([[1, 2.0], [0, 0], (1+1j, 3.)])

# 创建原生数组
# shape 为元组
# zeros(shape) 将创建一个用指定形状用0填充的数组
x = np.zeros((2, 3))
# ones(shape) 将创建一个用1个值填充的数组
x = np.ones((2, 3))
# arange() 将创建具有有规律递增值的数组，创建的方法与 range() 函数类似
x = np.arange(10)
x = np.arange(2, 10)
x = np.arange(2, 3, 0.1)
# linspace() 将创建具有指定数量元素的数组，并在指定的开始值和结束值之间平均间隔
x = np.linspace(1., 4., 6)
# indices() 将创建一组数组（堆积为一个更高维的数组）
x = np.indices((3, 3, 3))
# eye() 创建一个具有对角线为 1 的单位矩阵
x = np.eye(3)
# random.rand() 创建一个具有随机值的数组，这些值在 0 到 1 之间均匀分
x = np.random.rand(2, 3)
print(x)
