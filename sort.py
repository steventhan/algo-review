def mergesort(nums):
    return _mergesort(0, len(nums)-1, nums)


def _mergesort(lo, hi, nums):
    if lo == hi:
        return
    mid = (lo + hi) // 2
    _mergesort(lo, mid, nums)
    _mergesort(mid+1, hi, nums)
    merge(lo, mid, hi, nums)


def merge(lo, mid, hi, nums):
    left = []
    right = []
    for i in range(lo, mid+1):
        left.append(nums[i])

    for i in range(mid+1, hi+1):
        right.append(nums[i])

    left_idx = right_idx = 0
    i = lo
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            nums[i] = right[right_idx]
            right_idx += 1
        else:
            nums[i] = left[left_idx]
            left_idx += 1
        i += 1

    while left_idx < len(left):
        nums[i] = left[left_idx]
        left_idx += 1
        i += 1

from random import shuffle

for i in range(1000):
    nums1 = [i for i in range(10)]
    shuffle(nums1)
    nums2 = sorted(nums1)
    mergesort(nums1)
    assert nums1 == nums2
