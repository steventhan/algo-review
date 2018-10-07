class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[-1]*(m+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 or j == 1: matrix[i][j] = 1
                else: matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] 
        print(matrix)

sol = Solution()
print(sol.uniquePaths(3, 2))
