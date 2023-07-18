# 模块  
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# 可以用以下方式运行 Python 模块：
# python fibo.py <arguments>
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))