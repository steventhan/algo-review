
def fib(n):
    if n < 2: return n
    i = 1
    num1 = 0
    num2 = 1

    while i < n:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i += 1
    return num3

def fib_recursive(n):
    def _fib(n, num1, num2):
        if n < 1: return num1
        return _fib(n-1, num2, num1+num2)
    return _fib(n, 0, 1)
print([fib(i) for i in range(10)])
print([fib_recursive(i) for i in range(10)])
