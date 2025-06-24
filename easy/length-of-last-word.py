#solved on 2025-06-24
#beats 100% in runtime(python)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len((s.strip().split(" "))[-1])
