class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        row_beg = col_beg = 0
        row_end = len(matrix) - 1
        col_end = len(matrix[0]) - 1
        res = []
        while row_beg <= row_end and col_beg <= col_end:
            for i in range(col_beg, col_end+1):
                res.append(matrix[row_beg][i])

            row_beg += 1

            for i in range(row_beg, row_end+1):
                res.append(matrix[i][col_end])

            col_end -= 1

            for i in range(col_end, col_beg-1, -1):
                res.append(matrix[row_end][i])

            row_end -= 1
            for i in range(row_end, row_beg-1, -1):
                res.append(matrix[i][col_beg])

            col_beg += 1
        return res

sol = Solution()
print(sol.spiralOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)
print(sol.spiralOrder(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
))
