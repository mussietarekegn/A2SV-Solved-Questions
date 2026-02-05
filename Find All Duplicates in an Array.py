class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapp=defaultdict(int)
        ans=[]

        for i in range(len(nums)):
            mapp[nums[i]]+=1
        
        for keys,values in mapp.items():
            if values>1:
                ans.append(keys)
        
        return ans
