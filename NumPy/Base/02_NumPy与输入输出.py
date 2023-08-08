import numpy as np
import io
from io import BytesIO

# delimiter
data = "1 2 3\n4 5 6"
# delimiter 关键字用于定义拆分应该如何进行，默认为None -> s空白区域（包括制表符）分割
x = np.genfromtxt(BytesIO(data.encode()))
print(x)

data = "  1  2  3\n  4  5 67\n890123  4"
# delimiter 设置为整数，按照设置的列数进行分割
x = np.genfromtxt(BytesIO(data.encode()), delimiter=3)
print(x)

# autostrip
data = "1, abc , 2\n 3, xxx, 4"
# dtype="|S5" 设置数组元素的数据类型 -> 长度为 5 的字符串
x = np.genfromtxt(BytesIO(data.encode()), delimiter=",", dtype="|S5")
print(x)
# 将 autostrip 设置为 True 当分解为字符串的元素，前面和后面的空格会去掉
x = np.genfromtxt(BytesIO(data.encode()),
                  delimiter=",", dtype="|S5", autostrip=True)
print(x)

# comments
data = """
/
/ Skip me !
/ Skip me too !
1, 2
3, 4
5, 6 /This is the third line of the data
7, 8
/ And here comes the last line
9, 0
"""
# comments 用于定义标记注释开始的字符串
# 默认 comments='#'
x = np.genfromtxt(BytesIO(data.encode()), comments='/', delimiter=",")
print(x)

# skip_header skip_footer
data = "\n".join(str(i) for i in range(10))
x = np.genfromtxt(BytesIO(data.encode()),)
print(x)
# skip_header 跳过前面 n 行 skip_footer 跳过后面 n 行
x = np.genfromtxt(BytesIO(data.encode()),
                  skip_header=3, skip_footer=5)
print(x)

# usecols
data = "1 2 3 7 8\n4 5 6 9 10"
# usecols 接受与要导入的列的索引相对应的单个整数或整数序列
x = np.genfromtxt(BytesIO(data.encode()), usecols=(0, 3, 2))
print(x)

# 设置名称
data = "1 2 3\n 4 5 6"
x = np.genfromtxt(BytesIO(data.encode()), dtype=[(_, int) for _ in "abc"])
print(x)

# names
data = "1 2 3\n 4 5 6"
x = np.genfromtxt(BytesIO(data.encode()), names="A, B, C")
print(x['A'])

# 从数据本身定义列名 names=True
data = "So it goes\n#a b c\n1 2 3\n 4 5 6"
x = np.genfromtxt(BytesIO(data.encode()), skip_header=1, names=True)
print(x['b'])

# 调整转换
# converters


def convertfunc(x): return float(x.strip("%"))/100.


data = "1, 2.3%, 45.\n6, 78.9%, 0"
names = ("i", "p", "n")
x = np.genfromtxt(BytesIO(data.encode()), delimiter=",", names=names)
print(x)
