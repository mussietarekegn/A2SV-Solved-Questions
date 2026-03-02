class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def res(nums,k):
            count=Counter()
            uni=0
            ans=0
            l=0

            for r in range(len(nums)):
                if count[nums[r]]==0:
                    uni+=1
                count[nums[r]]+=1

                while uni>k:
                    count[nums[l]]-=1
                    if count[nums[l]]==0:
                        count.pop(nums[l])
                        uni-=1
                    l+=1

                ans+=r-l+1
            return ans
        out=res(nums,k)-res(nums,k-1)
        return out
