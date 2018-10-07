def short_unsorted(lst):
    max_item = lst[0]
    min_item = lst[-1]
    n = len(lst)

    for i in range(1, n):
        max_item = max(max_item, lst[i])
        min_item = min(min_item, lst[n-i-1])

    print(max_item, min_item)
    return
    
print(short_unsorted([1, 2, 3]))
