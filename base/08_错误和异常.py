# 编写程序处理选定的异常
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("错误!  这不是一个有效的数字.  请再次输入...")

# try 语句的工作原理
# 1.执行 try 子句 （try 和 except 关键字之间的（多行）语句）
# 2.如果没有触发异常，则跳过 except 子句，try 语句执行完毕
# 3.如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。
#   如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。
# 4.如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外部的 try 语句中；
#   如果没有找到处理程序，则它是一个 未处理异常 且执行将终止并输出如上所示的消息。

class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。
# 它适用于 try 子句 没有引发异常但又必须要执行的代码
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# 异常处理程序不仅处理try子句中立即发生的异常，还处理try语句中调用（甚至是间接调用）的函数内部发生的异常。


def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# raise 语句支持强制触发指定的异常
# raise NameError('HiThere')

# raise ValueError
# 如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异常
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 捕获常规异常，所有类型的异常均捕获
'''
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
'''

# 捕获指定异常
'''
try:
    可能发生错误的代码
except 异常类型 as e:
    如果出现异常执行的代码
'''

# 捕获多个异常
'''
try:
    可能发生错误的代码
except (异常类型，异常类型，...): <-元组
    如果出现异常执行的代码
'''

# 捕获所有异常
'''
try:
    可能发生错误的代码
except Exception: 
    如果出现异常执行的代码
'''

# 异常else和finally
'''
try:
    可能发生错误的代码
except Exception: 
    如果出现异常执行的代码
else:
    如果没有出现异常要执行的代码
finally:
    有没有出现异常都要执行的代码
'''

# 异常具有传递性
