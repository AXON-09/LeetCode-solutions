class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frq = dict()
        for word in strs:
            lst = [0]*26
            for ch in word:
                lst[ord(ch) - ord('a')] += 1
            lst = tuple(lst)
            if frq.get(lst,0) == 0:
               frq[lst] = [word]
            else:
                frq[lst] = frq.get(lst) + [word]
        return list(frq.values())

            
        

                
        
            