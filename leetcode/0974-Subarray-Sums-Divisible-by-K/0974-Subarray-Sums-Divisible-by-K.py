class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p_sum=defaultdict(int)
        count=0
        summ=0
        p_sum[0]=1

        for i in range(len(nums)):
            summ+=nums[i]
            mod=summ%k

            if mod in p_sum:
                count+=p_sum[mod]
            p_sum[mod]+=1
        
        return count