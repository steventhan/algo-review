class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

    def is_palindrome(self, s):
        for i in range(len(s)//2):
            print(i, len(s)-1-i)
            if s[i] != s[len(s)-1-i]: return False
        return True

sol = Solution()
assert sol.is_palindrome("ABBA") == True
assert sol.is_palindrome("ABCBA") == True
assert sol.is_palindrome("ABC") == False
