class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=0
        while l<len(nums):
            idx=nums[l]-1
            if nums[l]>0 and nums[l]<=len(nums) and nums[idx]!=nums[l]:
                nums[l],nums[idx]=nums[idx],nums[l]
            else:
                l+=1
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1