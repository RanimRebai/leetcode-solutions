#solved on 2025 - 06 -24
#beats 80% in memory

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = ""
        for digit in digits:
            n+=str(digit)
        n = str(int(n)+1)
        l = list(int(i) for i in n)
        return l

