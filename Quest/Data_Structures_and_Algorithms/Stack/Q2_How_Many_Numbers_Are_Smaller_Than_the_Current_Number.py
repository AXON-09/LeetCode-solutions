class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for i in nums:
            count[i] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        return [count[x-1] if x!=0 else 0 for x in nums]
        
