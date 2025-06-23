#solved on 2025-06-22
#beats 42.5% in runtime
#beats 60% in memory

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            new =nums[i+1:]
            for n in new :
                
                if nums[i]+n==target:
                    return [i,new.index(n)+1+i]
        return []
