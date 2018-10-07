import pprint
def all_permutations(lst):
    result = []
    _all_permutations(lst, [], result)
    return result


def _all_permutations(lst, acc, result):
    if len(lst) == 0:
        result.append(acc)
    else:
        for i, item in enumerate(lst):
            _all_permutations(lst[:i] + lst[i+1:], acc + [item], result)


pprint.pprint((all_permutations([1, 2, 3, 4])))
