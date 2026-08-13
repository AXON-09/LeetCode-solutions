class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        arr = [1]*len(nums)
        for i in range(len(nums)):
            arr[i] *= l
            l *= nums[i]
            arr[len(nums)-1-i] *= r
            r *= nums[len(nums)-1-i]
        return arr
            