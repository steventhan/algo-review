class Solution:
    def trap(self, heights):
        if not heights: return 0
        stack = [0]
        trapped = 0
        i = 1
        import pdb; pdb.set_trace()
        while i < len(heights):
            if heights[stack[0]] <= heights[i]:
                shorter = heights[stack[0]]
                while stack:
                    popped = stack.pop()
                    trapped += shorter - heights[popped]
            stack.append(i)
            i += 1

        while stack:
            popped = stack.pop()
            # print(i, popped, stack, (i - 1 - (stack[-1] if stack else 0)))
            largest = max(largest, heights[popped] * (i - 1 - (stack[-1] if stack else -1)))

        return largest

    def trap2(self, height):
        stack = []
        index = 0
        water = 0
        import pdb; pdb.set_trace()
        while index < len(height):
            if len(stack) == 0 or height[index] <= height[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                bottom = stack.pop()
                if len(stack) != 0:
                    shorter = min(height[stack[-1]], height[index])
                    water += (shorter - height[bottom]) * (index - stack[-1] - 1)
        return water

    def trap3(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        import pdb; pdb.set_trace()
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

sol = Solution()
print(sol.trap3([0,1,0,2,1,0,1,3,2,1,2,1]))
