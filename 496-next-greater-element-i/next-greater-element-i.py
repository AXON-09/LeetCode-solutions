class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=-1
        h={}
        p=[]
        s=[]
        m=-1
        for i in range(len(nums2)-1,-1,-1):
            if not s:
                h[nums2[i]]=-1
            else:
                while s:
                    if nums2[i]<s[-1]:
                        h[nums2[i]]=s[-1]
                        break
                    else:
                        s.pop()
                    if not s:
                       h[nums2[i]]=-1
                       break
            s.append(nums2[i])
        for n in nums1:
            if n in h:
                p.append(h[n])
        return p


                
            



        