from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix, k):
        if not matrix: return 0
        pq = [(matrix[0][j], 0, j) for j in range(len(matrix[0]))]
        for _ in range(k):
            val, i, j  = heappop(pq)
            if i < len(matrix) - 1:
                print(i)
                heappush(pq, (matrix[i+1][j], i+1, j))
        return val        

sol = Solution()
matrix = [
    [1, 5, 12],
    [10, 11, 13],
    [12, 13, 15]
]
print(sol.kthSmallest(matrix, 8))
