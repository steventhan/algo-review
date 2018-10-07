class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0

        print(len(haystack)-len(needle)+1)
        for i in range(len(haystack)-len(needle)+1):
            print(i, haystack[i:i+len(needle)])
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1

sol = Solution()
print(sol.strStr("hello", "o"))
