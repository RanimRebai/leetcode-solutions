#solved on 2025-06-22
#beats 51% in memory

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        for i in range(len(s)//2):
            if s[i]!=s[-1-i]: return False
        return True
