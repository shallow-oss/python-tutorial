import numpy as np

# NumPy提供熟悉的数学函数，例如sin，cos和exp，这些即为通函数
B = np.arange(3)
print(B)
# 对B中的每个元素进行指数运算，计算结果为每个元素e的幂次方
print(np.exp(B))
# 对B中每个元素开根号
print(np.sqrt(B))

C = np.array([2., -1., 4.])
D = np.array([1., 1., 1.])
print(np.add(B, np.add(C, D)))

# 通函数
# all， any， apply_along_axis， argmax， argmin， argsort， average， bincount，
# ceil， clip， conj， corrcoef， cov， cross， cumprod， cumsum， diff， dot， floor，
# inner， INV ， lexsort， max， maximum， mean， median， min， minimum， nonzero，
# outer， prod， re， round， sort， std， sum， trace， transpose， var， vdot， vectorize， where

# np.floor(x)
# x 是一个数组或标量
# 对数组中的元素进行向下取整操作,返回不大于输入值的最大整数
