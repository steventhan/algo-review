def find_kth(nums1, nums2, k):
    # import pdb; pdb.set_trace()
    if not nums1:
        return nums2[k-1]
    if not nums2:
        return nums1[k-1]

    mid1 = len(nums1) // 2
    mid2 = len(nums2) // 2
    if mid1 + mid2 >= k-1:
        if nums1[mid1] > nums2[mid2]:
            return find_kth(nums1[:mid1], nums2, k)
        else:
            return find_kth(nums1, nums2[:mid2], k)
    else:
        if nums1[mid1] > nums2[mid2]:
            return find_kth(nums1, nums2[mid2+1:], k-mid2-1)
        else:
            return find_kth(nums1[mid1+1:], nums2, k-mid1-1)

# nums1 = []
# nums2 = [3, 5, 7]
# assert find_kth(nums1, nums2, 3) == 7

nums1 = [1, 4, 6, 8]
nums2 = [2, 3, 6, 7]
# assert find_kth(nums1, nums2, 4) == 3
print(find_kth(nums1, nums2, 7))

def find_kth2(k, nums1, nums2):
    if len(nums1) == 0:
        return nums2[k]
    if len(nums2) == 0:
        return nums1[k]

    mid1 = len(nums1) // 2
    mid2 = len(nums2) // 2
    # import pdb; pdb.set_trace()
    if k > mid1 + mid2:
        if nums1[mid1] > nums2[mid2]:
            return find_kth2(k - mid2 - 1, nums1, nums2[mid2 + 1:])
        else:
            return find_kth2(k - mid1 - 1, nums1[mid1 + 1:], nums2)
    else:
        if nums1[mid1] > nums2[mid2]:
            return find_kth2(k, nums1[:mid1], nums2)
        else:
            return find_kth2(k, nums1, nums2[:mid2])

assert find_kth2(7, nums1, nums2) == find_kth(nums1, nums2, 8)
assert find_kth2(6, nums1, nums2) == find_kth(nums1, nums2, 7)
assert find_kth2(5, nums1, nums2) == find_kth(nums1, nums2, 6)
assert find_kth2(4, nums1, nums2) == find_kth(nums1, nums2, 5)
assert find_kth2(3, nums1, nums2) == find_kth(nums1, nums2, 4)
assert find_kth2(2, nums1, nums2) == find_kth(nums1, nums2, 3)
assert find_kth2(1, nums1, nums2) == find_kth(nums1, nums2, 2)
assert find_kth2(0, nums1, nums2) == find_kth(nums1, nums2, 1)
