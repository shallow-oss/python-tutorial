import numpy as np

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
             dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print(x)
print(x[1])
print(x['age'])
x['age'] = 5
print(x)

# 结构化数据类型创建

# 1. 元组列表，每个字段一个元组
# 元组形式 （字段名称、数据类型、形状（可选））
x = np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))])
print(x)

# 如果 fieldname 是空字符串 '' ，则将为字段指定格式为 f# 的默认名称， 其中 # 是字段的整数索引，从左侧开始从0开始计数
x = np.dtype([('x', 'f4'), ('', 'i4'), ('z', 'i8')])
print(x)

# 2. 逗号分隔的数据类型规范字符串
# 数据类型由逗号分隔，字段名称被赋予默认名称 f0、f1等
x = np.dtype('i8, f4, S3')
print(x)

# 3. 字段参数组字典
# 字典有两个必需键 “names” 和 “format”
# 四个可选键 “offsets”、“itemsize”、“Aligned” 和 “title”
x = np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4']})
print(x)
x = np.dtype({'names': ['col1', 'col2'],
              'formats': ['i4', 'f4'],
              'offsets': [0, 4],
              'itemsize': 12})
print(x)

# 操作和显示结构化数据类型
d = np.dtype([('x', 'i8'), ('y', 'f4')])
# 在dtype对象的属性中找到结构化数据类型的字段名称列表
print(d.names)
# fields 键:字段名称 值:包含每个字段的dtype和字节偏移量的元组
