class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=0

        while l<len(nums):
            idx=nums[l]-1
            if nums[l]!=nums[idx]:
                nums[l],nums[idx]=nums[idx],nums[l]
            else:
                l+=1
        
        ans=[]

        for i in range(len(nums)):
            if i+1!=nums[i]:
                ans.append(nums[i])
                ans.append(i+1)
        
        return ans