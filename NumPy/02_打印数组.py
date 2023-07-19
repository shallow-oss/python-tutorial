import numpy as np
import sys

# 2.打印数组
# 一维数组打印为行
print(np.arange(6))
# 二维数据打印为矩阵
print(np.arange(12).reshape(4, 3))
# 三维数据打印为矩数组表
print(np.arange(24).reshape(2, 3, 4))

# 如果数组太大而无法打印，NumPy会自动跳过数组的中心部分并仅打印角点
print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))

# 要禁用此行为并强制NumPy打印整个数组，可以使用更改打印选项set_printoptions
# np.set_printoptions(threshold=sys.maxsize)
