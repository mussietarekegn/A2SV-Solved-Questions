class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_=float('-inf')
        p_sum=0

        for r in range(len(nums)):
            if p_sum<0:
                p_sum=0
            p_sum+=nums[r]
            max_=max(max_,p_sum)
        
        return max_