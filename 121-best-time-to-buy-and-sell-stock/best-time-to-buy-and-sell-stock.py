class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mx = 0
        for i in prices:
            if i - mn > mx:
                mx = i - mn
            elif i < mn:
                 mn = i
        return mx

            


        