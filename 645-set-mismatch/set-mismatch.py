class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        lst = set(range(1,len(nums)+1))
        s = set(nums)
        for i in range(len(nums)):
            if nums[i] in seen:
                p = list(lst-(s))
                return [nums[i], p[0]]
            else:
                seen.add(nums[i]) 
        