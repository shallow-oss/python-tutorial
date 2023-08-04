# PEP8

## 一、代码布局

*  括号内隐式连接，垂直对齐
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

* if 语句过长时，可选的处理方式
```python    
# 条件连续行额外缩进
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

* 闭环括号内元素跨行
```python      
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

* 在二元运算符之前、之后断行都可，推荐之前
```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

* 空行    
```python
# 顶层函数和类定义间使用两个空行


def function1():
    pass


# 不同函数组之间使用两个空行隔离
def function2():
    pass


class MyClass:
    # 类内方法定义间使用一个空行
    def fun1():
        pass

    def fun2():
        pass
```

* 模块导入
```Python
正确：
    from subprocess import Popen, PIPE
    import os
    import sys

错误：
    import sys, os
```

模块导入总是位于文件顶部，在**模块注释**和**文档字符串**之后，模块**全局变量**和**常量**之前。

导入应该按照以下顺序分组，不同组间用空行隔离。

* 标准库 imports  
* 相关第三方 imports  
* 本地特定应用／库 imports  
  
绝对导入
```Python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

类导入
```Python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

如果这种方式导致了本地命名冲突，可以使用以下方式：
```Python
import myclass
import foo.bar.yourclass
```

## 二、 命名约定

### 描述性: 命名风格

以下命名风格通常区分彼此使用：

* b (单个小写字母)

* B (单个大写字母)

* lowercase（小写）

* lower_case_with_underscores（带下划线的小写）

* UPPERCASE（大写）

* UPPER_CASE_WITH_UNDERSCORES（带下划线的大写）

* CapitalizedWords（驼峰式）

<blockquote>Note: 使用驼峰式时，缩写全部大写，例如：HTTPServerError 好于 HttpServerError </blockquote>

* mixedCase (乌鬼头)

* Capitalized_Words_With_Underscores 

* single_trailing_underscore_ : 用来避免和 python 关键字冲突，例如：
```python
Tkinter.Toplevel(master, class_='ClassName')
```

### 规定性: 命名习惯

#### 包、模块

**模块**应该使用**简短**并且**全小写**的命名，下划线也可以提升可读性。  
**包**也应该使用简短的**全小写**名称，尽管不鼓励使用下划线。

#### 类

**类名**通常使用**驼峰式命名**习惯。

#### 异常名

异常可以看成类，所以可以使用类命名习惯，但是，如果异常是个错误类，一般加上 **"Error"** 后缀。

#### 全局变量名

我们假设这些全局变量只在一个模块内使用，这样的话和函数的命名习惯是一样的。  
设计为通过 <code>from M import *</code> 导入的类应该使用 \_\_all\_\_ 机制避免导出全局变量，或者可以使用老式的习惯，给这些全局变量名加上下划线作为前缀(表示这是非公有变量)。

#### 函数名

**全部小写**，可以使用下划线分隔单词  
例如，<code>func</code> or <code>func_write_to_file</code>  
为了向后兼容性，也可以使用 **mixedCase** 式命名风格。

#### 函数和方法参数

实例方法第一个入参一定要是 self。  
类方法第一个入参一定要是 cls。  
如果函数入参名和保留关键字冲突，则后缀下划线好过缩写或者糟糕的拼写。  
例如，class_ 好过 clss。

#### 方法名和实例变量

使用函数命名风格即可。如果希望是私有方法或实例变量，则前缀下划线。  
为避免和子类的命名冲突，请使用双下划线前缀命名。  
如果类 Foo 有一个属性变量 __a，那么通过 Foo.__a 是不能被访问的。当然，固执的用户仍然可以通过 Foo._Foo__a 访问），一般来说，双下划线前缀只是在避免子类属性命名冲突的场景下使用。

#### 常量

常量一般定义在模块级别。命名风格如：MAX_OVERFLOW 或 TOTAL 。

#### 简略说明

1. 包、模块名：**全部小写**，可以使用下划线分隔单词，例如：my_module.py

2. 函数、变量和属性名：**全部小写**，可以使用下划线分隔单词，例如：my_variable

3. 类名：采用**驼峰命名法**（首字母大写），例如：MyClass

4. 函数和方法的参数名：采用**小写字母**，可以使用下划线分隔单词，例如：my_parameter

5. 常量名：**全部大写**，可以使用下划线分隔单词，例如：MY_CONSTANT

6. 类的实例变量名：采用**小写字母**，可以使用下划线分隔单词，例如：my_instance_variable

7. 类的私有实例变量名：以一个下划线开头，例如：_private_variable

8. 类的私有方法名：以一个下划线开头，例如：_private_method

9.  类的保护实例变量名：以一个下划线开头，例如：_protected_variable

10. 类的公共实例变量名：避免使用前导下划线，例如：public_variable

## 三、函数注释
``` python
"""
这是一个加法函数的示例。

参数:
x (int): 第一个加数
y (int): 第二个加数

返回:
int: 两个数的和
"""
``` 

## 四、编码建议

* 不要使用 ~~a += b~~ 或 ~~a = a + b~~ 来实现字符串连接，在库的性能敏感部分，应该使用 **''.join()** 的形式，这就能保证在不同的 python 实现中，连接动作可以在线性时间内完成。

* 和例如 None 这类 singleton 的比较，应该使用 is 或 is not 而不是 ==。另外，小心使用 <code>if x</code> 如果你的本意是 <code>if x is not None</code>，如果 x 是个布尔变量值 false，那可就完蛋了。
```python
正确：

    if foo is not None:

错误：

    if not foo is None:
```

* 当使用 rich comparisons （丰富的比较）实现排序操作时，最好是实现所有六种操作(\_\_eq\_\_,\_\_ne\_\_, \_\_lt\_\_, \_\_le\_\_, \_\_gt\_\_, \_\_ge\_\_)而不要依赖其他的代码去单独实现某一类比较。为了减少劳动，functools.total_ordering() decorator 提供了一个生成缺失比较方法的工具。
```python
# 简化自定义类的 rich comparisons
# 只需要实现 __eq__() 和任意一个其他比较方法（例如 __lt__()）即可

from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age
  
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1 == person2)  # 输出: False
print(person1 < person2)   # 输出: True
print(person1 <= person2)  # 输出: True
print(person1 > person2)   # 输出: False
print(person1 >= person2)  # 输出: False
```

* 使用 def 语句而不要使用赋值语句去直接绑定一个 lambda 表达式到标识符上：

```python
正确：

    def f(x): return 2*x

错误：

    f = lambda x: 2*x
```

赋值语句的使用消除了 lambda 表达式相对于显式 def 语句的唯一好处，那就是它能够嵌入到一个更大的表达式里面。

* **函数返回语句要一致**。在一个函数内的所有返回语句要么都返回一个表达式，要么都不返回。如果任何一个返回语句返回了表达式，那么其他任何没有返回值的语句应该明确声明为 return None。在函数结束部分必须出现返回语句：
```python
是：

    def foo(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return None
    
    def bar(x):
        if x < 0:
            return None
        return math.sqrt(x)

否：

    def foo(x):
        if x >= 0:
            return math.sqrt(x)
    
    def bar(x):
        if x < 0:
            return
        return math.sqrt(x)
```

* 相对于 string 模块，使用 string 方法要快的多并且与 unicode strings 共享相同的 API。当然了，除了需要考虑 2.0 版本之前 python 代码向后兼容性的情况。

* 使用 **''.startswith() 和 ''.endswith()** 而不是字符串切片来检查**前缀或后缀**，例如：

```python
是： if foo.startswith('bar'):
否： if foo[:3] == 'bar':
```

* **对象类型**比较应该使用**isinstance()** 而不是直接比较：

```python
是： if isinstance(obj, int):
否： if type(obj) is type(1):
```

当检查一个对象是否为字符串时，一定要注意这个对象也可能是 unicode 字符串！在 Python 2 中，string 和 unicode 拥有一个公共基类 basestring，因此可以这么的：

```python
if isinstance(obj, basestring):
```

在 Python 3 中，unicode 和 basestring 已然不复存在(there's only str)，并且 bytes object 也不再视为一种 string 了，而是一个整形序列。

* 对于序列（字符串，列表，元组）的判空操作：
```python
是：
    if not seq:
    if seq:

否：
    if len(seq):
    if not len(seq):
```

* 不要使用尾随空格。

* 不要使用 == 验证布尔值为 Ture 或 False：

```python
是：
      if greeting:
否：
      if greeting == True:
虾扯蛋：
      if greeting is True:
```