class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # if len(s) == 1:
        #     return 1 if 1 <= int(s) <= 26 else 0
        memo = [1, 1 if 1 <= int(s[0]) <= 26 else 0]
        for i in range(2, len(s)+1):
            sub_str = s[:i]
            memo.append(0)
            if 1 <= int(sub_str[-1:]) <= 9:
                memo[i] += memo[i-1]
            if 10 <= int(sub_str[-2:]) <= 26:
                memo[i] += memo[i-2]
        print(memo)
        return memo[-1]

sol = Solution()
# print(sol.numDecodings("10"))
# print(sol.numDecodings("27"))
print(sol.numDecodings("02"))
