class Solution:
    def mySqrt(self, x: int) -> int:
        
        l=0
        r=x
        while l<=r:
            mid=(l+r)//2
            m=mid**2
            if m==x:
                return mid
            elif m<x:
                l=mid+1
            else:
                r=mid-1
        return r