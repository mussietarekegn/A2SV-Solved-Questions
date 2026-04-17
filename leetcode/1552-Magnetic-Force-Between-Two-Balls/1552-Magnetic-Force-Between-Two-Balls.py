class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(mid):
            j=0
            count=1
            nonlocal m

            for i in range(1,len(position)):
                if position[i]-position[j]>=mid:
                    count+=1
                    j=i

            return count>=m

        l=1
        r=position[-1]-position[0]
        ans=0
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        
        return ans