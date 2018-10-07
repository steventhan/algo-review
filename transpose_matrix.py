class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        print(list(zip([1,2,3], [4, 5, 6])))
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], A[j][i])
                A[i][j], A[j][i] = A[j][i], A[i][j]
        print(A)
        return A

sol = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
sol.transpose(m)
