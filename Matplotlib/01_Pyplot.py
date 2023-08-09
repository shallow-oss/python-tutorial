import matplotlib.pyplot as plt
import numpy as np

# pyplot
x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
# plt.plot(x, y, x, z)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sizes = [30, 50, 70, 90, 110]
colors = ['r', 'g', 'b', 'c', 'm']
# plt.scatter(x, y, s=sizes, color=colors)

x = [1, 2, 3, 4, 5]
height = [3, 7, 2, 5, 4]
# plt.bar(x, height, width=0.5, align='center')

x = [1, 2, 2, 3, 3, 3, 4, 4, 5]
# plt.hist(x)

x = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
autopct = '%1.1f%%'
# plt.pie(x, labels=labels, colors=colors, autopct=autopct)

# 创建一个随机的灰度图像数据
X = np.random.rand(100, 100)
# 创建一个随机的RGB图像数据
X = np.random.rand(100, 100, 3)
X = np.random.rand(100, 100)
# plt.imshow(X, cmap='hot')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
levels = [0.2, 0.4, 0.6, 0.8, 1.0]
colors = 'r'
# plt.contour(X, Y, Z, levels=levels, colors=colors)

# 创建随机数据
x = np.random.randn(100)
# plt.boxplot(x, notch=True, sym='ro', vert=False, whis=1.5, widths=0.3)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, rstride=10, cstride=10)

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
c = np.random.randn(100)
s = np.random.randn(100)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter3D(x, y, z, c=c, s=s)

plt.show()
