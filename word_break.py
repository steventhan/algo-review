class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        memo = {}
        return self.helper(s, word_set, memo)

    def helper(self, s, word_set, memo):
        if s == "":
            return True
        for i in range(1, len(s)+1):
            if s[:i] in word_set:
                if s[i:] not in memo:
                    memo[s[i:]] = self.helper(s[i:], word_set, memo)
                if memo[s[i:]]:
                    return True
        return False

sol = Solution()
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
