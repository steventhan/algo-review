from itertools import permutations
def solution(A):
    return level1(convert(A))

def convert(A):
    return [(A[i], A[i+1]) for i in range(0, len(A), 2)]

def level1(A):
    for i, domino in enumerate(A):
        left_over = A[:i] + A[i+1:]
        if level2(left_over, domino) or level2(left_over, domino[::-1]):
            return True
    return False

def level2(left_over, level1):
    # print(left_over, level1)
    for i in range(len(left_over)):
        for j in range(i+1, len(left_over)):
            this_levels = [
                left_over[i] + left_over[j],
                left_over[i][::-1] + left_over[j],
                left_over[i] + left_over[j][::-1],
                left_over[i][::-1] + left_over[j][::-1]
            ]
            new_left_over = left_over[:i] + left_over[i+1:j] + left_over[j+1:]
            for level in this_levels:
                if level[1:-1] == level1 and level3(new_left_over, level):
                    return True
    return False

def level3(left_over, level2):
    for permut in permutations(left_over):
        for i in range(len(permut)):
            # print("here", permut[i])
            a = permut[:i] + (permut[i],) + permut[i+1:]
            a = tuple(i for tuple in a for i in tuple)
            b = permut[:i] + (permut[i][::-1],) + permut[i+1:]
            b = tuple(i for tuple in b for i in tuple)
            print(a, b, level2)
            if a[1:-1] == level2 or b[1:-1] == level2:
                return True
    return False


A = [4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5]
print(solution(A))
