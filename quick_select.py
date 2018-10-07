from random import randrange

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find_kth_smallest(0, len(nums) - 1, nums, len(nums)+1-k)

    def find_kth_smallest(self, low, high, nums, k):
        if low == high:
            return nums[low]

        mid = self.partition(low, high, nums)
        if mid - low == k - 1:
            return nums[mid]
        elif mid - low > k - 1:
            return self.find_kth_smallest(low, mid-1, nums, k)
        else:
            return self.find_kth_smallest(mid+1, high, nums, k-(mid-low+1))

    def partition(self, low, high, nums):
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            print(i)
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        print(nums)
        return i + 1
