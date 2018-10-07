class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        matrix = [[0] * len(grid[0]) for i in range(len(grid))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == j == 0: matrix[i][j] = grid[i][j]
                else:
                    up = float("inf") if i - 1 < 0 else matrix[i-1][j]
                    left = float("inf") if j - 1 < 0 else matrix[i][j-1]
                    matrix[i][j] = min(up, left) + grid[i][j]

        return matrix[len(grid)-1][len(grid[0])-1]

sol = Solution()
print(sol.minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]))
