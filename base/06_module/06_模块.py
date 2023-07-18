import fibo

fibo.fib(1000)

print(fibo.fib2(100))

from fibo import fib, fib2

fib(500)

print(fib2(500))

from fibo import *

fib(500)

# 模块名后使用 as 时，直接把 as 后的名称与导入模块绑定
import fibo as fib

fib.fib(500)

from fibo import fib as fibonacci

fibonacci(500)

# 内置函数 dir() 用于查找模块定义的名称。返回结果是经过排序的字符串列表
import fibo, sys
print(dir(fibo))
print(dir(sys))