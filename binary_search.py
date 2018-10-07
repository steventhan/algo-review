def binary_search(lst, num):
    return _binary_search(lst, num, 0, len(lst) - 1)


def _binary_search(lst, num, low, high):
    if low > high:
        raise ValueError("Not found")
    middle = (low + high) // 2
    if lst[middle] < num:
        return _binary_search(lst, num, middle+1, high)
    elif lst[middle] > num:
        return _binary_search(lst, num, low, middle-1)
    else:
        return middle