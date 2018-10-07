def my_func():
    lst = [1, 2, 3, 4]
    return list(filter(is_even, lst))

def is_even(x):
    return x % 2 == 0


print(my_func())