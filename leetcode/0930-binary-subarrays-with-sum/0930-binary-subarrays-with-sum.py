class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p_sum=defaultdict(int)
        res=0
        p_sum[0]+=1
        curr=0

        for r in range(len(nums)):
            curr+=nums[r]
            res+=p_sum[curr-goal]
            p_sum[curr]+=1
        return res
