import numpy as np

# 花式索引和索引技巧

# 使用索引数组进行索引
a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
print(a)
print(a[i])

j = np.array([[3, 4], [9, 7]])
print(a[j])
