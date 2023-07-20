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
