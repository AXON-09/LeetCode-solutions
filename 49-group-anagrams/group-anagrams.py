class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for i in strs:
            frq = {}
            for j in i.lower():
                frq[j] = frq.get(j,0) + 1
            t = tuple(sorted(frq.items()))
            grp[t] = grp.get(t, [])
            grp[t].append(i.lower())
        return [value for value in grp.values()]
        
