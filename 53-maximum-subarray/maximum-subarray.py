class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]

        for num in nums[1:]:
            if cur < 0:
                cur = num
            else:
                cur += num

            if cur > ans:
                ans = cur

        return ans