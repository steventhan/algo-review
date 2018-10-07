class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 1

        for i in range(32):
            # print("-----")
            print(bin(res), len(bin(res)[2:]))
            # print(bin(n))
            # res += n & 1
            res <<= 1
            n >>= 1
        return res

sol = Solution()
print(bin(2147483647))
print(bin(sol.reverseBits(2147483647)))
# print(len(bin(sol.reverseBits(2147483647))[2:]))
