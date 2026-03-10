class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp={}
        stack=[]

        for i in range(len(nums2)):
            
            while stack and stack[-1]<nums2[i]:
                prev=stack.pop()
                mapp[prev]=nums2[i]

            stack.append(nums2[i])
        res=[]

        while stack:
            mapp[stack.pop()]=-1
        for i in range(len(nums1)):
            res.append(mapp[nums1[i]])
        
        return res

            
