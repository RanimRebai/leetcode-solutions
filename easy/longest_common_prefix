# Solved on 2025-06-22
# Beats 100% in runtime (python)
# Memory: beats 60%

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
            if prefix =="": return prefix
        return prefix
        
