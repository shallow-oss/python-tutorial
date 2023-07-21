# while
# 多重赋值
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b

# if
x = 2

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for
# Python中的for可以迭代列表或字符串等任意序列
# 元素的迭代顺序与在序列中出现的顺序一致
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# 遍历时修改列表的内容，容易造成错误。因此不能直接进行循环，应遍历该集合的副本或创建新的集合
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# copy() 复制操作
# items() 函数以列表返回可遍历的(键, 值) 元组数组
# 遍历该集合的副本
for user, status in users.copy().items():
    print(user,status)
    if status == 'inactive':
        del users[user]
print(users)

# 创建新的集合
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# range() 常用于遍历数字序列
# range(stop) 计数从 0 开始到 stop 结束，不包括 stop
# range(begin,stop[,step])  计数从 start(默认为0) 开始到 stop 结束不包括 stop 以 step(默认为1) 为步长
for i in range(6):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# range() 和 len() 组合在一起，可以按索引迭代序列
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range() 返回的对象和列表很像，但并未生成真正的列表，从而节省空间
# 这种称为可迭代对象
print(range(10))

# 循环语句支持 else 子句
# for 循环中，可迭代对象中的元素全部循环完毕，或 while 循环的条件为假时，执行该子句
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue 继续执行循环的下一次迭代
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# pass 不执行任何操作
# 语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句

# match 
# 将一个目标值与一个或多个字面值进行比较
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # 使用 | 在一个模式中可以组合多个字面值
        case 401 | 403 | 404:
            return "Not allowed"
        # _ 被作为通配符并必定会匹配成功
        case _:
            return "Something's wrong with the internet"

print(http_error(401))

# 类似解包赋值,可被用于绑定变量
def point(point):
    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

point((3,5))

# 函数
# 默认值参数，函数有多种方式调用
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

i = 5
# 默认值在 定义 作用域里的函数定义中求值
def f(arg=i):
    print(arg)

i = 6
print("---------------------------------------")
f()

# 会累积后续调用时传递的参数
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 不想在后续调用之间共享默认值
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# 不能对同一个参数多次赋值
def function(a):
    pass
# 错误调用
# function(0, a=0)

# 最后一个形参为 **name 形式时，接收一个字典
# *arguments 传入的为元组
# **keywords 传入的为字典
# 传入方式
''' 
    def fun(参数, *arg, **kwarg)
    fun( 参数1, arg1, arg2, ...,
                键1 = 值1,键2 = 值2,...)
'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 特殊参数
# 最常见形式函数定义，可以按位置也可以按关键字传递参数
def standard_arg(arg):
    print(arg)

standard_arg(2)
standard_arg(arg=2)

# 函数定义中有 /，仅限使用位置传递参数， / 只能写在参数后
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)
# pos_only_arg(arg=1) 无法使用

# 通过 * 表明后续仅限关键字参数, * 只能写在参数前
def kwd_only_arg(*, arg):
    print(arg)

# kwd_only_arg(3) 无法使用
kwd_only_arg(arg=3)

# 使用了全部的调用形式 / *
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)

# 可变参数，*args一般位于形参列表的末尾
# *args 形参后的任何形式参数只能是关键字参数，不能用作位置参数
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# 解包实参列表
# 函数调用要求独立的位置参数
print(list(range(3, 6)))
# 如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来
args = [3, 6]
print(*args)
print(list(range(*args)))

# ** 操作符可以解包字典
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# lambda 表达式
def make_incrementor(n):
    # lambda 关键字用于创建小巧的匿名函数
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

# 把匿名函数用作传递的实参
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)