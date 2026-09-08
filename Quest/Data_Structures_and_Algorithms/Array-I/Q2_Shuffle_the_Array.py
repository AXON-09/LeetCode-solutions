class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0]*n*2
        for i in range(n):
            arr[i*2] = nums[i]
            arr[(i*2)+1] = nums[n+i]
        return arr

