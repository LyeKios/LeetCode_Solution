class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while(len(s)):
            conutL = s[:i].count('L')
            countR = s[:i].count('R')
            if (conutL == countR) and countR and conutL:
                ans += 1
                s = s[i:]
                # print (s)
                i = 0
            i += 1

        return ans