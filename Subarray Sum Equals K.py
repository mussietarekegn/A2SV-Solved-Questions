class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_sum=defaultdict(int)
        p_sum[0]=1
        summ=0
        res=0

        for r in range(len(nums)):
            summ+=nums[r]
            diff=summ-k

            if diff in p_sum:
                res+=p_sum[diff]
                
            p_sum[summ]+=1
        return res
