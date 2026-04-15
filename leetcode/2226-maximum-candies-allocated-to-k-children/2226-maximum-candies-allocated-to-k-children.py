class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        ans=0

        while l<=r:
            mid=(l+r)//2
            count=0
            for c in candies:
                count+=c//mid
            if count>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        
        return ans
    
            

