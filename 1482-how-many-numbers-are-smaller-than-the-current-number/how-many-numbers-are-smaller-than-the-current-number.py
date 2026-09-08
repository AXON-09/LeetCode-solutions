class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101

        # Count frequency of each number
        for num in nums:
            count[num] += 1

        # Convert frequency into number of elements smaller than each number
        for i in range(1, 101):
            count[i] += count[i - 1]

        # Build answer
        ans = []

        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(count[num - 1])

        return ans