class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        p_sum=[0]*(len(nums)+1)

        for num in requests:
            l=num[0]
            r=num[1]
            p_sum[l]+=1
            p_sum[r+1]-=1
        
        for i in range(1,len(p_sum)):
            p_sum[i]+=p_sum[i-1]
        
        nums.sort(reverse=True)
        p_sum.sort(reverse=True)

        ans=[0]*(len(nums)+1)

        for i in range((len(nums))):
            ans[i]=p_sum[i]*nums[i]
        
        return sum(ans)%1000000007
