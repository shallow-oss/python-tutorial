import numpy as np

# 拷贝和视图

# 完全不复制
# 简单分配不会复制数组对象或其数据
# a 和 b 是同一个数组对象的两个名字，对其中一个修改便可改变数组
a = np.arange(12)
print(a)
b = a
print(b is a)
b.shape = 3, 4
print(a)

# 视图或浅拷贝
# c 和 a 共享相同的数据，但是它们是不同的数组对象
c = a.view()
c.shape = 2, 6
print(a)
print(c)
# 对视图数组进行修改，会改变原始数组
c[0, 4] = 1234
print(a)

# 切片数组会返回一个视图
s = a[:, 1:3]
print(s)

s[:] = 10
print(a)

# 深拷贝
# copy() 方法生成数组及其数据的完整副本
d = a.copy()
d[0, 0] = 9999
print(d)
print(a)
# 如果不再需要原始数组，则应在切片后调用 copy
