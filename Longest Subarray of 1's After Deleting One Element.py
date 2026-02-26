class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        mapp=defaultdict(int)

        for r in range(len(nums)):
            mapp[nums[r]]+=1
            while mapp[0]>1:
                mapp[nums[l]]-=1
                if mapp[nums[l]]==0:
                    mapp.pop(nums[l])
                l+=1
            if mapp[0]<=1:
                if 0 in mapp:
                    ans=max(ans,(r-l+1)-1)
                else:
                    ans=max(ans,r-l+1)
        
        return ans
