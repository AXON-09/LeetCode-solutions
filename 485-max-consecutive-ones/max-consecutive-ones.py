class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        mx = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                a += 1
                mx = max(a,mx)
            else:
                a = 0
        return mx 

