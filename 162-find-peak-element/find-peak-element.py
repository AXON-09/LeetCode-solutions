class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[p] < nums[i]:
                p = i
        return p
            
                    
        