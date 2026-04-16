class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=0
        while l<len(nums):
            idx=nums[l]-1
            if nums[l]!=nums[idx]:
                nums[l],nums[idx]=nums[idx],nums[l]
            else:
                l+=1
        
        ans=0

        for i in range(len(nums)):
            if i+1!=nums[i]:
                ans=nums[i]
                break
        
        return ans