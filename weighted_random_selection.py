import random
from collections import Counter

def weighted_choice_sub(weights):
    rand = random.randrange(sum(weights))
    for i, w in enumerate(weights):
        print(rand, w)
        rand -= w
        if rand < 0:
            return i


# c = Counter()
# for i in range(100000):
#     c[weighted_choice_sub([1, 2, 3])] += 1
weighted_choice_sub([1, 2, 3])
# print(c)