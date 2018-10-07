class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
    def matched(self, s1, s2):    
        m1 = {}
        m2 = {}
        for i in range(len(s1)):
            if s1[i] not in m1 and s2[i] not in m2:
                m1[s1[i]] = s2[i]
                m2[s2[i]] = s1[i]
            elif (s1[i] in m1) ^ (s2[i] in m2):     
                return False
        print(m1, m2)
        return True    
                

sol = Solution()
print(sol.matched("dkd", "abb"))