class Solution(object):
    def isPalindrome(self, x):
         if x < 0 or (x % 10 == 0 and x != 0):
             return False
         tar = 0
         while x > tar:
            tar = tar * 10 + x % 10
            x //= 10
         return x == tar or x == tar // 10



s = Solution()
s.isPalindrome(121)