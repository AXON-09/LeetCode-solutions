class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        for i in strs:
            frq = {}
            for j in i:
                frq[j] = frq.get(j,0) + 1
            lst.append(frq)
        i = [s for s in range(len(lst))]
        grp = []
        while i:
           j = i[0]
           l = [strs[j]]
           rem = []
           for s in i[1:]:
               if lst[j] == lst[s]:
                   l.append(strs[s])
               else:
                   rem.append(s)
           i = rem    
           grp.append(l)
        return grp
            



        