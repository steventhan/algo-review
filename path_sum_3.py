from node import TreeNode

class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        import pdb; pdb.set_trace()
        # exit condition
        if root is None:
            return
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1

node1 = TreeNode(1)
node3 = TreeNode(3)
node1b = TreeNode(1)

node1.left = node3
node3.left = node1b
sol = Solution()
sol.pathSum(node1, 4)
