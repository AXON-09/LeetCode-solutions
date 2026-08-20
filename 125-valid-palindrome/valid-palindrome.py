class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter = "".join(char for char in s.lower() if (char.isalpha() or char.isdigit()))
        l = 0
        r = len(filter) - 1
        while l < r:
            if filter[l] != filter[r]:
                return False
            l += 1
            r -= 1
        return True
