# solved on 2025-06-23
# beats 64% in memory (python)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for n in nums:
            try:
                d[n]+=1
            except:
                d[n]=1
            if d[n]> len(nums)//2: return n
        
