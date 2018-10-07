
def find_subarray(array):
    current_max = global_max = array[0]

    for i in range(1, len(array)):
        current_max = max(current_max, current_max + array[i])
        global_max = max(current_max, global_max)

    return global_max

print(find_subarray([1, -3]))
