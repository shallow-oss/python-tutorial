# Matplotlib

## Pyplot

### 1.使用

```python
import matplotlib.pyplot as plt
```

### 2.常用函数

```python
# 绘制线图和散点图
plot(x, y, [format], x2, y2, [format], ..., **kwargs)
```

* x：表示x轴上的数据点的值，可以是一个数组或列表。
* y：表示y轴上的数据点的值，可以是一个数组或列表。
* format（可选）：表示线条的格式，可以是一个字符串，用于指定线条的颜色、线型和标记。常用的格式包括：
  * 颜色缩写：可以使用单个字符表示颜色，例如'r'表示红色，'b'表示蓝色，'g'表示绿色，'k'表示黑色，'w'表示白色等。
  * 线型缩写：可以使用单个字符表示线型，例如'-'表示实线，'--'表示虚线，':'表示点线，'-.‘表示点划线等。
  * 标记缩写：可以使用单个字符表示标记，例如'o'表示圆圈，'s'表示正方形，'^'表示三角形，'.'表示点等。

```python
# 绘制散点图
scatter(x, y, [size], [color])
```

* x：表示x轴上的数据点的值，可以是一个数组或列表。
* y：表示y轴上的数据点的值，可以是一个数组或列表。
* size（可选）：表示散点的大小，可以是一个标量或与x、y相同长度的数组或列表。默认情况下，散点的大小为20。
* color（可选）：表示散点的颜色，可以是一个颜色名称、颜色缩写或与x、y相同长度的数组或列表。默认情况下，散点的颜色为蓝色。

```python
# 绘制条形图
bar(x, height, [width], [bottom], [align])
```

* x：表示条形图中每个条形的x轴位置，可以是一个数组或列表。
* height：表示条形图中每个条形的高度，可以是一个数组或列表。
* width（可选）：表示条形的宽度，默认为0.8。
* bottom（可选）：表示条形的底部位置，默认为None，即从0开始绘制。
* align（可选）：表示条形的对齐方式，默认为'center'，即条形在给定的x位置上居中。

```python
# 绘制直方图
hist(x, [bins], [density], [color])
```

* x：表示要绘制直方图的数据，可以是一个数组或列表。
* bins（可选）：表示直方图的柱子数量或柱子边界。默认情况下，bins为10，表示将数据分成10个柱子。
* density（可选）：表示是否对直方图进行标准化处理。默认情况下，density为False，表示直方图的高度表示样本数量。如果将density设置为True，则直方图的高度表示样本占比。
* color（可选）：表示直方图的颜色。可以是一个颜色名称、颜色缩写或颜色的RGB值。

```python
# 绘制饼图
pie(x, [labels], [colors], [autopct])
```

* x：表示饼图的数据，可以是一个数组或列表。
* labels（可选）：表示饼图中各个部分的标签，可以是一个字符串列表。
* colors（可选）：表示饼图中各个部分的颜色，可以是一个颜色列表。
* autopct（可选）：表示饼图中各个部分的百分比格式化字符串。

```python
# 绘制图像
imshow(X, [cmap])
```

* X：表示要绘制的图像数据，可以是一个二维数组或一个表示图像的三维数组（如RGB图像）。
* cmap（可选）：表示用于着色的颜色映射。默认情况下，cmap为None，表示使用默认的颜色映射。

```python
# 绘制等高线图
contour(X, Y, Z, [levels], [colors])
```

* X：表示网格的x坐标，可以是一个二维数组。
* Y：表示网格的y坐标，可以是一个二维数组。
* Z：表示在网格上每个点的高度值，可以是一个二维数组。
* levels（可选）：表示要绘制的等高线的高度值。可以是一个数值列表或整数，表示要绘制的等高线的数量。
* colors（可选）：表示等高线的颜色。

```python
# 绘制箱线图
boxplot(x, [notch], [sym], [vert], [whis], [positions], [widths])
```

* x：表示要绘制箱线图的数据，可以是一个一维数组或一个二维数组。
* notch（可选）：表示是否绘制缺口框。默认为False，表示不绘制缺口框。
* sym（可选）：表示异常值的标记符号。默认为'+'，表示使用加号标记。
* vert（可选）：表示箱线图的方向。默认为True，表示垂直方向绘制箱线图。
* whis（可选）：表示箱线图的须的长度。默认为1.5，表示须的长度为1.5倍的四分位距。
* positions（可选）：表示箱线图的位置。默认为None，表示根据数据自动确定箱线图的位置。
* widths（可选）：表示箱线图的宽度。默认为0.5，表示箱线图的宽度为0.5。

```python
# 绘制三维表面图
plot_surface(X, Y, Z, [rstride], [cstride], [cmap])
```

* X：表示网格的x坐标，可以是一个二维数组。
* Y：表示网格的y坐标，可以是一个二维数组。
* Z：表示在网格上每个点的高度值，可以是一个二维数组。
* rstride（可选）：表示行的步长，默认为1，表示每隔1行绘制一个表面。
* cstride（可选）：表示列的步长，默认为1，表示每隔1列绘制一个表面。
* cmap（可选）：表示颜色映射，默认为None，表示使用默认的颜色映射。

```python
# 绘制三维散点图
scatter3D(x, y, z, [c], [s])
```

* x：表示散点的x坐标，可以是一个一维数组。
* y：表示散点的y坐标，可以是一个一维数组。
* z：表示散点的z坐标，可以是一个一维数组。
* c（可选）：表示散点的颜色，可以是一个一维数组或一个标量。默认为None，表示使用默认的颜色映射。
* s（可选）：表示散点的大小，可以是一个一维数组或一个标量。默认为None，表示使用默认的散点大小。

## 轴标签和标题

### 1. 轴标签

```python
plt.xlabel("x - label")
plt.ylabel("y - label")
```

### 2. 标题

```python
plt.title("TITLE")
```

## 网格线

```python
plt.grid(color='red', linestyle='--', linewidth=0.5)
```

* color：指定网格线的颜色。可以是一个字符串（如'red'、'blue'等），也可以是一个RGB元组（如(0.5, 0.5, 0.5)表示灰色），默认为'gray'。
* linestyle：指定网格线的线型。可以是一个字符串（如'solid'、'dashed'、'dotted'等），也可以是一个符号（如'-'表示实线，'--'表示虚线，':'表示点线），默认为'-'。
* linewidth：指定网格线的线宽，以点为单位。可以是一个标量（如1、2等），默认为0.5。
* alpha：指定网格线的透明度，取值范围为0到1之间。默认为None，表示不透明。
* axis：指定要添加网格线的轴。可以是一个字符串（如'both'、'x'、'y'等），也可以是一个轴对象（如plt.gca().xaxis表示当前轴的x轴），默认为'both'，表示添加到x和y轴。
* which：指定要添加的网格线类型。可以是一个字符串（如'major'、'minor'等），也可以是一个元组（如('major', 'minor')），默认为'major'，表示添加主要网格线。