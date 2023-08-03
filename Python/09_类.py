# 类
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

# 定义类


class Complex:
    # 创建带有特定初始状态的自定义实例
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

# 设计类
'''
class 类名称:
    类的属性
    类的行为
'''


class Student:
    name = None
    gender = None
    nation = None
    native = None
    age = None

    # self 必须存在，用来表示类自身的意思
    # 传参时可以不用考虑self
    def say_hi(self):
        print(f"大家好，我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")


# 创建一个对象
stu_1 = Student()

# 对象属性赋值
stu_1.name = "zzp"
stu_1.gender = "男"
stu_1.age = 22
stu_1.nation = "china"
stu_1.native = "ZJ"

# 获取对象中的记录信息
print(stu_1.name)
stu_1.say_hi()
# 调用时当 self 不存在
stu_1.say_hi2("hhhhhh")


class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"id:{clock1.id},价格:{clock1.price}")
# clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"id:{clock2.id},价格:{clock2.price}")
# clock2.ring()

# 构造方法
# __init__()
# 在创建类对象时会自动执行
# 在创建类对象时将传入参数自动传递给__init__方法使用


class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"name:{self.name},age:{self.age},tel:{self.tel}")


student = Student("zzp", 24, "13757633776")
