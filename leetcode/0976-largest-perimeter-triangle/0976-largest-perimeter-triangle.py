class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i+1<len(nums) and i+2<len(nums) and nums[i+1]+nums[i+2]>nums[i] :
                return nums[i+1]+nums[i+2]+nums[i]
        
        return 0

