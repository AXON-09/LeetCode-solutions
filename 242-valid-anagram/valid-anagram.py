class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        fs = {}
        ft = {}

        for c1, c2 in zip(s, t):
            fs[c1] = fs.get(c1, 0) + 1
            ft[c2] = ft.get(c2, 0) + 1

        return fs == ft
