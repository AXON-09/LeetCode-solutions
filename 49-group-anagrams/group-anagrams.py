class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for i in strs:
            frq = {}
            for j in i:
                frq[j] = frq.get(j,0) + 1
            t = tuple(sorted(frq.items()))
            grp[t] = grp.get(t,[])+[i]
        return [value for value in grp.values()]
        
