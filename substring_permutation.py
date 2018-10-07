class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in s2[0:len(s1)]:
            if ch in freq:
                freq[ch] -=1

        i = 0
        while i <= len(s2) - len(s1):
            if all(val == 0 for key, val in freq.items()):
                return True
            if s2[i] in freq:
                freq[s2[i]] += 1
            i += 1
            new_ch_indx = i + len(s1) - 1
            if new_ch_indx < len(s2) and s2[i+len(s1)-1] in freq:
                freq[s2[new_ch_indx]] -= 1
        return False


sol = Solution()
print(sol.checkInclusion("abc", "adacb"))
print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("ccc", "cbac"))
print(sol.checkInclusion("hello", "ooolleoooleh"))
