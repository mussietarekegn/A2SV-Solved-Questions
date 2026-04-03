class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def helper(i,arr):
            if len(arr)>=2:
                res.append(arr[:])
                # return 
            
            sett=set()
            
            for j in range(i,len(nums)):
                if nums[j] in sett:
                    continue 
                if not arr or nums[j]>=arr[-1]:
                    sett.add(nums[j])
                    arr.append(nums[j])
                    helper(j+1,arr)
                    arr.pop()
                    
        helper(0,[])

        return res