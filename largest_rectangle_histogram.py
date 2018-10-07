class Solution:
    def largestRectangleArea(self, heights):
        if not heights: return 0
        stack = [0]
        largest = 0
        i = 1
        while i < len(heights):
            if heights[i] < heights[i-1]:
                while stack and heights[stack[-1]] > heights[i]:
                    popped = stack.pop()
                    largest = max(largest, heights[popped] * (i - 1 - (stack[-1] if stack else -1)))
            stack.append(i)
            i += 1

        while stack:
            popped = stack.pop()
            # print(i, popped, stack, (i - 1 - (stack[-1] if stack else 0)))
            largest = max(largest, heights[popped] * (i - 1 - (stack[-1] if stack else -1)))

        return largest



sol = Solution()
print(sol.largestRectangleArea([2,1,2]))
# print(sol.largestRectangleArea([1,2,3,4,5,3,3,2]))
